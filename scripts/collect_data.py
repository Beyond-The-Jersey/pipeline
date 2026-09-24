#!/usr/bin/env python3
"""Collect team data from Wikipedia (static HTML, no JS rendering needed)."""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

OUTPUT_DIR = Path("raw_data")
OUTPUT_DIR.mkdir(exist_ok=True)

WIKIPEDIA_SOURCES = {
    "soccer": {
        "premier_league": "https://en.wikipedia.org/wiki/2025%E2%80%9326_Premier_League",
    },
    "basketball": {
        "nba": "https://en.wikipedia.org/wiki/2025%E2%80%9326_NBA_season",
    },
}

def extract_teams_wiki(content: str, sport: str) -> list:
    """Parse Wikipedia page for team names."""
    teams = []

    if sport == "soccer":
        # Premier League: look for [[Team Name (football)|Short Name]] patterns
        pattern = r'\[\[([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+\(football\)\|([^\]]+)\]\]'
        for match in re.finditer(pattern, content):
            full_name = match.group(1).strip()
            short_name = match.group(2).strip()
            if full_name and len(full_name) > 2:
                teams.append({"name": full_name, "short_name": short_name})
    elif sport == "basketball":
        # NBA: look for [[Team Name]] patterns in division tables
        pattern = r'\[\[([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\]\]'
        skip_words = {"Wikipedia", "Portal", "Sports", "Basketball", "See", "Also", "Edit"}
        for match in re.finditer(pattern, content):
            name = match.group(1).strip()
            if name not in skip_words and len(name) > 2:
                teams.append({"name": name})

    return teams

def collect_team_data(sport: str, league: str, url: str) -> dict:
    """Collect team data from Wikipedia."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; BehindTheJersey/0.1)"}
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8", errors="replace")
    except URLError as e:
        print(f"ERROR: Failed to fetch {url}: {e}", file=sys.stderr)
        return {"sport": sport, "league": league, "url": url, "teams": [], "error": str(e)}

    teams = extract_teams_wiki(content, sport)

    return {
        "sport": sport,
        "league": league,
        "url": url,
        "teams": teams,
        "collected_at": datetime.now(timezone.utc).isoformat(),
    }

def main():
    all_data = {}
    for sport, leagues in WIKIPEDIA_SOURCES.items():
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