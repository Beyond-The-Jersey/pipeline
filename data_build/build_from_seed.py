import json, os, glob

# Load seed data from website
import urllib.request
BASE = "https://raw.githubusercontent.com/Beyond-The-Jersey/website/main/data/seed"

def fetch(name):
    url = f"{BASE}/{name}"
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            return json.loads(r.read())
    except Exception as e:
        print(f"WARN: could not fetch {name}: {e}")
        return None

meta = fetch("meta.json") or {"schemaVersion": 1, "updatedAt": "2026-09-24"}
sports = fetch("sports.json") or []
leagues = fetch("leagues.json") or []
clubs_seed = fetch("clubs.json") or []
owners_seed = fetch("owners.json") or []
claims_seed = fetch("claims.json") or []
sponsors_seed = fetch("sponsors.json") or []
kits_seed = fetch("kits.json") or []
deals_seed = fetch("deals.json") or []
dropped_seed = fetch("dropped.json") or []
levels = fetch("levels.json") or []
tiers = fetch("tiers.json") or []

# Load pipeline data
data_dir = "/tmp/data/data"
team_files = glob.glob(os.path.join(data_dir, "*.json"))

teams = {}
for f in team_files:
    try:
        with open(f) as fh:
            t = json.load(fh)
        teams[t.get("team", "")] = t
    except:
        pass

# Build clubs.json from seed + pipeline
clubs = []
for sc in clubs_seed:
    sid = sc.get("id", "")
    t = teams.get(sid, {})
    club = {
        "id": sid,
        "name": sc.get("name", t.get("name", "")),
        "shortName": sc.get("shortName", t.get("shortName", "")),
        "code": sc.get("code", t.get("code", "")),
        "aliases": sc.get("aliases", t.get("aliases", [])),
        "leagueId": sc.get("leagueId", t.get("league", "")),
        "sportId": sc.get("sportId", t.get("sport", "")),
        "country": sc.get("country", t.get("country", "Unknown")),
        "crest": sc.get("crest", None),
    }
    clubs.append(club)

# Add pipeline teams not in seed
seed_ids = {c["id"] for c in clubs}
for slug, t in teams.items():
    if slug not in seed_ids:
        clubs.append({
            "id": slug,
            "name": t.get("name", slug),
            "shortName": t.get("shortName", ""),
            "code": t.get("code", ""),
            "aliases": t.get("aliases", []),
            "leagueId": t.get("league", ""),
            "sportId": t.get("sport", "soccer"),
            "country": t.get("country", "Unknown"),
            "crest": None,
        })

# Fix known issues from the GitHub issue
# 1. Atlético de Madrid id should be atletico-de-madrid (not atlético-de-madrid)
for c in clubs:
    if c["id"] == "atlético-de-madrid":
        c["id"] = "atletico-de-madrid"

# 2. Fix duplicate manutd / manchester-united
manutd = None
manutd_idx = None
for i, c in enumerate(clubs):
    if c["id"] == "manutd":
        manutd = c
        manutd_idx = i
        break
if manutd:
    manutd["id"] = "manchester-united"
    manutd["leagueId"] = "premier-league"

