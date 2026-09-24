#!/usr/bin/env python3
"""Merge Wikidata owners into team JSONs and update repos."""

import json
import re
import subprocess
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import quote_plus

DATA_DIR = Path("/tmp/data/data")
PIPELINE_DIR = Path("/tmp/pipeline")
RAW_DATA_DIR = PIPELINE_DIR / "raw_data"

# Our team slugs and their common names
TEAM_NAMES = {
    "arsenal": ["Arsenal", "Arsenal F.C.", "Arsenal FC"],
    "aston-villa": ["Aston Villa", "Aston Villa F.C.", "Aston Villa FC"],
    "bournemouth": ["Bournemouth", "AFC Bournemouth", "A.F.C. Bournemouth"],
    "brentford": ["Brentford", "Brentford F.C.", "Brentford FC"],
    "brighton-hove-albion": ["Brighton", "Brighton & Hove Albion", "Brighton and Hove Albion"],
    "chelsea": ["Chelsea", "Chelsea F.C.", "Chelsea FC"],
    "crystal-palace": ["Crystal Palace", "Crystal Palace F.C.", "Crystal Palace FC"],
    "everton": ["Everton", "Everton F.C.", "Everton FC"],
    "fulham": ["Fulham", "Fulham F.C.", "Fulham FC"],
    "hull-city": ["Hull City", "Hull City A.F.C."],
    "ipswich-town": ["Ipswich Town", "Ipswich Town F.C."],
    "leeds-united": ["Leeds United", "Leeds United F.C."],
    "liverpool": ["Liverpool", "Liverpool F.C.", "Liverpool FC"],
    "manchester-city": ["Manchester City", "Manchester City F.C.", "Manchester City FC"],
    "manchester-united": ["Manchester United", "Manchester United F.C.", "Manchester United FC"],
    "newcastle-united": ["Newcastle United", "Newcastle United F.C."],
    "nottingham-forest": ["Nottingham Forest", "Nottingham Forest F.C."],
    "sunderland": ["Sunderland", "Sunderland A.F.C."],
    "tottenham-hotspur": ["Tottenham Hotspur", "Tottenham Hotspur F.C.", "Tottenham"],
    "west-ham-united": ["West Ham", "West Ham United", "West Ham United F.C."],
    "wolverhampton-wanderers": ["Wolves", "Wolverhampton Wanderers", "Wolverhampton Wanderers F.C."],
    "athletic-club": ["Athletic Club", "Athletic Bilbao", "Athletic Club Bilbao"],
    "atletico-de-madrid": ["Atlético Madrid", "Atletico Madrid", "Atlético de Madrid"],
    "ca-osasuna": ["Osasuna", "CA Osasuna"],
    "celta": ["Celta", "RC Celta de Vigo", "Celta de Vigo"],
    "elche-cf": ["Elche", "Elche CF"],
    "fc-barcelona": ["Barcelona", "FC Barcelona", "Futbol Club Barcelona"],
    "getafe-cf": ["Getafe", "Getafe CF"],
    "levante-ud": ["Levante", "Levante UD"],
    "málaga-cf": ["Málaga", "Málaga CF", "Malaga"],
    "r-racing-club": ["Racing Santander", "Racing Club"],
    "rayo-vallecano": ["Rayo Vallecano", "Rayo"],
    "rc-deportivo": ["Deportivo", "Deportivo de La Coruña", "Deportivo La Coruña"],
    "rcd-espanyol-de-barcelona": ["Espanyol", "RCD Espanyol", "Espanyol Barcelona"],
    "real-betis": ["Real Betis", "Betis"],
    "real-madrid": ["Real Madrid", "Real Madrid CF"],
    "real-sociedad": ["Real Sociedad", "Real Sociedad de Fútbol"],
    "sevilla-fc": ["Sevilla", "Sevilla FC"],
    "valencia-cf": ["Valencia", "Valencia CF"],
    "villarreal-cf": ["Villarreal", "Villarreal CF"],
    "bayern-munich": ["Bayern Munich", "Bayern München", "FC Bayern Munich"],
    "borussia-dortmund": ["Borussia Dortmund", "BVB", "Borussia Dortmund GmbH"],
    "rb-leipzig": ["RB Leipzig", "RasenBallsport Leipzig"],
    "vfb-stuttgart": ["VfB Stuttgart", "Stuttgart"],
    "tsg-hoffenheim": ["TSG Hoffenheim", "Hoffenheim", "TSG 1899 Hoffenheim"],
    "bayer-leverkusen": ["Bayer Leverkusen", "Bayer 04 Leverkusen", "Leverkusen"],
    "sport-club-freiburg": ["SC Freiburg", "Freiburg", "Sport-Club Freiburg"],
    "eintracht-frankfurt": ["Eintracht Frankfurt", "Frankfurt"],
    "fc-augsburg": ["FC Augsburg", "Augsburg"],
    "1-fsv-mainz-05": ["Mainz", "1. FSV Mainz 05", "FSV Mainz 05"],
    "1-fc-union-berlin": ["Union Berlin", "1. FC Union Berlin", "FC Union Berlin"],
    "atlanta-hawks": ["Atlanta Hawks", "Hawks"],
    "boston-celtics": ["Boston Celtics", "Celtics"],
    "brooklyn-nets": ["Brooklyn Nets", "Nets"],
    "charlotte-hornets": ["Charlotte Hornets", "Hornets"],
    "chicago-bulls": ["Chicago Bulls", "Bulls"],
    "cleveland-cavaliers": ["Cleveland Cavaliers", "Cavaliers"],
    "dallas-mavericks": ["Dallas Mavericks", "Mavericks"],
    "denver-nuggets": ["Denver Nuggets", "Nuggets"],
    "golden-state-warriors": ["Golden State Warriors", "Warriors", "GS Warriors"],
    "houston-rockets": ["Houston Rockets", "Rockets"],
    "indiana-pacers": ["Indiana Pacers", "Pacers"],
    "los-angeles-clippers": ["LA Clippers", "Los Angeles Clippers", "Clippers"],
    "los-angeles-lakers": ["LA Lakers", "Los Angeles Lakers", "Lakers"],
    "memphis-grizzlies": ["Memphis Grizzlies", "Grizzlies"],
    "miami-heat": ["Miami Heat", "Heat"],
    "milwaukee-bucks": ["Milwaukee Bucks", "Bucks"],
    "minnesota-timberwolves": ["Minnesota Timberwolves", "Timberwolves", "Wolves"],
    "new-orleans-pelicans": ["New Orleans Pelicans", "Pelicans"],
    "oklahoma-city-thunder": ["OKC Thunder", "Oklahoma City Thunder", "Thunder"],
    "orlando-magic": ["Orlando Magic", "Magic"],
    "philadelphia-76ers": ["Philadelphia 76ers", "76ers", "Philly 76ers"],
    "phoenix-suns": ["Phoenix Suns", "Suns"],
    "portland-trail-blazers": ["Portland Trail Blazers", "Trail Blazers", "Blazers"],
    "sacramento-kings": ["Sacramento Kings", "Kings"],
    "san-antonio-spurs": ["San Antonio Spurs", "Spurs"],
    "toronto-raptors": ["Toronto Raptors", "Raptors"],
    "utah-jazz": ["Utah Jazz", "Jazz"],
    "washington-wizards": ["Washington Wizards", "Wizards"],
    "arizona-cardinals": ["Arizona Cardinals", "Cards"],
    "atlanta-falcons": ["Atlanta Falcons", "Falcons"],
    "baltimore-ravens": ["Baltimore Ravens", "Ravens"],
    "buffalo-bills": ["Buffalo Bills", "Bills"],
    "carolina-panthers": ["Carolina Panthers", "Panthers"],
    "chicago-bears": ["Chicago Bears", "Bears"],
    "cincinnati-bengals": ["Cincinnati Bengals", "Bengals"],
    "cleveland-browns": ["Cleveland Browns", "Browns"],
    "dallas-cowboys": ["Dallas Cowboys", "Cowboys"],
    "denver-broncos": ["Denver Broncos", "Broncos"],
    "detroit-lions": ["Detroit Lions", "Lions"],
    "green-bay-packers": ["Green Bay Packers", "Packers"],
    "houston-texans": ["Houston Texans", "Texans"],
    "indianapolis-colts": ["Indianapolis Colts", "Colts"],
    "jacksonville-jaguars": ["Jacksonville Jaguars", "Jaguars"],
    "kansas-city-chiefs": ["Kansas City Chiefs", "Chiefs"],
    "las-vegas-raiders": ["Las Vegas Raiders", "Raiders"],
    "los-angeles-chargers": ["LA Chargers", "Los Angeles Chargers", "Chargers"],
    "los-angeles-rams": ["LA Rams", "Los Angeles Rams", "Rams"],
    "miami-dolphins": ["Miami Dolphins", "Dolphins"],
    "minnesota-vikings": ["Minnesota Vikings", "Vikings"],
    "new-england-patriots": ["New England Patriots", "Patriots", "NE Patriots"],
    "new-orleans-saints": ["New Orleans Saints", "Saints"],
    "new-york-giants": ["NY Giants", "New York Giants", "Giants"],
    "new-york-jets": ["NY Jets", "New York Jets", "Jets"],
    "philadelphia-eagles": ["Philadelphia Eagles", "Eagles"],
    "pittsburgh-steelers": ["Pittsburgh Steelers", "Steelers"],
    "san-francisco-49ers": ["San Francisco 49ers", "49ers", "SF 49ers"],
    "seattle-seahawks": ["Seattle Seahawks", "Seahawks"],
    "tampa-bay-buccaneers": ["Tampa Bay Buccaneers", "Buccaneers", "Bucs"],
    "tennessee-titans": ["Tennessee Titans", "Titans"],
    "washington-commanders": ["Washington Commanders", "Commanders", "Washington Football Team"],
    "arizona-diamondbacks": ["Arizona Diamondbacks", "Diamondbacks", "AZ Diamondbacks"],
    "atlanta-braves": ["Atlanta Braves", "Braves"],
    "baltimore-orioles": ["Baltimore Orioles", "Orioles"],
    "boston-red-sox": ["Boston Red Sox", "Red Sox", "BOS"],
    "chicago-cubs": ["Chicago Cubs", "Cubs"],
    "chicago-white-sox": ["Chicago White Sox", "White Sox", "CWS"],
    "cincinnati-reds": ["Cincinnati Reds", "Reds"],
    "cleveland-guardians": ["Cleveland Guardians", "Guardians", "Cleveland Indians"],
    "colorado-rockies": ["Colorado Rockies", "Rockies"],
    "detroit-tigers": ["Detroit Tigers", "Tigers"],
    "houston-astros": ["Houston Astros", "Astros"],
    "kansas-city-royals": ["Kansas City Royals", "Royals"],
    "los-angeles-angels": ["LA Angels", "Los Angeles Angels", "Angels", "LA Angels of Anaheim"],
    "miami-marlins": ["Miami Marlins", "Marlins"],
    "milwaukee-brewers": ["Milwaukee Brewers", "Brewers"],
    "minnesota-twins": ["Minnesota Twins", "Twins"],
    "new-york-mets": ["NY Mets", "New York Mets", "Mets"],
    "new-york-yankees": ["NY Yankees", "New York Yankees", "Yankees"],
    "oakland-athletics": ["Oakland Athletics", "Athletics", "OAK", "Oakland A's"],
    "philadelphia-phillies": ["Philadelphia Phillies", "Phillies"],
    "pittsburgh-pirates": ["Pittsburgh Pirates", "Pirates"],
    "san-diego-padres": ["San Diego Padres", "Padres"],
    "san-francisco-giants": ["SF Giants", "San Francisco Giants", "Giants"],
    "seattle-mariners": ["Seattle Mariners", "Mariners"],
    "st-louis-cardinals": ["St. Louis Cardinals", "Cardinals", "STL Cardinals"],
    "tampa-bay-rays": ["Tampa Bay Rays", "Rays"],
    "texas-rangers": ["Texas Rangers", "Rangers"],
    "toronto-blue-jays": ["Toronto Blue Jays", "Blue Jays"],
    "washington-nationals": ["Washington Nationals", "Nationals"],
}

