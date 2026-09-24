"""Build normalized/ from the website seed + curated additions, then validate.

Run:  python3 build_normalized_new.py
Writes normalized/*.json next to this file and prints the validator result.

BTJ_SEED     path to Beyond-The-Jersey/website data/seed  (default /tmp/website/data/seed)
BTJ_VALIDATE path to Beyond-The-Jersey/website validate.py
"""
import json
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pipeline_data as A

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = os.environ.get("BTJ_SEED", "/tmp/website/data/seed")
OUT = os.path.join(HERE, "normalized")
VALIDATE = os.environ.get("BTJ_VALIDATE", "/tmp/website/data/validate.py")


def load(name):
    with open(os.path.join(SEED, name + ".json"), encoding="utf-8") as f:
        return json.load(f)


def write(name, obj):
    with open(os.path.join(OUT, name + ".json"), "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


os.makedirs(OUT, exist_ok=True)

# ------------------------------------------------------------------ meta
meta = load("meta")
meta["generatedBy"] = "Beyond-The-Jersey data pipeline (scripts/)"
meta["updatedAt"] = A.D
try:
    meta["sourceCommit"] = subprocess.run(
        ["git", "-C", HERE, "rev-parse", "--short", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
except Exception:
    pass
write("meta", meta)

# ------------------------------------------------------------------ sports / leagues / scales
sports = load("sports")
have = {s["id"] for s in sports}
sports += [s for s in A.NEW_SPORTS if s["id"] not in have]
write("sports", sports)

leagues = load("leagues")
have = {l["id"] for l in leagues}
leagues += [l for l in A.NEW_LEAGUES if l["id"] not in have]
for l in leagues:
    if l["id"] == "la-liga":
        l["notes"] = ["All 20 clubs for 2026-27 are in the data; front sponsors are unrated."]
    if l["id"] == "bundesliga":
        l["notes"] = [
            "All 18 clubs for 2026-27 are in the data; front sponsors are unrated.",
            "Bayern Munich dropped Qatar Airways in 2023 and moved away from Visit Rwanda in 2025.",
        ]
    if l["id"] == "nba":
        l["notes"] = ["LA Clippers x Visit Rwanda (since 2025), value not disclosed; fronts not mapped yet."]
    if l["id"] == "nfl":
        l["notes"] = ["LA Rams x Visit Rwanda (since 2025), at the stadium rather than on the shirt."]
write("leagues", leagues)

write("levels", load("levels"))
write("tiers", load("tiers"))

# ------------------------------------------------------------------ clubs
clubs = load("clubs")
by_id = {c["id"]: c for c in clubs}
for c in A.NEW_CLUBS:
    by_id.setdefault(c["id"], c)
if "schalke-04" in by_id:
    by_id["schalke-04"]["leagueId"] = "bundesliga"
    by_id["schalke-04"]["hasTeamPageDesign"] = False
clubs = list(by_id.values())
write("clubs", clubs)
print("clubs:", len(clubs))

# ------------------------------------------------------------------ owners / sponsors
owners = load("owners")
oid = {o["id"]: o for o in owners}
for o in A.NEW_OWNERS:
    oid.setdefault(o["id"], o)
# a few owners for existing seed sponsors
for extra in [
    A._o("qualcomm", "Qualcomm", "listed-company", "USA"),
    A._o("aia-group", "AIA Group", "listed-company", "Hong Kong"),
    A._o("standard-chartered-plc", "Standard Chartered plc", "listed-company", "United Kingdom"),
    A._o("kaizen-gaming", "Kaizen Gaming", "private-company", "Greece"),
]:
    oid.setdefault(extra["id"], extra)
owners = list(oid.values())
# seed style: country and via are left out when unknown, not set to null
for o in owners:
    for k in ("country", "via"):
        if o.get(k) is None:
            o.pop(k, None)
write("owners", owners)

ssponsors = load("sponsors")
sid = {s["id"]: s for s in ssponsors}
for s in A.NEW_SPONSORS:
    sid.setdefault(s["id"], s)
for name, owner in [
    ("snapdragon", "qualcomm"),
    ("aia", "aia-group"),
    ("standard-chartered", "standard-chartered-plc"),
    ("betano", "kaizen-gaming"),
]:
    if name in sid:
        sid[name]["ownerId"] = owner
        sid[name]["ownership"] = "owned"
if "etihad-airways" in sid:
    sid["etihad-airways"]["claimIds"] = ["uae-mass-trial-2024", "uae-mass-trial-upheld-2025"]
    sid["etihad-airways"].pop("note", None)
sponsors = list(sid.values())
write("sponsors", sponsors)
print("sponsors:", len(sponsors))

# ------------------------------------------------------------------ claims
claims = load("claims")
for c in claims:
    url, note = A.CLAIM_URLS.get(c["id"], (None, None))
    if url:
        c["source"]["url"] = url
        c["source"].pop("note", None)
        if note:
            c["source"]["note"] = note
claims += A.EXTRA_CLAIMS
write("claims", claims)

# ------------------------------------------------------------------ kits
kits = load("kits")
have = {k["id"] for k in kits}
for club, sponsor, srckey in A.FRONTS:
    kid = f"{club}-2026-27-home"
    if kid in have:
        continue
    kits.append({
        "id": kid,
        "clubId": club,
        "season": "2026-27",
        "kitType": "home",
        "periodLabel": "2026/27",
        "periodFrom": "2026-27",
        "periodTo": "2026-27",
        "photos": {},
        "sponsors": [{"sponsorId": sponsor, "placement": "front", "source": A.SRC[srckey]}],
        "sponsorsComplete": False,
        "summary": None,
        "change": None,
    })
# source on the seed's own 2026-27 kit sponsors where we have one
PL_CLUB_IDS = {c["id"] for c in json.load(open(os.path.join(SEED, "clubs.json")))
               if c.get("leagueId") == "premier-league"}
SEED_KIT_SOURCE = {
    "newcastle-united": {
        "name": "The Mag",
        "date": "2026-06",
        "url": "https://www.themag.co.uk/2026/06/newcastle-united-have-agreed-new-main-sponsor-front-of-shirt-three-year-deal-to-replace-sela/",
    },
    "real-madrid": A.SRC["footballkitarchive"] if False else {
        "name": "SportsPro",
        "date": "2026-06-10",
        "url": "https://www.sportspro.com/news/sponsorship-marketing/real-madrid-emirates-record-sponsorship-june-2026/",
    },
    "manchester-city": {
        "name": "All Football",
        "date": "2026",
        "url": "https://m.allfootballapp.com/news/EPL/Manchester-City-set-to-keep-up-%C2%A367.5million-a-year-deal-with-Abu-Dhabi-airline-Etihad/2424047",
    },
    "arsenal": {
        "name": "Sporting Goods Intelligence",
        "date": "2026-08-06",
        "url": "https://www.sgieurope.com/marketing/emirates-and-arsenal-extend-shirt-deal-to-2033/122576.article",
    },
    "aston-villa": {
        "name": "SportsPro (citing The Athletic)",
        "date": "2026-07-15",
        "url": "https://www.sportspro.com/news/sponsorship-marketing/aston-villa-visit-rwanda-shirt-principal-sponsorship-july-2026/",
    },
}
for k in kits:
    if k["season"] != "2026-27":
        continue
    # seed kits whose front the seed left empty (filled from the 2026/27 overview)
    if not k["sponsors"] and k["clubId"] in A.PL_FILL:
        k["sponsors"] = [{
            "sponsorId": A.PL_FILL[k["clubId"]],
            "placement": "front",
            "source": A.PL_FILL_SOURCE,
        }]
    src = SEED_KIT_SOURCE.get(k["clubId"])
    if not src and not k["sponsors"]:
        continue
    if not src:
        # scoreandchange overview covers every club in the league
        src = (A.SRC["scoreandchange-pl"] if k["clubId"] in PL_CLUB_IDS
               else A.SRC["scoreandchange-laliga"])
    for p in k["sponsors"]:
        p.setdefault("source", src)
write("kits", kits)
print("kits:", len(kits))

# ------------------------------------------------------------------ deals
deals = load("deals")
have = {d["id"] for d in deals}
for club, sponsor, placement, frm, to, value, srckey, note in A.NEW_DEALS:
    did = f"{club}-{sponsor}".replace("-", "-")
    if did in have:
        continue
    d = {
        "id": did,
        "clubId": club,
        "orgName": None,
        "sponsorId": sponsor,
        "placement": placement,
        "from": frm,
        "to": to,
        "value": value,
        "source": A.SRC[srckey],
    }
    if note:
        d["note"] = note
    deals.append(d)
    have.add(did)
for row in A.UNDISCLOSED_DEALS:
    if len(row) == 8:
        club, sponsor, placement, frm, to, value, srckey, note = row
    else:
        club, sponsor, srckey = row
        placement, frm, to, value, note = "front", "2026-27", None, None, "Value not disclosed."
    did = f"{club}-{sponsor}"
    if did in have:
        continue
    d = {
        "id": did,
        "clubId": club,
        "orgName": None,
        "sponsorId": sponsor,
        "placement": placement,
        "from": frm,
        "to": to,
        "value": value,
        "source": A.SRC[srckey],
    }
    if note:
        d["note"] = note
    deals.append(d)
    have.add(did)
# the deal id for the Arsenal sleeve that replaced Visit Rwanda
for d in deals:
    if d["id"] == "arsenal-deel":
        d["source"] = {
            "name": "SportsPro (citing The Athletic)",
            "date": "2026-07-15",
            "url": "https://www.sportspro.com/news/sponsorship-marketing/aston-villa-visit-rwanda-shirt-principal-sponsorship-july-2026/",
        }
write("deals", deals)
print("deals:", len(deals))

# ------------------------------------------------------------------ double-checks
for d in deals:
    if d["id"] == "city-etihad":
        d["note"] = ("GBP67.5m a year, from an older report. SportsPro's 2026/27 season "
                     "analysis does not restate a figure, so the number stays as the last "
                     "published value rather than being re-estimated.")
for sp in sponsors:
    if "LeadMonitor" in (sp.get("note") or ""):
        sp["note"] = sp["note"].replace(
            " (LeadMonitor, verify)",
            " (checked against Score and Change and SportsPro, 2026/27)")
# bal-visit-rwanda is a real deal and Visit Rwanda publishes it themselves
for d in deals:
    if d["id"] == "bal-visit-rwanda":
        d["source"] = {
            "name": "Visit Rwanda, Basketball Africa League partnership",
            "date": "2025",
            "url": "https://visitrwanda.com/basketball-africa-league/",
        }

write("kits", kits)
print("kits:", len(kits))
write("deals", deals)

# ------------------------------------------------------------------ changes / dropped
changes = load("changes")
changes += [c for c in A.EXTRA_CHANGES if c["id"] not in {x["id"] for x in changes}]
changes.sort(key=lambda c: c["id"], reverse=True)
write("changes", changes)

dropped = load("dropped")
for d in dropped:
    src = A.DROPPED_SOURCES.get(d["id"])
    if src:
        d["source"] = src
        d.pop("todo", None)
write("dropped", dropped)

# ------------------------------------------------------------------ contacts
# top up any club the network pass missed, using the sourced overrides
cpath = os.path.join(HERE, "contacts_build.json")
contacts = json.load(open(cpath, encoding="utf-8")) if os.path.exists(cpath) else []
import build_contacts as BC  # noqa: E402

have = {c["clubId"] for c in contacts}
club_ids = {c["id"] for c in clubs}
for cid in sorted(club_ids - have):
    if cid in BC.OVERRIDES:
        contacts.append({"clubId": cid, "channels": BC.OVERRIDES[cid], "lastChecked": A.D})
        print("contacts: override for", cid)
    else:
        print("contacts: STILL MISSING", cid)
contacts.sort(key=lambda c: c["clubId"])
write("contacts", contacts)
print("contacts:", len(contacts))

# ------------------------------------------------------------------ validate
r = subprocess.run([sys.executable, VALIDATE, OUT, "--assets", "/tmp/website/public"],
                   capture_output=True, text=True, errors="replace")
out = r.stdout.strip()
errs = [l for l in out.splitlines() if l.startswith("error:")]
warns = [l for l in out.splitlines() if l.startswith("warning:")]
print(f"\nvalidator exit={r.returncode} errors={len(errs)} warnings={len(warns)}")
for l in errs[:40]:
    print(" ", l)
print("---- tail ----")
print("\n".join(out.splitlines()[-6:]))
