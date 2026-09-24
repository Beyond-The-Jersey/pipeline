#!/usr/bin/env python3
"""Collect sponsor/funder data from Wikipedia for all teams."""

import json
import re
import sys
import urllib.parse
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

OUTPUT_DIR = Path("/tmp/data/data")
RAW_DIR = Path("/tmp/pipeline/raw_data")
RAW_DIR.mkdir(exist_ok=True)

# Comprehensive Wikipedia page name mapping
# Format: slug -> Wikipedia page name
TEAM_WIKIPEDIA = {
    # Premier League
    "arsenal": "Arsenal_F.C.",
    "aston-villa": "Aston_Villa_F.C.",
    "bournemouth": "AFC_Bournemouth",
    "brentford": "Brentford_F.C.",
    "brighton-hove-albion": "Brighton_%26_Hove_Albion",
    "chelsea": "Chelsea_F.C.",
    "coventry-city": "Coventry_City_F.C.",
    "crystal-palace": "Crystal_Palace_F.C.",
    "everton": "Everton_F.C.",
    "fulham": "Fulham_F.C.",
    "hull-city": "Hull_City_A.F.C.",
    "ipswich-town": "Ipswich_Town_F.C.",
    "leeds-united": "Leeds_United_F.C.",
    "liverpool": "Liverpool_F.C.",
    "manchester-city": "Manchester_City_F.C.",
    "manchester-united": "Manchester_United_F.C.",
    "newcastle-united": "Newcastle_United_F.C.",
    "nottingham-forest": "Nottingham_Forest_F.C.",
    "sunderland": "Sunderland_A.F.C.",
    "tottenham-hotspur": "Tottenham_Hotspur_F.C.",
    # NBA
    "atlanta-hawks": "Atlanta_Hawks",
    "boston-celtics": "Boston_Celtics",
    "brooklyn-nets": "Brooklyn_Nets",
    "charlotte-hornets": "Charlotte_Hornets",
    "chicago-bulls": "Chicago_Bulls",
    "cleveland-cavaliers": "Cleveland_Cavaliers",
    "dallas-mavericks": "Dallas_Mavericks",
    "denver-nuggets": "Denver_Nuggets",
    "detroit-pistons": "Detroit_Pistons",
    "golden-state-warriors": "Golden_State_Warriors",
    "houston-rockets": "Houston_Rockets",
    "indiana-pacers": "Indiana_Pacers",
    "los-angeles-clippers": "Los_Angeles_Clippers",
    "los-angeles-lakers": "Los_Angeles_Lakers",
    "memphis-grizzlies": "Memphis_Grizzlies",
    "miami-heat": "Miami_Heat",
    "milwaukee-bucks": "Milwaukee_Bucks",
    "minnesota-timberwolves": "Minnesota_Timberwolves",
    "new-orleans-pelicans": "New_Orleans_Pelicans",
    "new-york-knicks": "New_York_Knicks",
    "oklahoma-city-thunder": "Oklahoma_City_Thunder",
    "orlando-magic": "Orlando_Magic",
    "philadelphia-76ers": "Philadelphia_76ers",
    "phoenix-suns": "Phoenix_Suns",
    "portland-trail-blazers": "Portland_Trail_Blazers",
    "sacramento-kings": "Sacramento_Kings",
    "san-antonio-spurs": "San_Antonio_Spurs",
    "toronto-raptors": "Toronto_Raptors",
    "utah-jazz": "Utah_Jazz",
    "washington-wizards": "Washington_Wizards",
    # NFL
    "arizona-cardinals": "Arizona_Cardinals",
    "atlanta-falcons": "Atlanta_Falcons",
    "baltimore-ravens": "Baltimore_Ravens",
    "buffalo-bills": "Buffalo_Bills",
    "carolina-panthers": "Carolina_Panthers",
    "chicago-bears": "Chicago_Bears",
    "cincinnati-bengals": "Cincinnati_Bengals",
    "cleveland-browns": "Cleveland_Browns",
    "dallas-cowboys": "Dallas_Cowboys",
    "denver-broncos": "Denver_Broncos",
    "detroit-lions": "Detroit_Lions",
    "green-bay-packers": "Green_Bay_Packers",
    "houston-texans": "Houston_Texans",
    "indianapolis-colts": "Indianapolis_Colts",
    "jacksonville-jaguars": "Jacksonville_Jaguars",
    "kansas-city-chiefs": "Kansas_City_Chiefs",
    "las-vegas-raiders": "Las_Vegas_Raiders",
    "los-angeles-chargers": "Los_Angeles_Chargers",
    "los-angeles-rams": "Los_Angeles_Rams",
    "miami-dolphins": "Miami_Dolphins",
    "minnesota-vikings": "Minnesota_Vikings",
    "new-england-patriots": "New_England_Patriots",
    "new-orleans-saints": "New_Orleans_Saints",
    "new-york-giants": "New_York_Giants",
    "new-york-jets": "New_York_Jets",
    "philadelphia-eagles": "Philadelphia_Eagles",
    "pittsburgh-steelers": "Pittsburgh_Steelers",
    "san-francisco-49ers": "San_Francisco_49ers",
    "seattle-seahawks": "Seattle_Seahawks",
    "tampa-bay-buccaneers": "Tampa_Bay_Buccaneers",
    "tennessee-titans": "Tennessee_Titans",
    "washington-commanders": "Washington_Commanders",
    # La Liga
    "athletic-club": "Athletic_Bilbao",
    "atletico-de-madrid": "Atl%C3%A9tico_de_Madrid",
    "ca-osasuna": "CA_Osasuna",
    "celta": "RC_Celta_de_Vigo",
    "deportivo-alaves": "Deportivo_Alav%C3%A9s",
    "elche-cf": "Elche_CF",
    "fc-barcelona": "FC_Barcelona",
    "getafe-cf": "Getafe_CF",
    "levante-ud": "Levante_UD",
    "málaga-cf": "M%C3%A1laga_CF",
    "r-racing-club": "Racing_de_Santander",
    "rayo-vallecano": "Rayo_Vallecano",
    "rc-deportivo": "Deportivo_de_La_Coru%C3%B1a",
    "rcd-espanyol-de-barcelona": "RCD_Espanyol",
    "real-betis": "Real_Betis",
    "real-madrid": "Real_Madrid_CF",
    "real-sociedad": "Real_Sociedad",
    "sevilla-fc": "Sevilla_FC",
    "valencia-cf": "Valencia_CF",
    "villarreal-cf": "Villarreal_CF",
    # Bundesliga
    "bayern-munich": "FC_Bayern_Munich",
    "borussia-dortmund": "Borussia_Dortmund",
    "rb-leipzig": "RB_Leipzig",
    "vfb-stuttgart": "VfB_Stuttgart",
    "tsg-hoffenheim": "TSG_1899_Hoffenheim",
    "bayer-leverkusen": "Bayer_04_Leverkusen",
    "sport-club-freiburg": "SC_Freiburg",
    "eintracht-frankfurt": "Eintracht_Frankfurt",
    "fc-augsburg": "FC_Augsburg",
    "1-fsv-mainz-05": "1._FSV_Mainz_05",
    "1-fc-union-berlin": "1._FC_Union_Berlin",
    "borussia-mönchengladbach": "Borussia_Mönchengladbach",
    "hamburger-sv": "Hamburger_SV",
    "1-fc-köln": "1._FC_Köln",
    "sv-werder-bremen": "SV_Werder_Bremen",
    "fc-schalke-04": "FC_Schalke_04",
    "sv-elversberg": "SV_Elversberg",
    "sc-paderborn-07": "SC_Paderborn_07",
    # MLB
    "arizona-diamondbacks": "Arizona_Diamondbacks",
    "atlanta-braves": "Atlanta_Braves",
    "baltimore-orioles": "Baltimore_Orioles",
    "boston-red-sox": "Boston_Red_Sox",
    "chicago-cubs": "Chicago_Cubs",
    "chicago-white-sox": "Chicago_White_Sox",
    "cincinnati-reds": "Cincinnati_Reds",
    "cleveland-guardians": "Cleveland_Guardians",
    "colorado-rockies": "Colorado_Rockies",
    "detroit-tigers": "Detroit_Tigers",
    "houston-astros": "Houston_Astros",
    "kansas-city-royals": "Kansas_City_Royals",
    "los-angeles-angels": "Los_Angeles_Angels",
    "los-angeles-dodgers": "Los_Angeles_Dodgers",
    "miami-marlins": "Miami_Marlins",
    "milwaukee-brewers": "Milwaukee_Brewers",
    "minnesota-twins": "Minnesota_Twins",
    "new-york-mets": "New_York_Mets",
    "new-york-yankees": "New_York_Yankees",
    "oakland-athletics": "Oakland_Athletics",
    "philadelphia-phillies": "Philadelphia_Phillies",
    "pittsburgh-pirates": "Pittsburgh_Pirates",
    "san-diego-padres": "San_Diego_Padres",
    "san-francisco-giants": "San_Francisco_Giants",
    "seattle-mariners": "Seattle_Mariners",
    "st-louis-cardinals": "St._Louis_Cardinals",
    "tampa-bay-rays": "Tampa_Bay_Rays",
    "texas-rangers": "Texas_Rangers",
    "toronto-blue-jays": "Toronto_Blue_Jays",
    "washington-nationals": "Washington_Nationals",
}


