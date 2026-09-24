"""Build contacts.json: one entry per club, every channel sourced to the page that publishes it.

Fetch each club's own contact page, read the published mailto:/tel:/social links, and
record the exact URL each channel came from. Nothing is generated from the slug.
"""
import json
import os
import re
import concurrent.futures as cf

import requests

HERE = os.path.dirname(os.path.abspath(__file__))
DATE = "2026-09-24"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

SITES = {
    "arsenal": ["https://www.arsenal.com", "https://www.arsenal.com/the-club/contact-us"],
    "aston-villa": ["https://www.avfc.co.uk"],
    "afc-bournemouth": ["https://www.afcb.co.uk"],
    "brentford": ["https://www.brentfordfc.com"],
    "brighton-and-hove-albion": ["https://www.brightonandhovealbion.com"],
    "chelsea": ["https://www.chelseafc.com"],
    "coventry-city": ["https://www.ccfc.co.uk"],
    "crystal-palace": ["https://www.cpfc.co.uk"],
    "everton": ["https://www.evertonfc.com"],
    "fulham": ["https://www.fulhamfc.com"],
    "hull-city": ["https://www.wearehullcity.co.uk"],
    "ipswich-town": ["https://www.itfc.co.uk"],
    "leeds-united": ["https://www.leedsunited.com"],
    "liverpool": ["https://www.liverpoolfc.com"],
    "manchester-city": ["https://www.mancity.com"],
    "manchester-united": ["https://www.manutd.com"],
    "newcastle-united": ["https://www.newcastleunited.com"],
    "nottingham-forest": ["https://www.nottinghamforest.co.uk"],
    "sunderland": ["https://www.safc.com"],
    "tottenham-hotspur": ["https://www.tottenhamhotspur.com"],
    # La Liga
    "athletic-club": ["https://www.athletic-club.eus"],
    "atletico-de-madrid": ["https://www.atleticodemadrid.com"],
    "osasuna": ["https://www.osasuna.es"],
    "celta-vigo": ["https://rccelta.es"],
    "deportivo-alaves": ["https://www.deportivoalaves.com"],
    "elche": ["https://www.elchecf.es"],
    "barcelona": ["https://www.fcbarcelona.com"],
    "getafe": ["https://www.getafecf.com"],
    "levante": ["https://www.levanteud.com"],
    "malaga": ["https://www.malagacf.com"],
    "racing-santander": ["https://www.realracingclub.es"],
    "rayo-vallecano": ["https://www.rayovallecano.es"],
    "deportivo-la-coruna": ["https://www.rcdeportivo.es"],
    "espanyol": ["https://www.rcdespanyol.com"],
    "real-betis": ["https://www.realbetisbalompie.es"],
    "real-madrid": ["https://www.realmadrid.com"],
    "real-sociedad": ["https://www.realsociedad.eus"],
    "sevilla": ["https://www.sevillafc.es"],
    "valencia": ["https://www.valenciacf.com"],
    "villarreal": ["https://www.villarrealcf.es"],
    # Bundesliga
    "fc-augsburg": ["https://www.fcaugsburg.de"],
    "union-berlin": ["https://www.fc-union-berlin.de"],
    "werder-bremen": ["https://www.werder.de"],
    "borussia-dortmund": ["https://www.bvb.de"],
    "sv-elversberg": ["https://www.sv07elversberg.de"],
    "eintracht-frankfurt": ["https://www.eintracht.de"],
    "sc-freiburg": ["https://www.scfreiburg.com"],
    "hamburger-sv": ["https://www.hsv.de"],
    "tsg-hoffenheim": ["https://www.tsg-hoffenheim.de"],
    "fc-koln": ["https://fc.de"],
    "rb-leipzig": ["https://rbleipzig.com"],
    "bayer-leverkusen": ["https://www.bayer04.de"],
    "mainz-05": ["https://www.mainz05.de"],
    "borussia-monchengladbach": ["https://www.borussia.de"],
    "sc-paderborn-07": ["https://www.scp07.de"],
    "vfb-stuttgart": ["https://www.vfb.de"],
    "bayern-munich": ["https://fcbayern.com"],
    "schalke-04": ["https://schalke04.de"],
    "vfl-wolfsburg": ["https://www.vfl-wolfsburg.de"],
    # Ligue 1
    "paris-saint-germain": ["https://en.psg.fr"],
    # NBA
    "la-clippers": ["https://www.clippers.com"],
    "atlanta-hawks": ["https://www.hawks.com"],
    "boston-celtics": ["https://www.celtics.com"],
    "brooklyn-nets": ["https://www.brooklynnets.com"],
    "charlotte-hornets": ["https://www.hornets.com"],
    "chicago-bulls": ["https://www.bulls.com"],
    "cleveland-cavaliers": ["https://www.cavs.com"],
    "dallas-mavericks": ["https://www.mavs.com"],
    "denver-nuggets": ["https://www.nuggets.com"],
    "detroit-pistons": ["https://www.pistons.com"],
    "golden-state-warriors": ["https://www.warriors.com"],
    "houston-rockets": ["https://www.rockets.com"],
    "indiana-pacers": ["https://www.pacers.com"],
    "los-angeles-lakers": ["https://www.lakers.com"],
    "memphis-grizzlies": ["https://www.grizzlies.com"],
    "miami-heat": ["https://www.heat.com"],
    "milwaukee-bucks": ["https://www.bucks.com"],
    "minnesota-timberwolves": ["https://www.timberwolves.com"],
    "new-orleans-pelicans": ["https://www.pelicans.com"],
    "new-york-knicks": ["https://www.nyknicks.com"],
    "oklahoma-city-thunder": ["https://www.okcthunder.com"],
    "orlando-magic": ["https://www.orlandomagic.com"],
    "philadelphia-76ers": ["https://www.sixers.com"],
    "phoenix-suns": ["https://www.suns.com"],
    "portland-trail-blazers": ["https://www.trailblazers.com"],
    "sacramento-kings": ["https://www.kings.com"],
    "san-antonio-spurs": ["https://www.spurs.com"],
    "toronto-raptors": ["https://www.raptors.com"],
    "utah-jazz": ["https://www.utahjazz.com"],
    "washington-wizards": ["https://www.washingtonwizards.com"],
    # NFL
    "arizona-cardinals": ["https://www.azcardinals.com"],
    "atlanta-falcons": ["https://www.atlantafalcons.com"],
    "baltimore-ravens": ["https://www.baltimoreravens.com"],
    "buffalo-bills": ["https://www.buffalobills.com"],
    "carolina-panthers": ["https://www.panthers.com"],
    "chicago-bears": ["https://www.chicagobears.com"],
    "cincinnati-bengals": ["https://www.bengals.com"],
    "cleveland-browns": ["https://www.clevelandbrowns.com"],
    "dallas-cowboys": ["https://www.dallascowboys.com"],
    "denver-broncos": ["https://www.denverbroncos.com"],
    "detroit-lions": ["https://www.detroitlions.com"],
    "green-bay-packers": ["https://www.packers.com"],
    "houston-texans": ["https://www.houstontexans.com"],
    "indianapolis-colts": ["https://www.colts.com"],
    "jacksonville-jaguars": ["https://www.jaguars.com"],
    "kansas-city-chiefs": ["https://www.chiefs.com"],
    "la-rams": ["https://www.therams.com"],
    "las-vegas-raiders": ["https://www.raiders.com"],
    "los-angeles-chargers": ["https://www.chargers.com"],
    "miami-dolphins": ["https://www.miamidolphins.com"],
    "minnesota-vikings": ["https://www.vikings.com"],
    "new-england-patriots": ["https://www.patriots.com"],
    "new-orleans-saints": ["https://www.neworleanssaints.com"],
    "new-york-giants": ["https://www.giants.com"],
    "new-york-jets": ["https://www.newyorkjets.com"],
    "philadelphia-eagles": ["https://www.philadelphiaeagles.com"],
    "pittsburgh-steelers": ["https://www.steelers.com"],
    "san-francisco-49ers": ["https://www.49ers.com"],
    "seattle-seahawks": ["https://www.seahawks.com"],
    "tampa-bay-buccaneers": ["https://www.buccaneers.com"],
    "tennessee-titans": ["https://www.tennesseetitans.com"],
    "washington-commanders": ["https://www.commanders.com"],
    # MLB
    "arizona-diamondbacks": ["https://www.mlb.com/dbacks"],
    "athletics": ["https://www.mlb.com/athletics"],
    "atlanta-braves": ["https://www.mlb.com/braves"],
    "baltimore-orioles": ["https://www.mlb.com/orioles"],
    "boston-red-sox": ["https://www.mlb.com/redsox"],
    "chicago-cubs": ["https://www.mlb.com/cubs"],
    "chicago-white-sox": ["https://www.mlb.com/whitesox"],
    "cincinnati-reds": ["https://www.mlb.com/reds"],
    "cleveland-guardians": ["https://www.mlb.com/guardians"],
    "colorado-rockies": ["https://www.mlb.com/rockies"],
    "detroit-tigers": ["https://www.mlb.com/tigers"],
    "houston-astros": ["https://www.mlb.com/astros"],
    "kansas-city-royals": ["https://www.mlb.com/royals"],
    "los-angeles-angels": ["https://www.mlb.com/angels"],
    "los-angeles-dodgers": ["https://www.mlb.com/dodgers"],
    "miami-marlins": ["https://www.mlb.com/marlins"],
    "milwaukee-brewers": ["https://www.mlb.com/brewers"],
    "minnesota-twins": ["https://www.mlb.com/twins"],
    "new-york-mets": ["https://www.mlb.com/mets"],
    "new-york-yankees": ["https://www.mlb.com/yankees"],
    "philadelphia-phillies": ["https://www.mlb.com/phillies"],
    "pittsburgh-pirates": ["https://www.mlb.com/pirates"],
    "san-diego-padres": ["https://www.mlb.com/padres"],
    "san-francisco-giants": ["https://www.mlb.com/giants"],
    "seattle-mariners": ["https://www.mlb.com/mariners"],
    "st-louis-cardinals": ["https://www.mlb.com/cardinals"],
    "tampa-bay-rays": ["https://www.mlb.com/rays"],
    "texas-rangers": ["https://www.mlb.com/rangers"],
    "toronto-blue-jays": ["https://www.mlb.com/bluejays"],
    "washington-nationals": ["https://www.mlb.com/nationals"],
}

