#!/usr/bin/env python3
"""Collect team and sponsor data from sport governing body websites."""

import json
import sys
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError

OUTPUT_DIR = Path("raw_data")
OUTPUT_DIR.mkdir(exist_ok=True)

# Sport governing body URLs to scrape
SPORT_SOURCES = {
    "soccer": {
        "premier_league": "https://www.premierleague.com/clubs",
        "la_liga": "https://www.laliga.com/en-GB/clubs",
        "serie_a": "https://www.legaseriea.it/en/clubs",
        "bundesliga": "https://www.bundesliga.com/en/bundesliga/teams",
        "ligue_1": "https://www.ligue1.com/clubs",
    },
    "basketball": {
        "nba": "https://www.nba.com/teams",
    },
    "american_football": {
        "nfl": "https://www.nfl.com/teams/",
    },
}

def collect_team_sponsors(sport: str, league: str, url: str) -> dict:
    """Scrape team and sponsor data from a sport governing body site."""
    try:
        with urlopen(url, timeout=30) as resp:
            content = resp.read().decode("utf-8", errors="replace")
    except URLError as e:
        print(f"ERROR: Failed to fetch {url}: {e}", file=sys.stderr)
        return {"sport": sport, "league": league, "url": url, "teams": [], "error": str(e)}

    # Parse team names and sponsors from content
    # This is a skeleton - actual parsing depends on site structure
    teams = []
    for line in content.split("\n"):
        line = line.strip()
        if not line:
            continue
        # Simple heuristic: look for team-like patterns
        if any(kw in line.lower() for kw in ["fc ", "united", "city", "athletic", "club"]):
            teams.append({"name": line, "sponsors": []})

    return {
        "sport": sport,
        "league": league,
        "url": url,
        "teams": teams,
        "collected_at": "__TIMESTAMP__",
    }

def main():
    all_data = {}
    for sport, leagues in SPORT_SOURCES.items():
        for league, url in leagues.items():
            print(f"Collecting {sport}/{league} from {url}...")
            data = collect_team_sponsors(sport, league, url)
            all_data[f"{sport}_{league}"] = data

    # Save raw data
    output_file = OUTPUT_DIR / "raw_collected.json"
    with open(output_file, "w") as f:
        json.dump(all_data, f, indent=2)
    print(f"Saved raw data to {output_file}")

if __name__ == "__main__":
    main()