def fetch_wikipedia_data(wiki_page: str) -> dict:
    """Fetch owner/sponsor data from Wikipedia for a team."""
    # URL-encode the page name
    encoded_page = urllib.parse.quote(wiki_page)
    url = f"https://en.wikipedia.org/wiki/{encoded_page}"

    try:
        req = Request(url, headers={"User-Agent": "BehindTheJersey/0.1"})
        with urlopen(req, timeout=20) as resp:
            content = resp.read().decode("utf-8", errors="replace")
    except URLError as e:
        return {"error": str(e), "wiki_url": url}

    owner = None
    sponsors = []

    # Extract owner - look for "Owner" or "Owner(s)" field in infobox
    owner_patterns = [
        r'\| Owner\(s\) = (.+?)(?:\n|\||\})',
        r'\| Owner = (.+?)(?:\n|\||\})',
    ]
    for pattern in owner_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            owner_text = match.group(1).strip()
            # Clean up wiki markup
            owner = re.sub(r'\[\[([^\]]+)\|([^\]]+)\]\]', r'\2', owner_text)
            owner = re.sub(r'\[\[([^\]]+)\]\]', r'\1', owner)
            owner = re.sub(r'<[^>]+>', '', owner).strip()
            # Remove citation markers
            owner = re.sub(r'\[\d+\]', '', owner).strip()
            break

    # Extract kit manufacturer / shirt sponsor
    sponsor_patterns = [
        r'\| Kit manufacturer = (.+?)(?:\n|\||\})',
        r'\| Shirt sponsor = (.+?)(?:\n\|\||}\n)',
        r'\| Sponsor = (.+?)(?:\n|\||\})',
    ]
    for pattern in sponsor_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            sponsor_text = match.group(1).strip()
            sponsor = re.sub(r'\[\[([^\]]+)\|([^\]]+)\]\]', r'\2', sponsor_text)
            sponsor = re.sub(r'\[\[([^\]]+)\]\]', r'\1', sponsor)
            sponsor = re.sub(r'<[^>]+>', '', sponsor).strip()
            sponsor = re.sub(r'\[\d+\]', '', sponsor).strip()
            if sponsor and sponsor.lower() not in ('none', 'tbd', 'none (tbd)', '—', '–'):
                sponsors.append({
                    "name": sponsor,
                    "type": "company",
                    "category": "sponsor",
                    "rating": "D",
                    "rating_desc": "Unverified — needs review",
                    "flags": [],
                    "deal_value": None,
                    "sources": [url],
                    "verified": False,
                    "last_updated": "2026-09-24",
                })

    return {
        "owner": owner,
        "sponsors": sponsors,
        "wiki_url": url,
        "error": None,
    }


