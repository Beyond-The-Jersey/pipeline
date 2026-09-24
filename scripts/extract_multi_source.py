#!/usr/bin/env python3
"""Extract sponsor/owner data from Wikidata and league sites."""

import json
import re
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import quote_plus

OUTPUT_DIR = Path("raw_data")
OUTPUT_DIR.mkdir(exist_ok=True)

def fetch(url, headers=None):
    """Fetch URL content."""
    if headers is None:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; DataPipeline/1.0)"}
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (URLError, HTTPError) as e:
        return f"ERROR: {e}"

def wikidata_query(query):
    """Run a SPARQL query against Wikidata."""
    encoded = quote_plus(query)
    url = f"https://query.wikidata.org/sparql?format=json&query={encoded}"
    content = fetch(url)
    if content.startswith("ERROR"):
        return []
    try:
        data = json.loads(content)
        return data.get("results", {}).get("bindings", [])
    except json.JSONDecodeError:
        return []

def get_all_wikidata_owners():
    """Get all football club owners from Wikidata."""
    print("=" * 60)
    print("WIKIDATA: Extracting all club owners")
    print("=" * 60)
    
    # Query for football club owners with labels
    query = """
    SELECT ?club ?clubLabel ?owner ?ownerLabel ?startTime ?endTime WHERE {
      ?club wdt:P31 wd:Q476028.
      ?club wdt:P127 ?owner.
      OPTIONAL { ?club p:P127 ?statement.
                 ?statement pq:P580 ?startTime.
                 ?statement pq:P582 ?endTime. }
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY ?clubLabel
    """
    
    results = wikidata_query(query)
    print(f"Found {len(results)} owner relationships")
    
    owners_by_club = {}
    for r in results:
        club = r.get("clubLabel", {}).get("value", "unknown")
        owner = r.get("ownerLabel", {}).get("value", "unknown")
        start = r.get("startTime", {}).get("value", "")
        end = r.get("endTime", {}).get("value", "")
        
        if club not in owners_by_club:
            owners_by_club[club] = []
        
        owners_by_club[club].append({
            "owner": owner,
            "start": start,
            "end": end,
        })
    
    # Print summary
    for club, owners in sorted(owners_by_club.items()):
        owner_names = [o["owner"] for o in owners]
        print(f"  {club}: {', '.join(owner_names)}")
    
    return owners_by_club

def get_wikidata_sponsors():
    """Get sponsor data from Wikidata."""
    print("\n" + "=" * 60)
    print("WIKIDATA: Extracting sponsor data")
    print("=" * 60)
    
    # Query for shirt sponsors
    query = """
    SELECT ?club ?clubLabel ?sponsor ?sponsorLabel WHERE {
      ?club wdt:P31 wd:Q476028.
      ?club wdt:P3342 ?sponsor.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    LIMIT 100
    """
    
    results = wikidata_query(query)
    print(f"Found {len(results)} shirt sponsor relationships")
    
    sponsors_by_club = {}
    for r in results:
        club = r.get("clubLabel", {}).get("value", "unknown")
        sponsor = r.get("sponsorLabel", {}).get("value", "unknown")
        
        if club not in sponsors_by_club:
            sponsors_by_club[club] = []
        
        sponsors_by_club[club].append(sponsor)
    
    for club, sponsors in sorted(sponsors_by_club.items()):
        print(f"  {club}: {', '.join(sponsors)}")
    
    return sponsors_by_club

def get_wikidata_kit_manufacturers():
    """Get kit manufacturer data from Wikidata."""
    print("\n" + "=" * 60)
    print("WIKIDATA: Extracting kit manufacturer data")
    print("=" * 60)
    
    query = """
    SELECT ?club ?clubLabel ?manufacturer ?manufacturerLabel WHERE {
      ?club wdt:P31 wd:Q476028.
      ?club wdt:P2414 ?manufacturer.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    LIMIT 100
    """
    
    results = wikidata_query(query)
    print(f"Found {len(results)} kit manufacturer relationships")
    
    manufacturers_by_club = {}
    for r in results:
        club = r.get("clubLabel", {}).get("value", "unknown")
        manufacturer = r.get("manufacturerLabel", {}).get("value", "unknown")
        
        if club not in manufacturers_by_club:
            manufacturers_by_club[club] = []
        
        manufacturers_by_club[club].append(manufacturer)
    
    for club, manufacturers in sorted(manufacturers_by_club.items()):
        print(f"  {club}: {', '.join(manufacturers)}")
    
    return manufacturers_by_club

