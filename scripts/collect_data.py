#!/usr/bin/env python3
"""Collect team data from official sport governing body websites + Wikipedia sponsor data."""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

OUTPUT_DIR = Path("raw_data")
OUTPUT_DIR.mkdir(exist_ok=True)

# Official sport governing body URLs
OFFICIAL_SOURCES = {
    "soccer": {
        "premier_league": "https://www.premierleague.com/clubs",
        "laliga_easports": "https://www.laliga.com/en-GB/laliga-easports/clubs",
        "bundesliga": "https://www.bundesliga.com/en/bundesliga/clubs",
    },
    "basketball": {
        "nba": "https://www.nba.com/teams",
    },
    "american_football": {
        "nfl": "https://www.nfl.com/teams/",
    },
    "baseball": {
        "mlb": "https://statsapi.mlb.com/api/v1/teams?sportId=1",
    },
}

# Wikipedia page names for each team slug
TEAM_WIKIPEDIA = {
    # Premier League
    "arsenal": "Arsenal_F.C.",
    "aston-villa": "Aston_Villa_F.C.",
    "bournemouth": "AFC_Bournemouth",
    "brentford": "Brentford_F.C.",
    "chelsea": "Chelsea_F.C.",
    "everton": "Everton_F.C.",
    "liverpool": "Liverpool_F.C.",
    "manchester-city": "Manchester_City_F.C.",
    "manchester-united": "Manchester_United_F.C.",
    "newcastle-united": "Newcastle_United_F.C.",
    "nottingham-forest": "Nottingham_Forest_F.C.",
    "sunderland": "Sunderland_A.F.C.",
    "tottenham-hotspur": "Tottenham_Hotspur_F.C.",
    # La Liga
    "athletic-club": "Athletic_Bilbao",
    "atletico-de-madrid": "Atlético_Madrid",
    "ca-osasuna": "CA_Osasuna",
    "celta": "RC_Celta_de_Vigo",
    "elche-cf": "Elche_CF",
    "fc-barcelona": "FC_Barcelona",
    "getafe-cf": "Getafe_CF",
    "levante-ud": "Levante_UD",
    "málaga-cf": "Málaga_CF",
    "r-racing-club": "Racing_de_Santander",
    "rayo-vallecano": "Rayo_Vallecano",
    "rc-deportivo": "Deportivo_de_La_Coruña",
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
    "deportivo-alaves": "Deportivo_Alavés",
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


def extract_teams_pl(content: str) -> list:
    teams = []
    pattern = r'!\[([^\]]+)\]\([^)]+\)\s*\n+\[([^\]]+)\]\(https://www\.premierleague\.com/en/clubs/\d+/[^\)]+\)'
    for match in re.finditer(pattern, content):
        name = match.group(1).strip()
        if name and len(name) > 2:
            teams.append({"name": name, "sponsors": [], "website": ""})
    seen = set()
    unique = []
    for t in teams:
        if t["name"] not in seen:
            seen.add(t["name"])
            unique.append(t)
    return unique


def extract_teams_nba(content: str) -> list:
    teams = []
    pattern = r'!\[([^\]]*)\]\([^)]+\)\s*\n+\[([^\]]+)\]\(https://www\.nba\.com/[^\)]+\)'
    for match in re.finditer(pattern, content):
        name = match.group(2).strip()
        if name and len(name) > 2:
            teams.append({"name": name, "sponsors": [], "website": ""})
    return teams


def extract_teams_nfl(content: str) -> list:
    teams = []
    pattern = r'!\[([^\]]*)\]\([^)]+\)\s*\n+\n+\*\*([^\*]+)\*\*'
    for match in re.finditer(pattern, content):
        name = match.group(2).strip()
        if name and len(name) > 2:
            teams.append({"name": name, "sponsors": [], "website": ""})
    return teams


def extract_teams_laliga(content: str) -> list:
    teams = []
    pattern = r'\*\*([^\*]+)\*\*\s*\n+\n+Foundation\s+\d{4}'
    for match in re.finditer(pattern, content):
        name = match.group(1).strip()
        if name and len(name) > 2:
            teams.append({"name": name, "sponsors": [], "website": ""})
    return teams


def extract_teams_bundesliga(content: str) -> list:
    teams = []
    pattern = r'!\[[^\]]*\]\([^)]+\)\s*\n+\n+([^\n]+)\n+'
    for match in re.finditer(pattern, content):
        name = match.group(1).strip()
        if name and len(name) > 2:
            teams.append({"name": name, "sponsors": [], "website": ""})
    return teams


def extract_teams_mlb(content: str) -> list:
    teams = []
    try:
        data = json.loads(content)
        for team in data.get("teams", []):
            name = team.get("name", "")
            if name:
                teams.append({"name": name, "sponsors": [], "website": ""})
    except json.JSONDecodeError:
        pass
    return teams


KNOWN_TEAMS = {
    "soccer_premier_league": [
        "Arsenal", "Aston Villa", "Bournemouth", "Brentford",
        "Brighton and Hove Albion", "Chelsea", "Coventry City",
        "Crystal Palace", "Everton", "Fulham", "Hull City",
        "Ipswich Town", "Leeds United", "Liverpool", "Manchester City",
        "Manchester United", "Newcastle United", "Nottingham Forest",
        "Sunderland", "Tottenham Hotspur"
    ],
    "soccer_laliga_easports": [
        "Athletic Club", "Atlético de Madrid", "CA Osasuna", "Celta",
        "Deportivo Alavés", "Elche CF", "FC Barcelona", "Getafe CF",
        "Levante UD", "Málaga CF", "R. Racing Club", "Rayo Vallecano",
        "RC Deportivo", "RCD Espanyol de Barcelona", "Real Betis",
        "Real Madrid", "Real Sociedad", "Sevilla FC", "Valencia CF",
        "Villarreal CF"
    ],
    "soccer_bundesliga": [
        "Bayern Munich", "Borussia Dortmund", "RB Leipzig", "VfB Stuttgart",
        "TSG Hoffenheim", "Bayer Leverkusen", "Sport-Club Freiburg",
        "Eintracht Frankfurt", "FC Augsburg", "1. FSV Mainz 05",
        "1. FC Union Berlin", "Borussia Mönchengladbach", "Hamburger SV",
        "1. FC Köln", "SV Werder Bremen", "FC Schalke 04",
        "SV Elversberg", "SC Paderborn 07"
    ],
    "basketball_nba": [
        "Boston Celtics", "Brooklyn Nets", "New York Knicks",
        "Philadelphia 76ers", "Toronto Raptors", "Chicago Bulls",
        "Cleveland Cavaliers", "Detroit Pistons", "Indiana Pacers",
        "Milwaukee Bucks", "Atlanta Hawks", "Charlotte Hornets",
        "Miami Heat", "Orlando Magic", "Washington Wizards",
        "Denver Nuggets", "Minnesota Timberwolves", "Oklahoma City Thunder",
        "Portland Trail Blazers", "Utah Jazz", "Golden State Warriors",
        "LA Clippers", "Los Angeles Lakers", "Phoenix Suns",
        "Sacramento Kings", "Dallas Mavericks", "Houston Rockets",
        "Memphis Grizzlies", "New Orleans Pelicans", "San Antonio Spurs"
    ],
    "american_football_nfl": [
        "Arizona Cardinals", "Atlanta Falcons", "Carolina Panthers",
        "Chicago Bears", "Dallas Cowboys", "Detroit Lions",
        "Green Bay Packers", "Los Angeles Rams", "Minnesota Vikings",
        "New Orleans Saints", "New York Giants", "Philadelphia Eagles",
        "San Francisco 49ers", "Seattle Seahawks", "Tampa Bay Buccaneers",
        "Washington Commanders", "Baltimore Ravens", "Buffalo Bills",
        "Cincinnati Bengals", "Cleveland Browns", "Denver Broncos",
        "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars",
        "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers",
        "Miami Dolphins", "New England Patriots", "New York Jets",
        "Pittsburgh Steelers", "Tennessee Titans"
    ],
    "baseball_mlb": [
        "Arizona Diamondbacks", "Atlanta Braves", "Baltimore Orioles",
        "Boston Red Sox", "Chicago Cubs", "Chicago White Sox",
        "Cincinnati Reds", "Cleveland Guardians", "Colorado Rockies",
        "Detroit Tigers", "Houston Astros", "Kansas City Royals",
        "Los Angeles Angels", "Los Angeles Dodgers", "Miami Marlins",
        "Milwaukee Brewers", "Minnesota Twins", "New York Mets",
        "New York Yankees", "Oakland Athletics", "Philadelphia Phillies",
        "Pittsburgh Pirates", "San Diego Padres", "San Francisco Giants",
        "Seattle Mariners", "St. Louis Cardinals", "Tampa Bay Rays",
        "Texas Rangers", "Toronto Blue Jays", "Washington Nationals"
    ]
}


def fetch_wikipedia_data(wiki_page_name: str) -> dict:
    """Fetch owner and sponsor data from a Wikipedia page."""
    result = {"owner": None, "sponsors": [], "error": None}
    url = f"https://en.wikipedia.org/wiki/{wiki_page_name}"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; BehindTheJersey/0.1)"}
    
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=15) as resp:
            content = resp.read().decode("utf-8", errors="replace")
    except (URLError, HTTPError, TimeoutError) as e:
        result["error"] = str(e)
        return result
    
    # Extract owner from infobox
    for pattern in [
        r'Owner\(s\) = (.+?)(?:\n|\||\})',
        r'Owner = (.+?)(?:\n|\||\})',
        r'Owners?\s*=\s*(.+?)(?:\n|\|)',
    ]:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            owner_text = match.group(1).strip()
            owner_text = re.sub(r'\[\[([^\]]+)\|([^\]]+)\]\]', r'\2', owner_text)
            owner_text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', owner_text)
            owner_text = re.sub(r'<[^>]+>', '', owner_text).strip()
            owner_text = re.sub(r'\[\d+\]', '', owner_text).strip()
            if owner_text and owner_text.lower() not in ('none', 'tbd', '—', '–'):
                result["owner"] = owner_text
            break
    
    # Extract sponsors from infobox
    for pattern in [
        r'Kit manufacturer = (.+?)(?:\n|\||\})',
        r'Shirt sponsor = (.+?)(?:\n\|\||}\n)',
        r'Sponsor = (.+?)(?:\n|\||\})',
    ]:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            sponsor_text = match.group(1).strip()
            sponsor_text = re.sub(r'\[\[([^\]]+)\|([^\]]+)\]\]', r'\2', sponsor_text)
            sponsor_text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', sponsor_text)
            sponsor_text = re.sub(r'<[^>]+>', '', sponsor_text).strip()
            sponsor_text = re.sub(r'\[\d+\]', '', sponsor_text).strip()
            if sponsor_text and sponsor_text.lower() not in ('none', 'tbd', '—', '–'):
                result["sponsors"].append({
                    "name": sponsor_text,
                    "type": "company",
                    "category": "sponsor",
                    "rating": "D",
                    "rating_desc": "Unverified — needs review",
                    "flags": [],
                    "deal_value": None,
                    "sources": [url],
                    "verified": False,
                    "last_updated": datetime.now(timezone.utc).isoformat(),
                })
            break
    
    return result


