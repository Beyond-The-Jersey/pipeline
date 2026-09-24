#!/usr/bin/env python3
"""Collect team and sponsor data from sport governing body websites."""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

OUTPUT_DIR = Path("raw_data")
OUTPUT_DIR.mkdir(exist_ok=True)

SPORT_SOURCES = {
    "soccer": {
        "premier_league": "https://www.premierleague.com/clubs",
    },
    "basketball": {
        "nba": "https://www.nba.com/teams",
    },
}

def extract_teams_pl(content: str) -> list:
    """Parse Premier League clubs page."""
    teams = []
    # Pattern: ![TeamName](badge_url)\n\n[TeamName](club_url)
    pattern = r'!\[([^\]]+)\]\([^)]+\)\s*\n+\[([^\]]+)\]\(([^)]+)\)'
    for match in re.finditer(pattern, content):
        name = match.group(2).strip()
        url = match.group(3).strip()
        if name and len(name) > 2 and "clubs/" in url:
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
    """Parse NBA teams page."""
    teams = []
    # Pattern: ![TeamName Logo](badge_url)\n\n[TeamName](team_url)
    pattern = r'!\[([^\]]*)\]\([^)]+\)\s*\n+\[([^\]]+)\]\(([^)]+)\)'
    for match in re.finditer(pattern, content):
        name = match.group(2).strip()
        url = match.group(3).strip()
        if name and len(name) > 2:
            teams.append({"name": name, "sponsors": [], "website": url})
    return teams

def collect_team_sponsors(sport: str, league: str, url: str) -> dict:
    """Scrape team and sponsor data from a sport governing body site."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; BehindTheJersey/0.1)"}
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8", errors="replace")
    except URLError as e:
        print(f"ERROR: Failed to fetch {url}: {e}", file=sys.stderr)
        return {"sport": sport, "league": league, "url": url, "teams": [], "error": str(e)}

    teams = []
    if sport == "soccer" and league == "premier_league":
        teams = extract_teams_pl(content)
    elif sport == "basketball" and league == "nba":
        teams = extract_teams_nba(content)

    return {
        "sport": sport,
        "league": league,
        "url": url,
        "teams": teams,
        "collected_at": datetime.now(timezone.utc).isoformat(),
    }

def main():
    all_data = {}
    for sport, leagues in SPORT_SOURCES.items():
        for league, url in leagues.items():
            print(f"Collecting {sport}/{league} from {url}...")
            data = collect_team_sponsors(sport, league, url)
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