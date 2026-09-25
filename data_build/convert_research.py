"""Convert research outputs into one additions file the builder can apply.

Sources: /tmp/coverage.json (Serie A + MLS clubs), /tmp/sleeves.json (PL sleeves),
/tmp/f1.json (2026 F1 grid), /tmp/f1ratings.json (F1 sponsor ratings).

Writes /tmp/data/research_additions.json. Nothing is added twice: anything already in
normalized/ wins, so re-running is safe.
"""
import json
import os
import re
import unicodedata

D = "/tmp/verify/normalized"
J = lambda n: json.load(open(os.path.join(D, n + ".json"), encoding="utf-8"))
have_clubs = {c["id"] for c in J("clubs")}
have_sponsors = {s["id"]: s for s in J("sponsors")}
have_owners = {o["id"] for o in J("owners")}

SEASON = "2026-27"
DATE_TODAY = "2026-09-24"

F1_TEAM_LEAGUE = "formula-1"
F1_TEAM_COUNTRY = {
    "red-bull-racing": "United Kingdom", "ferrari": "Italy", "mercedes": "United Kingdom",
    "mclaren": "United Kingdom", "aston-martin": "United Kingdom", "alpine": "United Kingdom",
    "williams": "United Kingdom", "racing-bulls": "Italy", "haas": "United States",
    "audi": "Germany", "cadillac": "United States",
}

PLACEMENT = {"title": "front", "front": "front", "sleeve": "sleeve",
             "rear": "back", "back": "back", "other": "partner"}


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.lower().replace("&", " and ").replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return re.sub(r"-{2,}", "-", s)


# ids the research pass got wrong or left un-slugged
ID_FIX = {"***": "fc-cincinnati"}


def clean_name(n):
    """Drop the parenthetical explainer, keep the trading name."""
    return re.sub(r"\s*\(.*?\)\s*$", "", n or "").strip() or n


def fix_date(src):
    """The schema wants a string date. Research sometimes gives null - take the year
    out of the URL rather than inventing one, and only fall back to the season."""
    if not isinstance(src, dict):
        return src
    if not src.get("date"):
        m = re.search(r"/(20\d\d)/", (src.get("url") or "") + "/")
        src["date"] = m.group(1) if m else "2026"
        src.setdefault("note", "date precision: year")
    src.setdefault("name", "source")
    return src


out = {"clubs": [], "owners": [], "sponsors": [], "kits": [], "sleeves": {}, "ratings": []}
seen_owner, seen_sponsor = set(), set()

# ---------------------------------------------------------------- Serie A + MLS clubs
cov = json.load(open("/tmp/coverage.json", encoding="utf-8"))
for key, lid in (("serie_a", "serie-a"), ("mls", "mls")):
    for c in cov.get(key, []):
        cid = ID_FIX.get(c["id"], c["id"])
        if cid in have_clubs:
            continue
        out["clubs"].append({
            "id": cid, "name": c["name"], "shortName": c.get("shortName") or c["name"],
            "code": c.get("code"), "sportId": "soccer", "leagueId": lid,
            "country": c.get("country") or None, "crest": None, "aliases": [],
        })
        have_clubs.add(cid)
        fs = c.get("frontSponsor") or {}
        sid, sname = fs.get("id"), fs.get("name")
        if not sid or not sname:
            continue
        if sid not in have_sponsors and sid not in seen_sponsor:
            out["sponsors"].append({
                "id": sid, "name": sname, "ownerId": None, "ownership": None,
                "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [],
                "aliases": [], "ownerGuess": slug(sname),
            })
            seen_sponsor.add(sid)
        out["kits"].append({
            "id": cid + "-" + SEASON + "-home", "clubId": cid, "season": SEASON,
            "kitType": "home", "periodLabel": SEASON, "periodFrom": "2026", "periodTo": "2027",
            "photos": {}, "sponsors": [{"sponsorId": sid, "placement": "front",
                                        "source": fs.get("source")}],
            "sponsorsComplete": False, "change": None,
            "summary": (c.get("notes") or None),
        })

# ---------------------------------------------------------------- Premier League sleeves
sleeves = json.load(open("/tmp/sleeves.json", encoding="utf-8"))
for row in sleeves.get("clubs", []):
    cid = row["clubId"]
    for placement, key in (("sleeve", "sleeve"), ("shorts", "shorts")):
        s = row.get(key)
        if not s or not s.get("sponsorId"):
            continue
        sid, sname = s["sponsorId"], s["name"]
        if sid not in have_sponsors and sid not in seen_sponsor:
            out["sponsors"].append({
                "id": sid, "name": sname, "ownerId": None, "ownership": None,
                "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [],
                "aliases": [], "ownerGuess": slug(sname),
            })
            seen_sponsor.add(sid)
        out["sleeves"].setdefault(cid, []).append(
            {"sponsorId": sid, "placement": placement, "source": s.get("source")})