def collect_team_data(sport: str, league: str, url: str) -> dict:
    """Collect team data from official sport governing body site."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; BehindTheJersey/0.1)"}
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8", errors="replace")
    except URLError as e:
        print(f"ERROR: Failed to fetch {url}: {e}", file=sys.stderr)
        key = f"{sport}_{league}"
        return {
            "sport": sport,
            "league": league,
            "url": url,
            "teams": [{"name": t, "sponsors": [], "website": ""} for t in KNOWN_TEAMS.get(key, [])],
            "error": str(e),
            "collected_at": datetime.now(timezone.utc).isoformat(),
        }

    teams = []
    if sport == "soccer" and league == "premier_league":
        teams = extract_teams_pl(content)
    elif sport == "soccer" and league == "laliga_easports":
        teams = extract_teams_laliga(content)
    elif sport == "soccer" and league == "bundesliga":
        teams = extract_teams_bundesliga(content)
    elif sport == "basketball" and league == "nba":
        teams = extract_teams_nba(content)
    elif sport == "american_football" and league == "nfl":
        teams = extract_teams_nfl(content)
    elif sport == "baseball" and league == "mlb":
        teams = extract_teams_mlb(content)

    if not teams:
        key = f"{sport}_{league}"
        teams = [{"name": t, "sponsors": [], "website": ""} for t in KNOWN_TEAMS.get(key, [])]
        print(f"  Note: Using known team list for {league} (JS-rendered site)")

    return {
        "sport": sport,
        "league": league,
        "url": url,
        "teams": teams,
        "collected_at": datetime.now(timezone.utc).isoformat(),
    }


def main():
    all_data = {}
    for sport, leagues in OFFICIAL_SOURCES.items():
        for league, url in leagues.items():
            print(f"Collecting {sport}/{league} from {url}...")
            data = collect_team_data(sport, league, url)
            all_data[f"{sport}_{league}"] = data
            print(f"  Found {len(data['teams'])} teams")
            for t in data["teams"][:5]:
                print(f"    - {t['name']}")

    # Save raw data
    output_file = OUTPUT_DIR / "raw_collected.json"
    with open(output_file, "w") as f:
        json.dump(all_data, f, indent=2)
    print(f"\nSaved raw data to {output_file}")

    total_teams = sum(len(d["teams"]) for d in all_data.values())
    print(f"Total teams collected: {total_teams}")


if __name__ == "__main__":
    main()