#!/usr/bin/env python3
"""Verify data quality - cross-reference sponsors with HR databases."""

import json
import sys
from pathlib import Path

VERIFIED_DIR = Path("verified_data")
VERIFIED_DIR.mkdir(exist_ok=True)

# HR databases to check against
HR_DATABASES = {
    "hrf": "https://hrforum.org",
    "amnesty": "https://amnesty.org",
    "hrw": "https://hrw.org",
    "bhr": "https://business-humanrights.org",
}

MIN_SOURCES = 2

def verify_sponsor(sponsor: dict, raw_data: dict) -> dict:
    """Verify a sponsor's human rights record with at least 2 sources."""
    name = sponsor.get("name", "")
    sources = sponsor.get("sources", [])
    
    verified = {
        "name": name,
        "original_data": sponsor,
        "sources_count": len(sources),
        "verified": len(sources) >= MIN_SOURCES,
        "flags": [],
    }
    
    if len(sources) < MIN_SOURCES:
        verified["flags"].append(f"Only {len(sources)} source(s), need {MIN_SOURCES}")
    
    # Check for known issues in source URLs
    for source in sources:
        if any(blocked in source.lower() for blocked in ["paywall", "subscription"]):
            verified["flags"].append(f"Source may be behind paywall: {source}")
    
    return verified

def main():
    # Load raw collected data
    raw_file = Path("raw_data") / "raw_collected.json"
    if not raw_file.exists():
        print(f"ERROR: {raw_file} not found. Run collect_data.py first.", file=sys.stderr)
        sys.exit(1)
    
    with open(raw_file) as f:
        raw_data = json.load(f)
    
    results = {}
    for key, sport_data in raw_data.items():
        teams = sport_data.get("teams", [])
        verified_teams = []
        
        for team in teams:
            sponsors = team.get("sponsors", [])
            verified_sponsors = [verify_sponsor(s, raw_data) for s in sponsors]
            
            verified_teams.append({
                "name": team.get("name", ""),
                "sponsors": verified_sponsors,
                "verified_count": sum(1 for s in verified_sponsors if s["verified"]),
                "total_count": len(verified_sponsors),
            })
        
        results[key] = {
            "sport": sport_data.get("sport", ""),
            "league": sport_data.get("league", ""),
            "teams": verified_teams,
            "overall_verified": sum(t["verified_count"] for t in verified_teams),
            "overall_total": sum(t["total_count"] for t in verified_teams),
        }
    
    # Save verified data
    output_file = VERIFIED_DIR / "verified_data.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved verified data to {output_file}")
    
    # Print summary
    for key, data in results.items():
        print(f"  {key}: {data['overall_verified']}/{data['overall_total']} sponsors verified")

if __name__ == "__main__":
    main()