def extract_from_league_site(content, league_name):
    """Extract sponsor/owner data from league site content."""
    sponsors = []
    owners = []
    
    # Look for sponsor mentions
    sponsor_patterns = [
        r'Sponsor[s]?:\s*(.*?)(?:\n|</|<)',
        r'(?:shirt|kit)\s+sponsor[s]?:\s*(.*?)(?:\n|</|<)',
        r'Partner[s]?:\s*(.*?)(?:\n|</|<)',
        r'Title\s+sponsor[s]?:\s*(.*?)(?:\n|</|<)',
    ]
    
    for pattern in sponsor_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        for m in matches:
            sponsor = m.strip()
            if sponsor and len(sponsor) > 2 and sponsor not in sponsors:
                sponsors.append(sponsor[:100])
    
    # Look for owner mentions
    owner_patterns = [
        r'Owner[s]?:\s*(.*?)(?:\n|</|<)',
        r'Owner[s]\s+(?:is|are|was|were)\s+(.*?)(?:\n|</|<)',
        r'Owned\s+by[s]?:\s*(.*?)(?:\n|</|<)',
    ]
    
    for pattern in owner_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        for m in matches:
            owner = m.strip()
            if owner and len(owner) > 2 and owner not in owners:
                owners.append(owner[:100])
    
    return {"sponsors": sponsors, "owners": owners}

def test_league_sites():
    """Test official league sites for sponsor/owner data."""
    print("\n" + "=" * 60)
    print("LEAGUE SITES: Extracting sponsor/owner data")
    print("=" * 60)
    
    test_urls = {
        "Premier League": "https://www.premierleague.com/clubs",
        "NBA": "https://www.nba.com/teams",
        "NFL": "https://www.nfl.com/teams/",
        "MLB": "https://www.mlb.com/",
    }
    
    results = {}
    for league, url in test_urls.items():
        print(f"\n{league}: {url}")
        content = fetch(url)
        
        if content.startswith("ERROR"):
            print(f"  Failed: {content}")
            results[league] = {"error": str(content)}
            continue
        
        data = extract_from_league_site(content, league)
        print(f"  Sponsors found: {len(data['sponsors'])}")
        print(f"  Owners found: {len(data['owners'])}")
        
        if data["sponsors"]:
            print(f"  Sponsor samples: {data['sponsors'][:3]}")
        if data["owners"]:
            print(f"  Owner samples: {data['owners'][:3]}")
        
        results[league] = data
    
    return results

def main():
    print("EXTRACTING SPONSOR/OWNER DATA FROM MULTIPLE SOURCES")
    print("=" * 60)
    
    # Get Wikidata data
    wikidata_owners = get_all_wikidata_owners()
    wikidata_sponsors = get_wikidata_sponsors()
    wikidata_manufacturers = get_wikidata_kit_manufacturers()
    
    # Get league site data
    league_data = test_league_sites()
    
    # Combine all data
    combined = {
        "wikidata_owners": wikidata_owners,
        "wikidata_sponsors": wikidata_sponsors,
        "wikidata_manufacturers": wikidata_manufacturers,
        "league_sites": league_data,
    }
    
    # Save to file
    output_path = OUTPUT_DIR / "multi_source_data.json"
    with open(output_path, 'w') as f:
        json.dump(combined, f, indent=2)
    print(f"\n\nResults saved to {output_path}")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Wikidata owners: {len(wikidata_owners)} clubs")
    print(f"Wikidata sponsors: {len(wikidata_sponsors)} clubs")
    print(f"Wikidata manufacturers: {len(wikidata_manufacturers)} clubs")
    print(f"League sites: {len(league_data)} leagues")

if __name__ == "__main__":
    main()