# ---------------------------------------------------------------- F1 grid
f1 = json.load(open("/tmp/f1.json", encoding="utf-8"))
owner_alias = {}
for t in f1["teams"]:
    c = t["club"]
    cid = c["id"]
    if cid not in have_clubs:
        out["clubs"].append({
            "id": cid, "name": c["name"], "shortName": c.get("shortName") or c["name"],
            "code": c.get("code"), "sportId": "motorsport", "leagueId": F1_TEAM_LEAGUE,
            "country": F1_TEAM_COUNTRY.get(cid, c.get("country")), "crest": None, "aliases": [],
        })
        have_clubs.add(cid)
    for o in t.get("owners") or []:
        oid = o["id"]
        base = re.sub(r"-(rb|am|a|h|c|w|s)$", "", oid)
        alias = base if base != oid else oid
        owner_alias[oid] = alias
        if alias in have_owners or alias in seen_owner:
            continue
        out["owners"].append({
            "id": alias, "name": clean_name(o["name"]), "type": o.get("type"),
            "country": o.get("country"), "parentId": owner_alias.get(o.get("parentId")),
        })
        seen_owner.add(alias)
    kit_sponsors = []
    for s in t.get("sponsors") or []:
        sid = s["id"]
        base = re.sub(r"-(rb|am|a|h|c|w|s)$", "", sid)
        if base in have_sponsors:
            sid = base
        if sid[0].isdigit():
            sid = "s-" + sid
        if sid not in have_sponsors and sid not in seen_sponsor:
            out["sponsors"].append({
                "id": sid, "name": clean_name(s["name"]), "ownerId": None, "ownership": None,
                "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [],
                "aliases": [], "ownerGuess": slug(clean_name(s["name"])),
            })
            seen_sponsor.add(sid)
        kit_sponsors.append({"sponsorId": sid,
                             "placement": PLACEMENT.get(s.get("placement"), "partner"),
                             "source": s.get("source")})
    out["kits"].append({
        "id": cid + "-2026-home", "clubId": cid, "season": "2026", "kitType": "home",
        "periodLabel": "2026", "periodFrom": "2026", "periodTo": "2026", "photos": {},
        "sponsors": kit_sponsors, "sponsorsComplete": False, "change": None,
        "summary": "2026 car. " + (t.get("notes") or [""])[0][:200] if t.get("notes") else None,
    })
for s in f1.get("leagueWideSponsors") or []:
    sid = s["id"]
    if sid not in have_sponsors and sid not in seen_sponsor:
        out["sponsors"].append({
            "id": sid, "name": clean_name(s["name"]), "ownerId": None, "ownership": None,
            "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [],
            "aliases": [], "ownerGuess": slug(clean_name(s["name"])),
        })
        seen_sponsor.add(sid)

# ---------------------------------------------------------------- F1 ratings
if os.path.exists("/tmp/f1ratings.json"):
    raw = json.load(open("/tmp/f1ratings.json", encoding="utf-8"))
    for r in (raw["ratings"] if isinstance(raw, dict) else raw):
        sid = re.sub(r"-(rb|am|a|h|c|w|s)$", "", r["sponsorId"])
        if sid in have_sponsors:
            continue
        src = (r.get("claim") or {}).get("source") or {}
        if not src.get("url"):
            continue
        r["sponsorId"] = sid
        r["owner"]["id"] = owner_alias.get(r["owner"]["id"], r["owner"]["id"])
        # the encoder's shape needs short + verdict; research gives only text
        text = re.sub(r"\s+", " ", (r["claim"].get("text") or "")).strip()
        short = text.split(". ")[0].strip()
        if len(short) > 165:
            short = short[:164].rsplit(" ", 1)[0] + "\u2026"
        if not short.endswith((".", "!", "?")):
            short += "."
        r["claim"]["short"] = short
        r["verdict"] = "Owned by " + r["owner"]["name"] + ". Nothing found." \
            if r["tier"] == "none" else short
        r.setdefault("ownership", "owned")
        r.setdefault("confidence", None)
        out["ratings"].append(r)

for k in out["kits"]:
    for pp in k["sponsors"]:
        pp["source"] = fix_date(pp.get("source"))
for v in out["sleeves"].values():
    for pp in v:
        pp["source"] = fix_date(pp.get("source"))
for r in out["ratings"]:
    r["claim"]["source"] = fix_date(r["claim"].get("source"))

out["clubs"].sort(key=lambda c: c["id"])
out["sponsors"].sort(key=lambda s: s["id"])
out["owners"].sort(key=lambda o: o["id"])
with open("/tmp/data/research_additions.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("clubs      ", len(out["clubs"]))
print("  by league", {x: sum(1 for c in out['clubs'] if c['leagueId'] == x)
                      for x in {c['leagueId'] for c in out['clubs']}})
print("sponsors   ", len(out["sponsors"]))
print("owners     ", len(out["owners"]))
print("kits       ", len(out["kits"]))
print("sleeves    ", sum(len(v) for v in out["sleeves"].values()), "on", len(out["sleeves"]), "clubs")
print("ratings    ", len(out["ratings"]))