# 3. Fill country for teams with Unknown
country_map = {
    "arsenal": "England", "aston-villa": "England", "brighton-and-hove-albion": "England",
    "brentford": "England", "bournemouth": "England", "chelsea": "England",
    "crystal-palace": "England", "everton": "England", "fulham": "England",
    "ipswich-town": "England", "leicester-city": "England", "liverpool": "England",
    "manchester-city": "England", "manchester-united": "England", "newcastle-united": "England",
    "nottingham-forest": "England", "west-ham-united": "England", "wolveredhampton": "England",
    "atletico-de-madrid": "Spain", "athletic-club": "Spain", "barcelona": "Spain",
    "real-betis": "Spain", "real-madrid": "Spain", "sevilla": "Spain", "valencia": "Spain",
    "villarreal": "Spain", "real-sociedad": "Spain", "osasuna": "Spain", "getafe": "Spain",
    "mallorca": "Spain", "alaves": "Spain", "cadiz": "Spain", "rayo-vallecano": "Spain",
    "valladolid": "Spain", "granada": "Spain", "celta-vigo": "Spain", "girona": "Spain",
    "las-palmas": "Spain", "Leganes": "Spain", "real-sociedad": "Spain",
    "bayern-munich": "Germany", "borussia-dortmund": "Germany", "rb-leipzig": "Germany",
    "bayer-leverkusen": "Germany", "wolfsburg": "Germany", "eintracht-frankfurt": "Germany",
    "borussia-monchengladbach": "Germany", "freiburg": "Germany", "stuttgart": "Germany",
    "augsburg": "Germany", "mainz-05": "Germany", "heidberg": "Germany",
    "union-berlin": "Germany", "hoffenheim": "Germany", "darmstadt": "Germany",
    "koln": "Germany", "essen": "Germany", "bochum": "Germany",
    "new-york-yankees": "USA", "new-york-mets": "USA", "boston-red-sox": "USA",
    "new-york-knicks": "USA", "la-clippers": "USA", "la-rams": "USA",
    "sf-giants": "USA", "la-dodgers": "USA", "sf-49ers": "USA",
}
for c in clubs:
    if c.get("country") == "Unknown" and c["id"] in country_map:
        c["country"] = country_map[c["id"]]
    elif c.get("country") == "Unknown":
        # Try to infer from league
        lid = c.get("leagueId", "")
        if "premier" in lid: c["country"] = "England"
        elif "la-liga" in lid: c["country"] = "Spain"
        elif "bundesliga" in lid: c["country"] = "Germany"
        elif "nba" in lid: c["country"] = "USA"
        elif "nfl" in lid: c["country"] = "USA"
        elif "mlb" in lid: c["country"] = "USA"

# Build sponsors.json from seed + pipeline
sponsors = {}
for s in sponsors_seed:
    sponsors[s["id"]] = s

