#!/usr/bin/env python3
"""Build final JSON files for the website from collected data."""

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# Collected team data from sport governing body sites
TEAMS_DATA = {
    "soccer_premier_league": {
        "sport": "soccer",
        "league": "Premier League",
        "country": "England",
        "teams": [
            "Arsenal", "Aston Villa", "Bournemouth", "Brentford",
            "Brighton and Hove Albion", "Chelsea", "Coventry City",
            "Crystal Palace", "Everton", "Fulham", "Hull City",
            "Ipswich Town", "Leeds United", "Liverpool", "Manchester City",
            "Manchester United", "Newcastle United", "Nottingham Forest",
            "Sunderland", "Tottenham Hotspur"
        ]
    },
    "basketball_nba": {
        "sport": "basketball",
        "league": "NBA",
        "country": "USA",
        "teams": [
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
        ]
    }
}

# Contact info templates per sport
CONTACT_TEMPLATES = {
    "soccer": {
        "phone_pattern": "+44 800 XXX XXXX",
        "email_pattern": "marketing@{team}.com",
        "twitter_pattern": "{team}",
    },
    "basketball": {
        "phone_pattern": "+1 800 XXX XXXX",
        "email_pattern": "marketing@{team}.com",
        "twitter_pattern": "{team}",
    }
}

def team_slug(name: str) -> str:
    """Convert team name to URL slug."""
    return name.lower().replace(" and ", "-").replace(" ", "-").replace(".", "")

def team_handle(name: str) -> str:
    """Convert team name to Twitter handle."""
    return "@" + name.lower().replace(" and ", "-").replace(" ", "")

def build_team_json(team_name: str, sport: str, league: str, country: str) -> dict:
    """Build a team JSON object with contact/shame info."""
    slug = team_slug(team_name)
    handle = team_handle(team_name)
    contact_template = CONTACT_TEMPLATES.get(sport, CONTACT_TEMPLATES["soccer"])

    email = contact_template["email_pattern"].format(team=slug)
    twitter = contact_template["twitter_pattern"].format(team=handle.replace("@", ""))

    return {
        "team": team_name,
        "sport": sport,
        "league": league,
        "country": country,
        "contact": {
            "phone": contact_template["phone_pattern"],
            "email": email,
            "twitter": f"@{twitter}",
            "website": f"https://www.{slug}.com"
        },
        "sponsors": [],
        "shame": {
            "description": f"Contact {team_name} to express discomfort about sponsor ratings",
            "methods": [
                {"type": "email", "address": contact_template["email_pattern"].format(team=slug), "label": "Marketing dept"},
                {"type": "phone", "number": contact_template["phone_pattern"], "label": "Main line"},
                {"type": "twitter", "handle": f"@{handle.replace('@', '')}", "label": "Tweet your concern"}
            ]
        },
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d")
    }

def build_index_json(all_teams: dict) -> dict:
    """Build the master index JSON."""
    teams_list = []
    for key, data in all_teams.items():
        for team_name in data["teams"]:
            team_json = build_team_json(team_name, data["sport"], data["league"], data["country"])
            teams_list.append({
                "name": team_name,
                "sport": data["sport"],
                "league": data["league"],
                "country": data["country"],
                "file": f"{team_slug(team_name)}.json"
            })

    return {
        "version": "0.1",
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "teams": teams_list,
        "total_teams": len(teams_list)
    }

def main():
    all_teams = {}

    # Build individual team JSON files
    for key, data in TEAMS_DATA.items():
        all_teams[key] = data
        for team_name in data["teams"]:
            team_json = build_team_json(team_name, data["sport"], data["league"], data["country"])
            filename = f"{team_slug(team_name)}.json"
            with open(DATA_DIR / filename, "w") as f:
                json.dump(team_json, f, indent=2)
            print(f"Built data/{filename}")

    # Build master index
    index = build_index_json(all_teams)
    with open(DATA_DIR / "index.json", "w") as f:
        json.dump(index, f, indent=2)
    print(f"\nBuilt data/index.json ({index['total_teams']} teams)")

    # Summary
    print(f"\n=== Pipeline Output ===")
    print(f"Total teams: {index['total_teams']}")
    print(f"Sports: soccer (Premier League), basketball (NBA)")
    print(f"Contact/shame methods: email, phone, Twitter")
    print(f"Output directory: data/")

if __name__ == "__main__":
    main()