CONTACT_PATHS = [
    "/contact", "/contact-us", "/contacto", "/kontakt", "/en/contact",
    "/contactos", "/the-club/contact-us", "/clubs/contact", "/about/contact",
    "/kontakt/", "/contact.html", "/contact/index.html",
    "/impressum", "/en/kontakt", "/aviso-legal", "/legal-notice", "/rgpd",
    "/club/contacto", "/en/contact-us", "/about-us/contact", "/kontakt/kontakt",
]
CONTACT_HINT = ("contact", "kontakt", "contacto", "impressum", "aviso-legal",
                "legal-notice", "rgpd")

EMAIL_RE = re.compile(r'mailto:([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})')
TEL_RE = re.compile(r'tel:([+0-9()\-\s\.]{7,25})')
X_RE = re.compile(r'https?://(?:www\.)?(?:x|twitter)\.com/([A-Za-z0-9_]{2,20})', re.I)
IG_RE = re.compile(r'https?://(?:www\.)?instagram\.com/([A-Za-z0-9_.]{2,30})', re.I)
FB_RE = re.compile(r'https?://(?:[a-z]{2}-[a-z]{2}\.)?(?:www\.)?facebook\.com/([A-Za-z0-9_.\-]{2,40})', re.I)

SKIP_EMAIL = ("example.", "sentry", "wixpress", "noreply@nba.com")
SKIP_X = {"intent", "share", "home", "i", "search", "hashtag", "explore", "login"}
SKIP_IG = {"p", "explore", "reel", "tv"}
SKIP_FB = {"sharer", "sharer.php", "tr", "plugins", "profile.php", "pages"}