def main():
    # Load index.json to get all teams
    with open(OUTPUT_DIR / "index.json") as f:
        index = json.load(f)

    teams = index.get("teams", [])
    print(f"Processing {len(teams)} teams...")

    updated = 0
    errors = 0
    no_wiki = 0

    for team_info in teams:
        team_name = team_info.get("team", "")
        file_name = team_info.get("file", "")
        slug = file_name.replace(".json", "")

        wiki_page = TEAM_WIKIPEDIA.get(slug)
        if not wiki_page:
            print(f"  SKIP {team_name} — no Wikipedia mapping for '{slug}'")
            no_wiki += 1
            continue

        # Load the team file
        team_path = OUTPUT_DIR / file_name
        if not team_path.exists():
            print(f"  SKIP {team_name} — file not found: {file_name}")
            continue

        with open(team_path) as f:
            team_data = json.load(f)

        # Fetch sponsor data from Wikipedia
        print(f"  FETCH {team_name} (wiki: {wiki_page})...")
        result = fetch_wikipedia_data(wiki_page)

        if result.get("error"):
            print(f"    ERROR: {result['error']}")
            errors += 1
            continue

        # Update team data with sponsor info
        changed = False
        if result.get("owner"):
            team_data["owner"] = result["owner"]
            changed = True
        if result.get("sponsors"):
            existing = team_data.get("sponsors", [])
            if not existing:
                team_data["sponsors"] = result["sponsors"]
                changed = True

        if changed:
            with open(team_path, "w") as f:
                json.dump(team_data, f, indent=2)

        updated += 1
        if updated % 20 == 0:
            print(f"  Progress: {updated}/{len(teams)} updated, {errors} errors")

    print(f"\nDone: {updated} teams updated, {errors} errors, {no_wiki} no wiki mapping")

    # Save a log of what was done
    log_path = RAW_DIR / "sponsor_collection_log.json"
    with open(log_path, "w") as f:
        json.dump({"updated": updated, "errors": errors, "no_wiki": no_wiki, "total": len(teams)}, f, indent=2)
    print(f"Log saved to {log_path}")


if __name__ == "__main__":
    main()