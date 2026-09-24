#!/usr/bin/env python3
"""Save Wikidata owners and extract sponsors from additional sources."""

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
        with urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (URLError, HTTPError, TimeoutError) as e:
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

def get_wikidata_owners():
    """Get all football club owners from Wikidata."""
    print("WIKIDATA: Extracting all club owners")
    
    query = """
    SELECT ?club ?clubLabel ?owner ?ownerLabel WHERE {
      ?club wdt:P31 wd:Q476028.
      ?club wdt:P127 ?owner.
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
        
        if club not in owners_by_club:
            owners_by_club[club] = []
        
        owners_by_club[club].append(owner)
    
    return owners_by_club

def get_wikidata_sponsors():
    """Get shirt sponsor data from Wikidata."""
    print("\nWIKIDATA: Extracting shirt sponsors")
    
    query = """
    SELECT ?club ?clubLabel ?sponsor ?sponsorLabel WHERE {
      ?club wdt:P31 wd:Q476028.
      ?club wdt:P3342 ?sponsor.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
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
    
    return sponsors_by_club

def get_wikidata_kit_mfrs():
    """Get kit manufacturer data from Wikidata."""
    print("\nWIKIDATA: Extracting kit manufacturers")
    
    query = """
    SELECT ?club ?clubLabel ?manufacturer ?manufacturerLabel WHERE {
      ?club wdt:P31 wd:Q476028.
      ?club wdt:P2414 ?manufacturer.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
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
    
    return manufacturers_by_club

def normalize_club_name(name):
    """Normalize club name for matching."""
    # Remove common suffixes and normalize
    name = name.lower().strip()
    # Remove "f.c.", "fc", "afc", etc.
    name = re.sub(r'\b(f\.?c\.?|afc|sc|fc)\b', '', name)
    # Remove punctuation
    name = re.sub(r'[^\w\s]', '', name)
    # Normalize spaces
    name = re.sub(r'\s+', ' ', name).strip()
    return name

def match_teams(wikidata_data, team_mapping):
    """Match Wikidata club names to our team slugs."""
    matched = {}
    unmatched = []
    
    for club, values in wikidata_data.items():
        normalized_club = normalize_club_name(club)
        
        # Try exact match first
        if club in team_mapping:
            matched[club] = {"slug": team_mapping[club], "values": values}
            continue
        
        # Try normalized match
        found = False
        for team_name, slug in team_mapping.items():
            if normalize_club_name(team_name) == normalized_club:
                matched[club] = {"slug": slug, "values": values}
                found = True
                break
        
        if not found:
            unmatched.append(club)
    
    return matched, unmatched

def main():
    print("EXTRACTING MULTI-SOURCE SPONSOR/OWNER DATA")
    print("=" * 60)
    
    # Get Wikidata data
    owners = get_wikidata_owners()
    sponsors = get_wikidata_sponsors()
    manufacturers = get_wikidata_kit_mfrs()
    
    # Load team mapping
    mapping_path = Path("raw_data/wiki_mapping.json")
    if mapping_path.exists():
        with open(mapping_path) as f:
            team_mapping = json.load(f)
        
        # Create slug -> wiki name mapping
        slug_to_wiki = {entry["slug"]: entry["wiki"] for entry in team_mapping}
    else:
        slug_to_wiki = {}
    
    # Match owners to our teams
    print("\n" + "=" * 60)
    print("MATCHING WIKIDATA TO OUR TEAMS")
    print("=" * 60)
    
    owner_matches, owner_unmatched = match_teams(owners, slug_to_wiki)
    sponsor_matches, sponsor_unmatched = match_teams(sponsors, slug_to_wiki)
    mfr_matches, mfr_unmatched = match_teams(manufacturers, slug_to_wiki)
    
    print(f"\nOwner matches: {len(owner_matches)}/{len(owners)}")
    print(f"Sponsor matches: {len(sponsor_matches)}/{len(sponsors)}")
    print(f"Manufacturer matches: {len(mfr_matches)}/{len(manufacturers)}")
    
    # Build enriched data structure
    enriched = {}
    
    # Add owners
    for club, data in owner_matches.items():
        slug = data["slug"]
        if slug not in enriched:
            enriched[slug] = {}
        enriched[slug]["owners"] = list(set(data["values"]))
    
    # Add sponsors
    for club, data in sponsor_matches.items():
        slug = data["slug"]
        if slug not in enriched:
            enriched[slug] = {}
        enriched[slug]["sponsors"] = list(set(data["values"]))
    
    # Add manufacturers
    for club, data in mfr_matches.items():
        slug = data["slug"]
        if slug not in enriched:
            enriched[slug] = {}
        enriched[slug]["kit_manufacturers"] = list(set(data["values"]))
    
    # Save enriched data
    output_path = OUTPUT_DIR / "wikidata_enriched.json"
    with open(output_path, 'w') as f:
        json.dump(enriched, f, indent=2)
    print(f"\nSaved {len(enriched)} enriched teams to {output_path}")
    
    # Print summary of what we found
    print("\n" + "=" * 60)
    print("SAMPLE ENRICHED DATA")
    print("=" * 60)
    
    for slug, data in list(enriched.items())[:15]:
        print(f"\n{slug}:")
        if "owners" in data:
            print(f"  Owners: {data['owners']}")
        if "sponsors" in data:
            print(f"  Sponsors: {data['sponsors']}")
        if "kit_manufacturers" in data:
            print(f"  Manufacturers: {data['kit_manufacturers']}")
    
    # Save unmatched for debugging
    unmatched_path = OUTPUT_DIR / "wikidata_unmatched.json"
    with open(unmatched_path, 'w') as f:
        json.dump({
            "owner_unmatched": owner_unmatched[:20],
            "sponsor_unmatched": sponsor_unmatched[:20],
            "mfr_unmatched": mfr_unmatched[:20],
        }, f, indent=2)
    print(f"\nUnmatched clubs saved to {unmatched_path}")

if __name__ == "__main__":
    main()