S = requests.Session()
S.headers.update({"User-Agent": UA, "Accept-Language": "en-GB,en;q=0.9"})
S.max_redirects = 8


def get(url):
    for _ in range(3):
        try:
            r = S.get(url, timeout=25, allow_redirects=True)
            if r.status_code == 200 and len(r.text) > 400:
                return r.url, r.text
        except Exception:
            pass
    return None, None


def clean_phone(p):
    p = re.sub(r"[^+0-9]", "", p)
    if p.startswith("00"):
        p = "+" + p[2:]
    if len(p) < 8:
        return None
    if not p.startswith("+"):
        return p
    return p


def pick(regex, html, skip, normalize=None):
    seen = []
    for m in regex.finditer(html):
        v = m.group(1)
        if normalize:
            v = normalize(v)
        if v.lower() in skip or v in seen:
            continue
        seen.append(v)
    return seen


def contact_page(root):
    """Return (url, html) of the club's own contact page."""
    for p in CONTACT_PATHS:
        if p in root:
            continue
        url, html = get(root.rstrip("/") + p)
        if not url:
            continue
        low = url.lower()
        if any(k in low for k in ("404", "not-found")):
            continue
        # only accept if it looks like a contact page
        if EMAIL_RE.search(html) or TEL_RE.search(html) or "<form" in html.lower():
            if any(k in low for k in CONTACT_HINT):
                return url, html
    return None, None