def normalize(name):
    """Normalize a name for comparison."""
    name = name.lower().strip()
    name = re.sub(r'\b(f\.?c\.?|afc|sc|fc|club)\b', '', name)
    name = re.sub(r'[^\w\s]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name

def find_match(unknown_name, team_names):
    """Find a match for an unknown name in our team names."""
    normalized_unknown = normalize(unknown_name)
    
    # Try direct match
    for slug, aliases in team_names.items():
        for alias in aliases:
            if normalize(alias) == normalized_unknown:
                return slug
    
    # Try partial match
    best_match = None
    best_score = 0
    
    for slug, aliases in team_names.items():
        for alias in aliases:
            normalized_alias = normalize(alias)
            if normalized_alias in normalized_unknown or normalized_unknown in normalized_alias:
                score = min(len(normalized_alias), len(normalized_unknown)) / max(len(normalized_alias), len(normalized_unknown))
                if score > best_score:
                    best_score = score
                    best_match = slug
    
    if best_score >= 0.6:
        return best_match
    
    return None

def fetch_wikidata_owners():
    """Fetch owners from Wikidata."""
    print("Fetching owners from Wikidata...")
    
    query = """
    SELECT ?club ?clubLabel ?owner ?ownerLabel WHERE {
      ?club wdt:P31 wd:Q476028.
      ?club wdt:P127 ?owner.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY ?clubLabel
    """
    
    encoded = quote_plus(query.strip())
    url = f"https://query.wikidata.org/sparql?format=json&query={encoded}"
    
    headers = {"User-Agent": "Mozilla/5.0 (compatible; DataPipeline/1.0)"}
    req = Request(url, headers=headers)
    with urlopen(req, timeout=30) as resp:
        content = resp.read().decode("utf-8", errors="replace")
    
    data = json.loads(content)
    results = data.get("results", {}).get("bindings", [])
    
    print(f"Found {len(results)} owner relationships")
    
    owners_by_club = {}
    for r in results:
        club = r.get("clubLabel", {}).get("value", "unknown")
        owner = r.get("ownerLabel", {}).get("value", "unknown")
        
        if club not in owners_by_club:
            owners_by_club[club] = []
        
        owners_by_club[club].append(owner)
    
    return owners_by_club

def fetch_wikidata_sponsors():
    """Fetch shirt sponsors from Wikidata."""
    print("\nFetching shirt sponsors from Wikidata...")
    
    query = """
    SELECT ?club ?clubLabel ?sponsor ?sponsorLabel WHERE {
      ?club wdt:P31 wd:Q476028.
      ?club wdt:P3342 ?sponsor.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    """
    
    encoded = quote_plus(query.strip())
    url = f"https://query.wikidata.org/sparql?format=json&query={encoded}"
    
    headers = {"User-Agent": "Mozilla/5.0 (compatible; DataPipeline/1.0)"}
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8", errors="replace")
        
        data = json.loads(content)
        results = data.get("results", {}).get("bindings", [])
        
        print(f"Found {len(results)} shirt sponsor relationships")
        
        sponsors_by_club = {}
        for r in results:
            club = r.get("clubLabel", {}).get("value", "unknown")
            sponsor = r.get("sponsorLabel", {}).get("value", "unknown")
            
            if club not in sponsors_by_club:
                sponsors_by_club[club] = []
            
            sponsors_by_club[club].append(sponsor)
        
        return sponsors_by_club
    except Exception as e:
        print(f"Error fetching sponsors: {e}")
        return {}

def fetch_wikidata_stadium_sponsors():
    """Fetch stadium naming rights sponsors from Wikidata."""
    print("\nFetching stadium sponsors from Wikidata...")
    
    query = """
    SELECT ?club ?clubLabel ?stadium ?stadiumLabel ?sponsor ?sponsorLabel WHERE {
      ?club wdt:P31 wd:Q476028.
      ?club wdt:P115 ?stadium.
      ?stadium wdt:P3342 ?sponsor.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    LIMIT 100
    """
    
    encoded = quote_plus(query.strip())
    url = f"https://query.wikidata.org/sparql?format=json&query={encoded}"
    
    headers = {"User-Agent": "Mozilla/5.0 (compatible; DataPipeline/1.0)"}
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8", errors="replace")
        
        data = json.loads(content)
        results = data.get("results", {}).get("bindings", [])
        
        print(f"Found {len(results)} stadium sponsor relationships")
        
        stadium_sponsors_by_club = {}
        for r in results:
            club = r.get("clubLabel", {}).get("value", "unknown")
            sponsor = r.get("sponsorLabel", {}).get("value", "unknown")
            
            if club not in stadium_sponsors_by_club:
                stadium_sponsors_by_club[club] = []
            
            stadium_sponsors_by_club[club].append(sponsor)
        
        return stadium_sponsors_by_club
    except Exception as e:
        print(f"Error fetching stadium sponsors: {e}")
        return {}

def merge_into_team_jsons(owners_data, sponsors_data, stadium_sponsors_data):
    """Merge Wikidata into team JSON files."""
    print("\n" + "=" * 60)
    print("MERGING WIKIDATA INTO TEAM JSONs")
    print("=" * 60)
    
    # Load team mapping
    mapping_path = RAW_DATA_DIR / "wiki_mapping.json"
    if mapping_path.exists():
        with open(mapping_path) as f:
            team_mapping = json.load(f)
    else:
        team_mapping = []
    
    # Create wiki name -> slug mapping
    wiki_to_slug = {entry.get("wiki", ""): entry["slug"] for entry in team_mapping if "wiki" in entry}
    
    # Also add slug -> slug for direct matches
    for entry in team_mapping:
        slug = entry.get("slug", "")
        wiki_to_slug[slug] = slug
    
    updated_count = 0
    
    # Process each team JSON file
    for file_path in sorted(DATA_DIR.glob("*.json")):
        if file_path.name in ("index.json", "verified_data.json"):
            continue
        
        try:
            with open(file_path) as f:
                team_data = json.load(f)
        except Exception as e:
            print(f"  ERROR reading {file_path.name}: {e}")
            continue
        
        slug = file_path.stem
        modified = False
        
        # Try to match this slug to a Wikidata club
        # First check if we have a direct match
        club_names = TEAM_NAMES.get(slug, [slug.replace("-", " ").title()])
        
        # Try each club name
        matched_owners = None
        matched_sponsors = None
        matched_stadium_sponsors = None
        
        for club_name in club_names:
            # Try direct match in owners data
            if club_name in owners_data:
                matched_owners = owners_data[club_name]
                break
            
            # Try normalized match
            for wikidata_club in owners_data.keys():
                if normalize(wikidata_club) == normalize(club_name):
                    matched_owners = owners_data[wikidata_club]
                    break
            
            if matched_owners:
                break
        
        # Also try matching by slug in the owners data keys
        if not matched_owners:
            for wikidata_club in owners_data.keys():
                # Check if slug matches any part of the Wikidata club name
                wikidata_normalized = normalize(wikidata_club)
                for club_name in club_names:
                    club_normalized = normalize(club_name)
                    if club_normalized in wikidata_normalized or wikidata_normalized in club_normalized:
                        matched_owners = owners_data[wikidata_club]
                        break
                if matched_owners:
                    break
        
        # Same for sponsors
        if not matched_sponsors:
            for club_name in club_names:
                if club_name in sponsors_data:
                    matched_sponsors = sponsors_data[club_name]
                    break
                
                for wikidata_club in sponsors_data.keys():
                    if normalize(wikidata_club) == normalize(club_name):
                        matched_sponsors = sponsors_data[wikidata_club]
                        break
                
                if matched_sponsors:
                    break
        
        # Also try matching by slug in sponsors data keys
        if not matched_sponsors:
            for wikidata_club in sponsors_data.keys():
                wikidata_normalized = normalize(wikidata_club)
                for club_name in club_names:
                    club_normalized = normalize(club_name)
                    if club_normalized in wikidata_normalized or wikidata_normalized in club_normalized:
                        matched_sponsors = sponsors_data[wikidata_club]
                        break
                if matched_sponsors:
                    break
        
        # Same for stadium sponsors
        if not matched_stadium_sponsors:
            for club_name in club_names:
                if club_name in stadium_sponsors_data:
                    matched_stadium_sponsors = stadium_sponsors_data[club_name]
                    break
                
                for wikidata_club in stadium_sponsors_data.keys():
                    if normalize(wikidata_club) == normalize(club_name):
                        matched_stadium_sponsors = stadium_sponsors_data[wikidata_club]
                        break
                
                if matched_stadium_sponsors:
                    break
        
        # Merge owners into team data
        if matched_owners:
            # Filter out generic/slavenames like "Q12345" or "unknown"
            filtered_owners = [o for o in matched_owners if not o.startswith("Q") and o.lower() not in ("unknown", "the", "a", "an", "and")]
            if filtered_owners:
                # Only update if we don't already have an owner, or if the new owner is different
                existing_owner = team_data.get("owner")
                new_owner = filtered_owners[0]  # Take the first (most likely primary) owner
                
                if not existing_owner or existing_owner == "TBD" or existing_owner == "":
                    team_data["owner"] = new_owner
                    modified = True
                    print(f"  {slug}: Added owner '{new_owner}'")
                elif existing_owner != new_owner and new_owner not in existing_owner:
                    # Keep existing but add as alternate
                    if "alternate_owners" not in team_data:
                        team_data["alternate_owners"] = []
                    if new_owner not in team_data["alternate_owners"]:
                        team_data["alternate_owners"].append(new_owner)
                        modified = True
                        print(f"  {slug}: Added alternate owner '{new_owner}'")
        
        # Merge sponsors into team data
        if matched_sponsors:
            filtered_sponsors = [s for s in matched_sponsors if not s.startswith("Q") and s.lower() not in ("unknown", "the", "a", "an", "and")]
            if filtered_sponsors:
                existing_sponsors = team_data.get("sponsors", [])
                existing_sponsor_names = [s.get("name", s) if isinstance(s, dict) else s for s in existing_sponsors]
                
                for sponsor in filtered_sponsors:
                    if sponsor not in existing_sponsor_names:
                        # Add as a new sponsor entry
                        if isinstance(existing_sponsors, list):
                            existing_sponsors.append({
                                "name": sponsor,
                                "type": "company",
                                "category": "sponsor",
                                "rating": "D",
                                "rating_desc": "Unverified — from Wikidata",
                                "flags": [],
                                "deal_value": None,
                                "sources": ["Wikidata"],
                                "verified": False,
                                "last_updated": "2026-09-24T20:00:00+00:00",
                            })
                        else:
                            existing_sponsors = [{"name": sponsor, "type": "company", "category": "sponsor", "rating": "D", "rating_desc": "Unverified — from Wikidata", "flags": [], "deal_value": None, "sources": ["Wikidata"], "verified": False, "last_updated": "2026-09-24T20:00:00+00:00"}]
                        
                        modified = True
                        print(f"  {slug}: Added sponsor '{sponsor}'")
                
                team_data["sponsors"] = existing_sponsors
        
        # Merge stadium sponsors
        if matched_stadium_sponsors:
            filtered_stadium = [s for s in matched_stadium_sponsors if not s.startswith("Q") and s.lower() not in ("unknown", "the", "a", "an", "and")]
            if filtered_stadium:
                existing_sponsors = team_data.get("sponsors", [])
                existing_sponsor_names = [s.get("name", s) if isinstance(s, dict) else s for s in existing_sponsors]
                
                for sponsor in filtered_stadium:
                    if sponsor not in existing_sponsor_names:
                        if isinstance(existing_sponsors, list):
                            existing_sponsors.append({
                                "name": sponsor,
                                "type": "company",
                                "category": "stadium_naming_rights",
                                "rating": "D",
                                "rating_desc": "Unverified — from Wikidata",
                                "flags": [],
                                "deal_value": None,
                                "sources": ["Wikidata"],
                                "verified": False,
                                "last_updated": "2026-09-24T20:00:00+00:00",
                            })
                        else:
                            existing_sponsors = [{"name": sponsor, "type": "company", "category": "stadium_naming_rights", "rating": "D", "rating_desc": "Unverified — from Wikidata", "flags": [], "deal_value": None, "sources": ["Wikidata"], "verified": False, "last_updated": "2026-09-24T20:00:00+00:00"}]
                        
                        modified = True
                        print(f"  {slug}: Added stadium sponsor '{sponsor}'")
                
                team_data["sponsors"] = existing_sponsors
        
        # Save if modified
        if modified:
            team_data["last_updated"] = "2026-09-24T20:00:00+00:00"
            with open(file_path, 'w') as f:
                json.dump(team_data, f, indent=2)
            updated_count += 1
    
    print(f"\nUpdated {updated_count} team JSON files")
    return updated_count

def main():
    print("MERGE WIKIDATA INTO TEAM JSONs")
    print("=" * 60)
    
    # Fetch data from Wikidata
    owners_data = fetch_wikidata_owners()
    sponsors_data = fetch_wikidata_sponsors()
    stadium_sponsors_data = fetch_wikidata_stadium_sponsors()
    
    # Save raw data
    raw_owners_path = RAW_DATA_DIR / "wikidata_raw_owners.json"
    with open(raw_owners_path, 'w') as f:
        json.dump(owners_data, f, indent=2)
    print(f"\nSaved raw owners to {raw_owners_path}")
    
    raw_sponsors_path = RAW_DATA_DIR / "wikidata_raw_sponsors.json"
    with open(raw_sponsors_path, 'w') as f:
        json.dump(sponsors_data, f, indent=2)
    print(f"Saved raw sponsors to {raw_sponsors_path}")
    
    raw_stadium_path = RAW_DATA_DIR / "wikidata_raw_stadium_sponsors.json"
    with open(raw_stadium_path, 'w') as f:
        json.dump(stadium_sponsors_data, f, indent=2)
    print(f"Saved raw stadium sponsors to {raw_stadium_path}")
    
    # Merge into team JSONs
    updated = merge_into_team_jsons(owners_data, sponsors_data, stadium_sponsors_data)
    
    # Run verification
    print("\n" + "=" * 60)
    print("RUNNING VERIFICATION")
    print("=" * 60)
    
    verify_result = subprocess.run(
        ["python3", "scripts/verify_quality.py"],
        cwd=str(PIPELINE_DIR),
        capture_output=True,
        text=True,
        timeout=60
    )
    
    if verify_result.returncode == 0:
        # Parse the verification output
        for line in verify_result.stdout.split('\n'):
            if 'Total teams' in line or 'Verified' in line or 'Errors' in line or 'Contact info' in line or 'Shame methods' in line:
                print(line)
    
    # Git commit and push
    print("\n" + "=" * 60)
    print("GIT COMMIT AND PUSH")
    print("=" * 60)
    
    # Commit data changes
    subprocess.run(["git", "add", "-A"], cwd=str(DATA_DIR), check=True)
    result = subprocess.run(
        ["git", "commit", "-m", "Update: Wikidata owners/sponsors enriched for teams"],
        cwd=str(DATA_DIR),
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(f"Data repo commit: {result.stdout.strip()}")
        subprocess.run(["git", "push", "origin", "main"], cwd=str(DATA_DIR), check=True)
        print("Data repo pushed to GitHub")
    else:
        print(f"No changes to commit in data repo: {result.stderr.strip()}")
    
    # Commit pipeline changes (raw data files)
    subprocess.run(["git", "add", "-A"], cwd=str(PIPELINE_DIR), check=True)
    result = subprocess.run(
        ["git", "commit", "-m", "Update: Wikidata raw data + enrichment scripts"],
        cwd=str(PIPELINE_DIR),
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(f"Pipeline repo commit: {result.stdout.strip()}")
        subprocess.run(["git", "push", "origin", "main"], cwd=str(PIPELINE_DIR), check=True)
        print("Pipeline repo pushed to GitHub")
    else:
        print(f"No changes to commit in pipeline repo: {result.stderr.strip()}")
    
    print("\n" + "=" * 60)
    print("DONE")
    print("=" * 60)

if __name__ == "__main__":
    main()