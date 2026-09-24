"""Second pass: give thin contact records a real email / contact page.

Runs only against clubs that are missing an email AND a contact page, tries the
language-appropriate contact paths on their own site, and records the URL it read.
Never invents an address: everything comes off the page that was fetched.
"""
import json
import os
import re
import time

import concurrent.futures as cf

import requests

HERE = os.path.dirname(os.path.abspath(__file__))
DATE = "2026-09-24"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

# extra paths per language, tried against the club's own root
PATHS_DE = ["/kontakt", "/de/kontakt", "/de-de/kontakt", "/impressum", "/de/impressum",
            "/de-de/impressum", "/service/kontakt", "/kontakt/kontakt"]
PATHS_ES = ["/contacto", "/es/contacto", "/club/contacto", "/aviso-legal", "/es/aviso-legal"]
PATHS_EN = ["/contact", "/contact-us", "/contactus", "/en/contact", "/en/contact-us",
            "/the-club/contact-us", "/about/contact", "/info/contact"]

DE = {"bayer-leverkusen", "borussia-monchengladbach", "eintracht-frankfurt", "sc-freiburg",
      "tsg-hoffenheim", "fc-augsburg", "union-berlin", "werder-bremen", "borussia-dortmund",
      "rb-leipzig", "mainz-05", "sc-paderborn-07", "vfb-stuttgart", "fc-koln",
      "hamburger-sv", "sv-elversberg", "schalke-04", "bayern-munich", "vfl-wolfsburg"}
ES = {"barcelona", "real-madrid", "atletico-de-madrid", "sevilla", "valencia", "villarreal",
      "real-betis", "real-sociedad", "athletic-club", "osasuna", "celta-vigo", "getafe",
      "elche", "espanyol", "mallorca", "deportivo-alaves", "rayo-vallecano", "girona",
      "levante", "malaga", "racing-santander", "deportivo-la-coruna"}

EMAIL_RE = re.compile(r'mailto:([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})')
TEL_RE = re.compile(r'tel:([+0-9()\-\s\.]{7,25})')
SKIP = ("example.", "sentry", "wixpress", "noreply", "imago-", "gettyimages", "blm.de")

S = requests.Session()
S.headers.update({"User-Agent": UA, "Accept-Language": "en-GB,en;q=0.9"})

# manual corrections where the site's own markup misleads the scrape
FIXES = {
    # the site links a news widget's handle, not the club's
    "brighton-and-hove-albion": {"drop_x": ["@Boro"], "add_x": ("@OfficialBHAFC", "https://www.brightonandhovealbion.com/")},
}


def get(url):
    for _ in range(2):
        try:
            r = S.get(url, timeout=25, allow_redirects=True)
            if r.status_code == 200 and len(r.text) > 500:
                return r.url, r.text
        except Exception:
            pass
        time.sleep(1)
    return None, None


def clean_phone(p):
    p = re.sub(r"[^+0-9]", "", p)
    if p.startswith("00"):
        p = "+" + p[2:]
    return p if len(p) >= 8 else None


def main():
    path = os.path.join(HERE, "contacts_build.json")
    data = json.load(open(path, encoding="utf-8"))
    by = {e["clubId"]: e for e in data}

    # every club gets its own homepage as a channel if the scrape did not record one,
    # so there is always a way in even when the club publishes no email
    import build_contacts as BC
    for club, sites in BC.SITES.items():
        e = by.get(club)
        if not e:
            continue
        if not any(c["type"] == "website" for c in e["channels"]):
            url = sites[-1]
            e["channels"].append({"type": "website", "value": url,
                                  "source": {"name": "Club website", "url": url, "date": DATE}})

    for club, fix in FIXES.items():
        e = by.get(club)
        if not e:
            continue
        if "drop_x" in fix:
            e["channels"] = [c for c in e["channels"]
                             if not (c["type"] == "x" and c["value"] in fix["drop_x"])]
        if "add_x" in fix:
            v, u = fix["add_x"]
            e["channels"].append({"type": "x", "value": v,
                                  "source": {"name": "Club website", "url": u, "date": DATE}})

    todo = []
    for club, e in sorted(by.items()):
        types = {c["type"] for c in e["channels"]}
        if "email" in types and "contact-form" in types:
            continue
        root = next((c["value"] for c in e["channels"] if c["type"] == "website"), None)
        if root:
            todo.append((club, root))

    def hunt(item):
        club, root = item
        e = by[club]
        types = {c["type"] for c in e["channels"]}
        paths = PATHS_DE if club in DE else PATHS_ES if club in ES else PATHS_EN
        for p in paths:
            url, html = get(root.rstrip("/") + p)
            if not url:
                continue
            low = url.lower()
            if "404" in low or "not-found" in low:
                continue
            found = []
            em = [m for m in EMAIL_RE.findall(html) if not any(k in m for k in SKIP)]
            if em and "email" not in types:
                found.append({"type": "email", "value": em[0],
                              "source": {"name": "Club website contact page", "url": url, "date": DATE}})
            tl = [t for t in (clean_phone(x) for x in TEL_RE.findall(html)) if t]
            if tl and "phone" not in types:
                found.append({"type": "phone", "value": tl[0],
                              "source": {"name": "Club website contact page", "url": url, "date": DATE}})
            if ("contact" in low or "kontakt" in low or "contacto" in low) and "contact-form" not in types:
                found.append({"type": "contact-form", "value": url, "label": "Contact page",
                              "source": {"name": "Club website contact page", "url": url, "date": DATE}})
            if found:
                return club, found, url
        return club, [], None

    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for club, found, url in ex.map(hunt, todo):
            if found:
                e = by[club]
                e["channels"].extend(
                    c for c in found if (c["type"], c["value"]) not in
                    {(x["type"], x["value"]) for x in e["channels"]})
                print(f"{club}: +{len(found)} from {url}", flush=True)

    json.dump(data, open(path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    open(path, "a").write("\n")
    thin = [e["clubId"] for e in data if len(e["channels"]) < 2]
    print("thin records left:", thin)
    print("clubs with an email:", sum(1 for e in data if any(c["type"] == "email" for c in e["channels"])))


if __name__ == "__main__":
    main()