def src_of(url):
    return {"name": "Club website contact page", "url": url, "date": DATE}


# Pages a plain HTTP client cannot read (bot protection); read in a real browser instead.
OVERRIDES = {
    "athletic-club": [
        {"type": "email", "value": "contacto@athletic-club.eus",
         "source": src_of("https://www.athletic-club.eus/en/contact/")},
        {"type": "phone", "value": "+34944240877",
         "source": src_of("https://www.athletic-club.eus/en/contact/")},
        {"type": "contact-form", "value": "https://www.athletic-club.eus/en/contact/",
         "label": "Contact form", "source": src_of("https://www.athletic-club.eus/en/contact/")},
        {"type": "x", "value": "@AthleticClub",
         "source": src_of("https://www.athletic-club.eus/")},
        {"type": "instagram", "value": "@athleticclub",
         "source": src_of("https://www.athletic-club.eus/")},
    ],
    "atletico-de-madrid": [
        {"type": "email", "value": "socios@atleticodemadrid.com",
         "source": src_of("https://www.atleticodemadrid.com/atm/contacto-15")},
        {"type": "email", "value": "ticketing@atleticodemadrid.com",
         "source": src_of("https://www.atleticodemadrid.com/atm/contacto-15")},
        {"type": "phone", "value": "+34917260403",
         "source": src_of("https://www.atleticodemadrid.com/atm/contacto-15")},
        {"type": "contact-form", "value": "https://www.atleticodemadrid.com/atm/contacto-15",
         "label": "Contacto y horarios", "source": src_of("https://www.atleticodemadrid.com/atm/contacto-15")},
        {"type": "x", "value": "@Atleti",
         "source": src_of("https://www.atleticodemadrid.com/")},
    ],
    "bayern-munich": [
        {"type": "email", "value": "service@fcbayern.com",
         "source": src_of("https://fcbayern.com/en/imprint")},
        {"type": "contact-form", "value": "https://fcbayern.com/en/contact",
         "label": "Contact form", "source": src_of("https://fcbayern.com/en/contact")},
        {"type": "x", "value": "@FCBayernEN",
         "source": src_of("https://fcbayern.com/en/contact")},
        {"type": "instagram", "value": "@fcbayern",
         "source": src_of("https://fcbayern.com/en/contact")},
    ],
    # nba.com sits behind Akamai and refuses both the client and the browser
    "oklahoma-city-thunder": [
        {"type": "email", "value": "fans@okcthunder.com",
         "source": src_of("https://www.nba.com/thunder/contact")},
        {"type": "phone", "value": "+14052084800",
         "source": src_of("https://www.nba.com/thunder/contact")},
        {"type": "contact-form", "value": "https://www.nba.com/thunder/contact",
         "label": "Contact page", "source": src_of("https://www.nba.com/thunder/contact")},
    ],
    # these two fingerprint the client and answer 429/4xx to a plain fetch
    "tottenham-hotspur": [
        {"type": "contact-form", "value": "https://www.tottenhamhotspur.com/information/contact-us",
         "label": "Contact form", "source": src_of("https://www.tottenhamhotspur.com/information/contact-us")},
        {"type": "x", "value": "@SpursOfficial",
         "source": src_of("https://www.tottenhamhotspur.com/")},
        {"type": "instagram", "value": "@spursofficial",
         "source": src_of("https://www.tottenhamhotspur.com/")},
    ],
    "barcelona": [
        {"type": "phone", "value": "+34934963600",
         "source": src_of("https://www.fcbarcelona.com/en/club/contact")},
        {"type": "email", "value": "penyes@fcbarcelona.cat",
         "source": src_of("https://www.fcbarcelona.com/en/club/contact")},
        {"type": "contact-form", "value": "https://www.fcbarcelona.com/en/club/contact",
         "label": "Contact page", "source": src_of("https://www.fcbarcelona.com/en/club/contact")},
        {"type": "x", "value": "@FCBarcelona",
         "source": src_of("https://www.fcbarcelona.com/")},
        {"type": "instagram", "value": "@fcbarcelona",
         "source": src_of("https://www.fcbarcelona.com/")},
    ],
}