# Add pipeline regime sponsors
regime_sponsors = {
    "visit-rwanda": {"id": "visit-rwanda", "name": "Visit Rwanda", "ownerId": "government-of-rwanda", "ownership": "owned", "tier": "unrated", "status": "being-rated", "verdict": "Government of Rwanda tourism brand. UN experts say 3,000–4,000 troops fighting alongside M23 rebels in eastern Congo.", "claimIds": ["rwanda-troops-m23", "m23-coltan-levies"], "aliases": ["rwanda tourism"]},
    "emirates": {"id": "emirates", "name": "Emirates", "ownerId": "government-of-dubai", "ownership": "owned", "tier": "serious", "status": "rated", "verdict": "Owned by the Government of Dubai via Investment Corporation of Dubai.", "claimIds": ["uae-mass-trial-2024"], "aliases": ["emirates airline"]},
    "etihad": {"id": "etihad", "name": "Etihad Airways", "ownerId": "government-of-abu-dhabi", "ownership": "owned", "tier": "serious", "status": "rated", "verdict": "Owned by the Government of Abu Dhabi.", "claimIds": ["uae-mass-trial-2024"], "aliases": ["etihad"]},
    "riyadh-air": {"id": "riyadh-air", "name": "Riyadh Air", "ownerId": "saudi-pif", "ownership": "owned", "tier": "serious", "status": "rated", "verdict": "Owned by Saudi Arabia's sovereign wealth fund PIF, chaired by Crown Prince Mohammed bin Salman.", "claimIds": ["saudi-executions-2024", "khashoggi-assessment"], "aliases": ["riyadh"]},
    "standard-chartered": {"id": "standard-chartered", "name": "Standard Chartered", "ownerId": None, "ownership": None, "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [], "aliases": ["std chart"]},
    "turkish-airlines": {"id": "turkish-airlines", "name": "Turkish Airlines", "ownerId": null, "ownership": None, "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [], "aliases": ["turkish"]},
    "knox-hydration": {"id": "knox-hydration", "name": "KNOX Hydration", "ownerId": null, "ownership": None, "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [], "aliases": []},
    "noon": {"id": "noon", "name": "noon.com", "ownerId": null, "ownership": None, "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [], "aliases": []},
    "betano": {"id": "betano", "name": "Betano", "ownerId": null, "ownership": None, "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [], "aliases": []},
    "trade-nation": {"id": "trade-nation", "name": "Trade Nation", "ownerId": null, "ownership": None, "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [], "aliases": []},
    "kraken": {"id": "kraken", "name": "Kraken", "ownerId": null, "ownership": None, "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [], "aliases": []},
    "snapdragon": {"id": "snapdragon", "name": "Snapdragon", "ownerId": null, "ownership": None, "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [], "aliases": []},
    "aia": {"id": "aia", "name": "AIA", "ownerId": null, "ownership": None, "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [], "aliases": []},
    "cmc-markets": {"id": "cmc-markets", "name": "CMC Markets", "ownerId": null, "ownership": None, "tier": "none", "status": "rated", "verdict": "Financial services company, no state owner.", "claimIds": [], "aliases": []},
    "temporal": {"id": "temporal", "name": "Temporal", "ownerId": null, "ownership": None, "tier": "none", "status": "rated", "verdict": "UK betting tech company, no state owner.", "claimIds": [], "aliases": []},
    "clickhouse": {"id": "clickhouse", "name": "ClickHouse", "ownerId": null, "ownership": None, "tier": "none", "status": "rated", "verdict": "Database company, no state owner.", "claimIds": [], "aliases": []},
    "marex": {"id": "marex", "name": "Marex", "ownerId": null, "ownership": None, "tier": "none", "status": "rated", "verdict": "Financial services company, no state owner.", "claimIds": [], "aliases": []},
    "indeed": {"id": "indeed", "name": "Indeed", "ownerId": null, "ownership": None, "tier": "none", "status": "rated", "verdict": "Job platform, no state owner.", "claimIds": [], "aliases": []},
    "vitality": {"id": "vitality", "name": "Vitality", "ownerId": null, "ownership": None, "tier": "none", "status": "rated", "verdict": "Health insurer, no state owner.", "claimIds": [], "aliases": []},
    "riyadh-air": {"id": "riyadh-air", "name": "Riyadh Air", "ownerId": "saudi-pif", "ownership": "owned", "tier": "serious", "status": "rated", "verdict": "Owned by Saudi Arabia's sovereign wealth fund PIF, chaired by Crown Prince Mohammed bin Salman.", "claimIds": ["saudi-executions-2024", "khashoggi-assessment"], "aliases": ["riyadh"]},
    "circle": {"id": "circle", "name": "Circle/USDC", "ownerId": None, "ownership": None, "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [], "aliases": []},
}

# Merge pipeline sponsors into seed
for slug, t in teams.items():
    for sp in t.get("sponsors", []):
        spid = sp.get("name", "").lower().replace(" ", "-").replace("'", "")
        spid = spid.replace("&", "and").replace("/", "-")
        if spid not in sponsors:
            sponsors[spid] = {
                "id": spid,
                "name": sp.get("name", ""),
                "ownerId": None,
                "ownership": None,
                "tier": "unrated",
                "status": "unrated",
                "verdict": None,
                "claimIds": [],
                "aliases": sp.get("aliases", []),
            }

# Add owners from pipeline
for slug, t in teams.items():
    owner = t.get("owner", "")
    if owner and owner not in ["Unknown", ""]:
        oid = owner.lower().replace(" ", "-").replace("'", "").replace(".", "")
        if oid not in sponsors:
            sponsors[oid] = {"id": oid, "name": owner, "ownerId": None, "ownership": None, "tier": "unrated", "status": "unrated", "verdict": None, "claimIds": [], "aliases": []}

sponsors_list = list(sponsors.values())

# Build kits.json from seed + pipeline
kits = list(kits_seed)

# Add kits for teams with sponsor data
for slug, t in teams.items():
    for sp in t.get("sponsors", []):
        kit_id = f"{slug}-2026-27-home"
        # Check if kit already exists
        if not any(k["clubId"] == slug and k["season"] == "2026-27" for k in kits):
            kits.append({
                "id": kit_id,
                "clubId": slug,
                "season": "2026-27",
                "kitType": "home",
                "periodLabel": "2026/27",
                "periodFrom": "2026-27",
                "periodTo": "2026-27",
                "photos": {"front": None, "back": None},
                "sponsors": [{
                    "sponsorId": sp.get("name", "").lower().replace(" ", "-").replace("'", ""),
                    "placement": sp.get("placement", "front"),
                    "source": sp.get("sources", [None])[0] if sp.get("sources") else None,
                }],
                "sponsorsComplete": False,
                "summary": None,
            })

# Build deals.json from seed + pipeline
deals = list(deals_seed)
for slug, t in teams.items():
    for sp in t.get("sponsors", []):
        deal_id = f"{slug}-{sp.get('name','').lower().replace(' ','-')}"
        deal = {
            "id": deal_id,
            "clubId": slug,
            "orgName": None,
            "sponsorId": sp.get("name", "").lower().replace(" ", "-").replace("'", ""),
            "placement": sp.get("placement", "front"),
            "from": "2026-27",
            "to": None,
            "value": {"amount": None, "currency": None, "unit": None, "per": None, "upTo": False, "usdApprox": None},
            "source": sp.get("sources", [{"name": "Wikipedia", "date": "2026-09-24", "url": None}])[0],
            "note": None,
        }
        # Try to parse deal value
        val = sp.get("deal_value", "")
        if val:
            import re
            m = re.search(r'([£€$])\s*([\d,.]+)\s*(m|bn)?', val)
            if m:
                cur = m.group(1)
                amt = float(m.group(2).replace(',', ''))
                unit = m.group(3) or 'm'
                deal["value"] = {"amount": amt, "currency": cur, "unit": unit, "per": "year", "upTo": "up to" in val.lower(), "usdApprox": None}
        deals.append(deal)

# Build owners.json from seed + pipeline
owners = {o["id"]: o for o in owners_seed}
# Add pipeline owners
for slug, t in teams.items():
    owner = t.get("owner", "")
    if owner and owner not in ["Unknown", ""]:
        oid = owner.lower().replace(" ", "-").replace("'", "").replace(".", "")
        if oid not in owners:
            owners[oid] = {"id": oid, "name": owner, "type": "unknown", "country": None, "note": None, "parentId": None}

# Add known regime owners
known_owners = {
    "government-of-rwanda": {"id": "government-of-rwanda", "name": "Government of Rwanda", "type": "government", "country": "Rwanda", "note": None, "parentId": None},
    "government-of-dubai": {"id": "government-of-dubai", "name": "Government of Dubai", "type": "government", "country": "UAE", "note": "Via Investment Corporation of Dubai", "parentId": None},
    "saudi-pif": {"id": "saudi-pif", "name": "Public Investment Fund (Saudi Arabia)", "type": "state-fund", "country": "Saudi Arabia", "note": "Chaired by Crown Prince Mohammed bin Salman", "parentId": "government-of-saudi-arabia"},
    "government-of-saudi-arabia": {"id": "government-of-saudi-arabia", "name": "Government of Saudi Arabia", "type": "government", "country": "Saudi Arabia", "note": None, "parentId": None},
    "government-of-abu-dhabi": {"id": "government-of-abu-dhabi", "name": "Government of Abu Dhabi", "type": "government", "country": "UAE", "note": None, "parentId": None},
}
for koid, kov in known_owners.items():
    if koid not in owners:
        owners[koid] = kov

owners_list = list(owners.values())

# Build claims.json from seed + pipeline
claims = {c["id"]: c for c in claims_seed}
# Add pipeline claims
for slug, t in teams.items():
    for sp in t.get("sponsors", []):
        for src in sp.get("sources", []):
            if src and src.get("url"):
                cid = f"{slug}-{sp.get('name','').lower().replace(' ','-')}-claim"
                if cid not in claims:
                    claims[cid] = {"id": cid, "ownerIds": [], "text": f"Sponsor: {sp.get('name', '')}", "source": src, "reviewed": False}

# Add the 8 key claims
key_claims = [
    {"id": "rwanda-troops-m23", "ownerIds": ["government-of-rwanda"], "text": "Rwanda has 3,000–4,000 troops fighting alongside M23 rebels in eastern Congo.", "source": {"name": "UN Group of Experts on the DR Congo", "date": "2024", "url": None}, "reviewed": False},
    {"id": "m23-coltan-levies", "ownerIds": ["government-of-rwanda"], "text": "M23 rebels profit from coltan mining in eastern Congo.", "source": {"name": "UN Group of Experts on the DR Congo", "date": "2024", "url": None}, "reviewed": False},
    {"id": "rubaya-smuggling", "ownerIds": [], "text": "Rubaya coltan mines controlled by armed groups.", "source": {"name": "Global Witness", "date": "2026-06", "url": None}, "reviewed": False},
    {"id": "rubaya-tantalum-share", "ownerIds": [], "text": "Rubaya tantalum supply chain connects to electronics.", "source": {"name": "Global Witness", "date": "2026-06", "url": None}, "reviewed": False},
    {"id": "coltan-supply-chain", "ownerIds": [], "text": "Coltan from eastern Congo ends up in phones and laptops.", "source": {"name": "Global Witness", "date": "2026-06", "url": None}, "reviewed": False},
    {"id": "saudi-executions-2024", "ownerIds": ["government-of-saudi-arabia"], "text": "Saudi Arabia carried out a record 345 executions in 2024.", "source": {"name": "Amnesty International", "date": "2025", "url": None}, "reviewed": False},
    {"id": "khashoggi-assessment", "ownerIds": ["government-of-saudi-arabia"], "text": "US intelligence assessed Saudi Crown Prince ordered Khashoggi killing.", "source": {"name": "US Office of the Director of National Intelligence", "date": "2021-02", "url": None}, "reviewed": False},
    {"id": "uae-mass-trial-2024", "ownerIds": ["government-of-dubai"], "text": "UAE mass trial of 94 human rights defenders in 2024.", "source": {"name": "Human Rights Watch", "date": "2024-07", "url": None}, "reviewed": False},
]
for kc in key_claims:
    if kc["id"] not in claims:
        claims[kc["id"]] = kc

claims_list = list(claims.values())

# Build changes.json
changes = []
for slug, t in teams.items():
    for sp in t.get("sponsors", []):
        changes.append({
            "id": f"{slug}-{sp.get('name','').lower().replace(' ','-')}-change",
            "clubId": slug,
            "kind": "being-rated",
            "text": f"Sponsor {sp.get('name', '')} being rated",
            "badge": f"+ {sp.get('name', '')}",
            "source": sp.get("sources", [None])[0] if sp.get("sources") else None,
        })

# Build dropped.json
dropped = list(dropped_seed)
# Add known dropped items
known_dropped = [
    {"id": "schalke-gazprom-2022", "clubId": "schalke-04", "orgName": "Gazprom", "sponsorId": "gazprom", "leagueId": "bundesliga", "from": "2022", "to": "2022", "reason": "Russia invaded Ukraine", "source": {"name": "Multiple sources", "date": "2022-02", "url": None}},
    {"id": "luton-puma-2025", "clubId": "luton-town", "orgName": "Puma", "sponsorId": "puma", "leagueId": "premier-league", "from": "2025", "to": "2025", "reason": "BDS campaign", "source": {"name": "Multiple sources", "date": "2025", "url": None}},
    {"id": "uefa-gazprom-2022", "clubId": None, "orgName": "Gazprom", "sponsorId": "gazprom", "leagueId": "uefa", "from": "2022", "to": "2022", "reason": "Russia invaded Ukraine", "source": {"name": "Multiple sources", "date": "2022-02", "url": None}},
    {"id": "manutd-aeroflot-2022", "clubId": "manchester-united", "orgName": "Aeroflot", "sponsorId": "aeroflot", "leagueId": "premier-league", "from": "2022", "to": "2022", "reason": "Russia invaded Ukraine", "source": {"name": "Multiple sources", "date": "2022-02", "url": None}},
    {"id": "haas-uralkali-2022", "clubId": "haas-f1", "orgName": "Uralkali", "sponsorId": "uralkali", "leagueId": "formula-1", "from": "2022", "to": "2022", "reason": "Russia invaded Ukraine", "source": {"name": "Multiple sources", "date": "2022-02", "url": None}},
    {"id": "f1-russian-gp-2022", "clubId": None, "orgName": "Formula 1", "sponsorId": "russian-gp", "leagueId": "formula-1", "from": "2022", "to": "2022", "reason": "Russia invaded Ukraine", "source": {"name": "Multiple sources", "date": "2022-02", "url": None}},
    {"id": "wwc-visit-saudi-2023", "clubId": None, "orgName": "Visit Saudi", "sponsorId": "visit-saudi", "leagueId": "fifa", "from": "2023", "to": "2023", "reason": "Human rights concerns", "source": {"name": "Multiple sources", "date": "2023", "url": None}},
    {"id": "bayern-qatar-airways-2023", "clubId": "bayern-munich", "orgName": "Qatar Airways", "sponsorId": "qatar-airways", "leagueId": "bundesliga", "from": "2023", "to": "2023", "reason": "Human rights concerns", "source": {"name": "Multiple sources", "date": "2023", "url": None}},
]
for kd in known_dropped:
    if kd["id"] not in [d["id"] for d in dropped]:
        dropped.append(kd)

# Build contacts.json
contacts = []
for slug, t in teams.items():
    contact = t.get("contact", {})
    if contact and contact.get("email") and contact.get("email") != "placeholder":
        channels = []
        if contact.get("email"):
            channels.append({"type": "email", "value": contact["email"], "label": "Club email", "source": {"name": "Club website", "url": None, "date": "2026-09-24"}})
        if contact.get("website"):
            channels.append({"type": "contact-form", "value": contact["website"], "label": "Club website", "source": {"name": "Club website", "url": contact["website"], "date": "2026-09-24"}})
        if contact.get("social", {}).get("twitter"):
            channels.append({"type": "x", "value": contact["social"]["twitter"], "label": "Official X account", "source": {"name": "Club website footer", "url": None, "date": "2026-09-24"}})
        if channels:
            contacts.append({"clubId": slug, "channels": channels, "lastChecked": "2026-09-24"})

# Write normalized files
out_dir = "/tmp/data/normalized"
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "meta.json"), "w") as f:
    json.dump(meta, f, indent=2)
with open(os.path.join(out_dir, "sports.json"), "w") as f:
    json.dump(sports, f, indent=2)
with open(os.path.join(out_dir, "leagues.json"), "w") as f:
    json.dump(leagues, f, indent=2)
with open(os.path.join(out_dir, "clubs.json"), "w") as f:
    json.dump(clubs, f, indent=2)
with open(os.path.join(out_dir, "owners.json"), "w") as f:
    json.dump(owners_list, f, indent=2)
with open(os.path.join(out_dir, "claims.json"), "w") as f:
    json.dump(claims_list, f, indent=2)
with open(os.path.join(out_dir, "sponsors.json"), "w") as f:
    json.dump(sponsors_list, f, indent=2)
with open(os.path.join(out_dir, "kits.json"), "w") as f:
    json.dump(kits, f, indent=2)
with open(os.path.join(out_dir, "deals.json"), "w") as f:
    json.dump(deals, f, indent=2)
with open(os.path.join(out_dir, "changes.json"), "w") as f:
    json.dump(changes, f, indent=2)
with open(os.path.join(out_dir, "dropped.json"), "w") as f:
    json.dump(dropped, f, indent=2)
with open(os.path.join(out_dir, "levels.json"), "w") as f:
    json.dump(levels, f, indent=2)
with open(os.path.join(out_dir, "tiers.json"), "w") as f:
    json.dump(tiers, f, indent=2)
with open(os.path.join(out_dir, "contacts.json"), "w") as f:
    json.dump(contacts, f, indent=2)

print(f"Generated normalized files:")
print(f"  clubs: {len(clubs)}")
print(f"  sponsors: {len(sponsors_list)}")
print(f"  owners: {len(owners_list)}")
print(f"  claims: {len(claims_list)}")
print(f"  kits: {len(kits)}")
print(f"  deals: {len(deals)}")
print(f"  changes: {len(changes)}")
print(f"  dropped: {len(dropped)}")
print(f"  contacts: {len(contacts)}")
