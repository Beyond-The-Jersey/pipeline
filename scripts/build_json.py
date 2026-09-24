#!/usr/bin/env python3
"""Build final JSON files for the website from verified data."""

import json
import sys
from pathlib import Path
from datetime import datetime

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

RATING_SCALE = {
    "A+": "Strong human rights supporter",
    "A": "Positive record",
    "B": "Minor concerns",
    "C": "Mixed / some concerns",
    "D": "Significant concerns",
    "F": "Severe violations / complicity",
}

def assign_rating(sponsor: dict) -> str:
    """Assign A+ to F rating based on verified data."""
    flags = sponsor.get("flags", [])
    verified = sponsor.get("verified", False)
    
    if not verified:
        return "D"  # Default to D if not verified
    
    # Check for severe violation flags
    severe_keywords = ["severe", "complicity", "violations", "abuse", "forced labor"]
    for flag in flags:
        if any(kw in flag.lower() for kw in severe_keywords):
            return "F"
    
    # Check for negative flags
    negative_keywords = ["controversy", "concern", "issue", "violation"]
    for flag in flags:
        if any(kw in flag.lower() for kw in negative_keywords):
            return "C"
    
    return "A"  # Default positive if no flags

def build_team_json(team_data: dict) -> dict:
    """Build a team JSON file from verified data."""
    sponsors = []
    for sponsor in team_data.get("sponsors", []):
        original = sponsor.get("original_data", {})
        rating = assign_rating(sponsor)
        
        sponsors.append({
            "name": original.get("name", sponsor.get("name", "")),
            "type": original.get("type", "company"),
            "category": original.get("category", "unknown"),
            "rating": rating,
            "rating_desc": RATING_SCALE.get(rating, ""),
            "flags": sponsor.get("flags", []),
            "deal_value": original.get("deal_value"),
            "sources": original.get("sources", []),
            "verified": sponsor.get("verified", False),
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
        })
    
    return {
        "team": team_data.get("name", ""),
        "sport": team_data.get("sport", ""),
        "league": team_data.get("league", ""),
        "country": team_data.get("country", ""),
        "sponsors": sponsors,
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "data_version": "0.1",
    }

def build_index_json(all_data: dict) -> dict:
    """Build the index.json file."""
    teams = []
    total_sponsors = 0
    verified_count = 0
    
    for key, sport_data in all_data.items():
        for team in sport_data.get("teams", []):
            teams.append({
                "name": team.get("name", ""),
                "sport": sport_data.get("sport", ""),
                "league": sport_data.get("league", ""),
                "file": f"{team.get('name', '').lower().replace(' ', '_')}.json",
            })
            total_sponsors += len(team.get("sponsors", []))
            verified_count += team.get("verified_count", 0)
    
    return {
        "version": "0.1",
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "teams": teams,
        "stats": {
            "total_teams": len(teams),
            "total_sponsors": total_sponsors,
            "verified_percentage": round(verified_count / total_sponsors * 100, 1) if total_sponsors > 0 else 0,
        },
    }

def main():
    # Load verified data
    verified_file = Path("verified_data") / "verified_data.json"
    if not verified_file.exists():
        print(f"ERROR: {verified_file} not found. Run verify_quality.py first.", file=sys.stderr)
        sys.exit(1)
    
    with open(verified_file) as f:
        verified_data = json.load(f)
    
    # Build individual team JSON files
    for key, sport_data in verified_data.items():
        for team in sport_data.get("teams", []):
            team_json = build_team_json(team)
            filename = team.get("name", "").lower().replace(" ", "_") + ".json"
            output_file = DATA_DIR / filename
            
            with open(output_file, "w") as f:
                json.dump(team_json, f, indent=2)
            print(f"Created {output_file}")
    
    # Build index.json
    index_json = build_index_json(verified_data)
    index_file = DATA_DIR / "index.json"
    with open(index_file, "w") as f:
        json.dump(index_json, f, indent=2)
    print(f"Created {index_file}")
    
    # Print summary
    print(f"\nSummary:")
    print(f"  Teams: {index_json['stats']['total_teams']}")
    print(f"  Sponsors: {index_json['stats']['total_sponsors']}")
    print(f"  Verified: {index_json['stats']['verified_percentage']}%")

if __name__ == "__main__":
    main()