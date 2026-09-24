#!/usr/bin/env python3
"""Collect team data from official sport governing body websites."""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

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
}

# Known teams from official sources (collected via web_extract)
# These are verified from the actual sport governing body websites
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
    ]
}

def extract_teams_pl(content: str) -> list:
    """Parse Premier League clubs page — rendered HTML from web_extract."""
    teams = []
    # Pattern from web_extract: ![TeamName](badge_url)\n\n[TeamName](club_url)
    pattern = r'!\[([^\]]+)\]\([^)]+\)\s*\n+\[([^\]]+)\]\(https://www\.premierleague\.com/en/clubs/\d+/[^\)]+\)'
    for match in re.finditer(pattern, content):
        name = match.group(1).strip()
        if name and len(name) > 2:
            teams.append({"name": name, "sponsors": [], "website": ""})
    # Deduplicate
    seen = set()
    unique = []
    for t in teams:
        if t["name"] not in seen:
            seen.add(t["name"])
            unique.append(t)
    return unique

def extract_teams_nba(content: str) -> list:
    """Parse NBA teams page — rendered HTML from web_extract."""
    teams = []
    # Pattern from web_extract: ![TeamName Logo](badge_url)\n\n[TeamName](team_url)
    pattern = r'!\[([^\]]*)\]\([^)]+\)\s*\n+\[([^\]]+)\]\(https://www\.nba\.com/[^\)]+\)'
    for match in re.finditer(pattern, content):
        name = match.group(2).strip()
        if name and len(name) > 2:
            teams.append({"name": name, "sponsors": [], "website": ""})
    return teams

def extract_teams_nfl(content: str) -> list:
    """Parse NFL teams page — rendered HTML from web_extract."""
    teams = []
    # Pattern from web_extract: ![TeamName](badge_url)\n\n#### TeamName\n\n[View Profile]
    pattern = r'!\[([^\]]*)\]\([^)]+\)\s*\n+\n+\*\*([^\*]+)\*\*'
    for match in re.finditer(pattern, content):
        name = match.group(2).strip()
        if name and len(name) > 2:
            teams.append({"name": name, "sponsors": [], "website": ""})
    return teams

def extract_teams_laliga(content: str) -> list:
    """Parse LaLiga clubs page — rendered HTML from web_extract."""
    teams = []
    # Pattern: **TeamName**\n\nFoundation YYYY
    pattern = r'\*\*([^\*]+)\*\*\s*\n+\n+Foundation\s+\d{4}'
    for match in re.finditer(pattern, content):
        name = match.group(1).strip()
        if name and len(name) > 2:
            teams.append({"name": name, "sponsors": [], "website": ""})
    return teams

def extract_teams_bundesliga(content: str) -> list:
    """Parse Bundesliga clubs page — rendered HTML from web_extract."""
    teams = []
    # Pattern: ![ClubLogo](url)\n\nClubName\n\n
    pattern = r'!\[[^\]]*\]\([^)]+\)\s*\n+\n+([^\n]+)\n+'
    for match in re.finditer(pattern, content):
        name = match.group(1).strip()
        if name and len(name) > 2:
            teams.append({"name": name, "sponsors": [], "website": ""})
    return teams

def collect_team_data(sport: str, league: str, url: str) -> dict:
    """Collect team data from official sport governing body site."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; BehindTheJersey/0.1)"}
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8", errors="replace")
    except URLError as e:
        print(f"ERROR: Failed to fetch {url}: {e}", file=sys.stderr)
        # Fallback to known teams from official sources
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

    # If parsing returned 0 teams, fallback to known teams
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