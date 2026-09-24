#!/usr/bin/env python3
"""Scrutinize Wikidata owner data and fix incorrect matches."""

import json
import re
from pathlib import Path

DATA_DIR = Path("/tmp/data/data")

# Known correct owners for cross-checking
KNOWN_OWNERS = {
    "golden-state-warriors": "Joe Lacob & Peter Guber",
    "new-york-jets": "Woody & Christopher Johnson",
    "portland-trail-blazers": "Jody Allen",
    "sport-club-freiburg": "Dietmar Hopp",  # Actually this might be wrong too
    "sacramento-kings": "Vivek Ranadivé",
    "detroit-tigers": "Christopher Ilitch",
    "miami-heat": "Micky Arison",
    "miami-marlins": "Bruce Sherman & Derek Jeter",
    "bournemouth": "Maxim Demin",  # Was previously unknown, Wikidata says Maxim Demin
    "rc-deportivo": "Tino Saqués",  # Deportivo La Coruña president/owner
}

# Teams where Wikidata owner is clearly wrong and should be removed
INCORRECT_OWNERS = {
    "golden-state-warriors": ["Abia State"],  # Wrong - Abia State is Nigerian
    "new-york-jets": ["Football Australia"],  # Wrong - Football Australia is Australian
    "portland-trail-blazers": ["Muang Thai Life Assurance"],  # Wrong - Thai insurer
    "sport-club-freiburg": ["Muang Thai Life Assurance"],  # Wrong - same Thai insurer
    "sacramento-kings": ["Bashundhara Group"],  # Wrong - Bangladeshi conglomerate
    "detroit-tigers": ["Dodsal Group"],  # Wrong - not related to Tigers
    "miami-heat": ["Riccardo Silva"],  # Wrong - Silva is AC Milan, not Heat
    "miami-marlins": ["Riccardo Silva"],  # Wrong - same
    "boston-red-sox": ["Benemérita Universidad Autónoma de Puebla"],  # Wrong - Mexican university
    "los-angeles-angels": ["Hyundai Steel"],  # Wrong - Korean company
}

def fix_incorrect_owners():
    """Fix incorrect Wikidata owner matches."""
    print("FIXING INCORRECT WIKIDATA OWNER MATCHES")
    print("=" * 60)
    
    fixed_count = 0
    
    for filename, incorrect_owners in INCORRECT_OWNERS.items():
        filepath = DATA_DIR / filename
        if not filepath.exists():
            print(f"  {filename}: file not found, skipping")
            continue
        
        with open(filepath) as f:
            data = json.load(f)
        
        current_owner = data.get("owner")
        
        # Check if current owner is in the incorrect list
        if current_owner in incorrect_owners:
            # Remove incorrect owner
            del data["owner"]
            data["last_updated"] = "2026-09-24T20:00:00+00:00"
            
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"  {filename}: REMOVED incorrect owner '{current_owner}'")
            fixed_count += 1
        else:
            print(f"  {filename}: no fix needed (owner={current_owner})")
    
    print(f"\nFixed {fixed_count} incorrect owner matches")
    return fixed_count

def clean_wiki_markup():
    """Clean wiki markup from owner data."""
    print("\n" + "=" * 60)
    print("CLEANING WIKI MARKUP FROM OWNER DATA")
    print("=" * 60)
    
    cleaned_count = 0
    
    for filepath in sorted(DATA_DIR.glob("*.json")):
        if filepath.name in ("index.json", "verified_data.json"):
            continue
        
        with open(filepath) as f:
            data = json.load(f)
        
        owner = data.get("owner")
        if owner:
            # Clean wiki markup
            original = owner
            # Remove reference tags like [a], [b], etc.
            owner = re.sub(r'\[\w+\]', '', owner).strip()
            # Clean up multiple spaces
            owner = re.sub(r'\s+', ' ', owner).strip()
            # Remove trailing punctuation that might be wiki markup
            owner = owner.rstrip('.,;')
            
            if owner != original:
                data["owner"] = owner
                data["last_updated"] = "2026-09-24T20:00:00+00:00"
                
                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=2)
                
                print(f"  {filepath.stem}: '{original}' → '{owner}'")
                cleaned_count += 1
    
    print(f"\nCleaned {cleaned_count} owner entries")
    return cleaned_count

def main():
    import re
    
    print("SCRUTINIZING WIKIDATA OWNER DATA")
    print("=" * 60)
    
    # Fix incorrect owners
    fixed = fix_incorrect_owners()
    
    # Clean wiki markup
    cleaned = clean_wiki_markup()
    
    # Final count
    print("\n" + "=" * 60)
    print("FINAL COUNT")
    print("=" * 60)
    
    teams_with_owners = 0
    for f in sorted(DATA_DIR.glob("*.json")):
        if f.name in ("index.json", "verified_data.json"):
            continue
        with open(f) as fh:
            data = json.load(fh)
        if data.get("owner"):
            teams_with_owners += 1
    
    print(f"Teams with owner data: {teams_with_owners}")

if __name__ == "__main__":
    main()