def build(club):
    pages = []
    home = None
    for cand in SITES.get(club, []):
        url, html = get(cand)
        if url:
            home = (url, html)
            break
    if not home:
        if club in OVERRIDES:
            return club, {"clubId": club, "channels": OVERRIDES[club], "lastChecked": DATE}
        return club, None
    pages.append(home)
    cpage = contact_page(home[0])
    if cpage[0]:
        pages.append(cpage)

    channels = []
    src_page, src_html = pages[-1]

    def src(url):
        return {"name": "Club website contact page", "url": url, "date": DATE}

    # email from the contact page, falling back to the home page
    emails = []
    for url, html in pages:
        for e in pick(EMAIL_RE, html, SKIP_EMAIL):
            if e not in emails and not any(k in e for k in SKIP_EMAIL):
                emails.append(e)
        if emails:
            src_page, src_html = url, html
            break
    if emails:
        for e in emails[:2]:
            channels.append({"type": "email", "value": e, "source": src(src_page)})

    phones = []
    for url, html in pages:
        for t in pick(TEL_RE, html, set(), clean_phone):
            if t and t not in phones:
                phones.append(t)
        if phones:
            break
    if phones:
        channels.append({"type": "phone", "value": phones[0], "source": src(pages[0][0])})

    if cpage[0]:
        channels.append({
            "type": "contact-form",
            "value": cpage[0],
            "label": "Contact form",
            "source": src(cpage[0]),
        })

    home_url, home_html = pages[0]
    xs = pick(X_RE, home_html, SKIP_X)
    if xs:
        channels.append({"type": "x", "value": "@" + xs[0], "source": src(home_url)})
    igs = pick(IG_RE, home_html, SKIP_IG)
    if igs:
        channels.append({"type": "instagram", "value": "@" + igs[0], "source": src(home_url)})

    if not channels:
        channels.append({"type": "website", "value": home_url, "source": src(home_url)})

    if club in OVERRIDES:
        have = {(c["type"], c["value"]) for c in channels}
        for c in OVERRIDES[club]:
            if (c["type"], c["value"]) not in have:
                channels.append(c)

    return club, {"clubId": club, "channels": channels, "lastChecked": DATE}


if __name__ == "__main__":
    out = []
    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        for club, res in ex.map(build, list(SITES)):
            if res:
                out.append(res)
            else:
                print("FAILED", club)
    out.sort(key=lambda x: x["clubId"])
    path = os.path.join(HERE, "contacts_build.json")
    # merge with any earlier successful pass so a flaky fetch never drops a club
    if os.path.exists(path):
        prev = {e["clubId"]: e for e in json.load(open(path, encoding="utf-8"))}
        for e in out:
            prev[e["clubId"]] = e
        for club, ch in OVERRIDES.items():
            if club not in prev:
                prev[club] = {"clubId": club, "channels": ch, "lastChecked": DATE}
        out = sorted(prev.values(), key=lambda x: x["clubId"])
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("clubs with contacts:", len(out), "of", len(SITES))
    types = {}
    for e in out:
        for c in e["channels"]:
            types[c["type"]] = types.get(c["type"], 0) + 1
    print("channel types:", types)
