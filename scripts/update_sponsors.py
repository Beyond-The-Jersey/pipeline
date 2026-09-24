#!/usr/bin/env python3
"""Update team JSON files with real sponsor and owner data from Wikipedia."""

import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import quote_plus

DATA_DIR = Path("/tmp/data/data")

def team_slug(name: str) -> str:
    """Convert team name to URL slug."""
    return name.lower().replace(" and ", "-").replace(" ", "-").replace(".", "")

def fetch_wikipedia_data(team_name: str) -> dict:
    """Fetch owner and sponsor data from Wikipedia for a team."""
    result = {"owner": None, "sponsors": []}
    
    # Create Wikipedia page name from team name
    wiki_name = team_name.replace(" ", "_").replace(".", "")
    # Handle special cases
    special_cases = {
        "Manchester United": "Manchester_United_F.C.",
        "Arsenal": "Arsenal_F.C.",
        "Liverpool": "Liverpool_F.C.",
        "Chelsea": "Chelsea_F.C.",
        "Tottenham Hotspur": "Tottenham_Hotspur_F.C.",
        "Manchester City": "Manchester_City_F.C.",
        "Newcastle United": "Newcastle_United_F.C.",
        "Aston Villa": "Aston_Villa_F.C.",
        "West Ham United": "West_Ham_United_F.C.",
        "Leeds United": "Leeds_United_F.C.",
        "Everton": "Everton_F.C.",
        "Wolves": "Wolverhampton_Wanderers_F.C.",
        "Crystal Palace": "Crystal_Palace_F.C.",
        "Brighton & Hove Albion": "Brighton_&_Hove_Albion",
        "Fulham": "Fulham_F.C.",
        "Brentford": "Brentford_F.C.",
        "Nottingham Forest": "Nottingham_Forest_F.C.",
        "Luton Town": "Luton_Town_F.C.",
        "Sheffield United": "Sheffield_United_F.C.",
        "Burnley": "Burnley_F.C.",
        "Bournemouth": "AFC_Bournemouth",
        "AFC Bournemouth": "AFC_Bournemouth",
        "Real Madrid": "Real_Madrid_CF",
        "Barcelona": "FC_Barcelona",
        "Atletico Madrid": "Atlético_Madrid",
        "Sevilla": "Sevilla_FC",
        "Valencia": "Valencia_CF",
        "Villarreal": "Villarreal_CF",
        "Athletic Bilbao": "Athletic_Bilbao",
        "Real Sociedad": "Real_Sociedad",
        "Celta Vigo": "RC_Celta_de_Vigo",
        "Betis": "Real_Betis",
        "Osasuna": "CA_Osasuna",
        "Alaves": "Deportivo_Alavés",
        "Elche": "Elche_CF",
        "Getafe": "Getafe_CF",
        "Las Palmas": "UD_Las_Palmas",
        "Rayo Vallecano": "Rayo_Vallecano",
        "Mallorca": "RCD_Mallorca",
        "Cadiz": "Cádiz_CF",
        "Almeria": "UD_Almería",
        "Granada": "Granada_CF",
        "Bayern Munich": "FC_Bayern_Munich",
        "Borussia Dortmund": "Borussia_Dortmund",
        "RB Leipzig": "RB_Leipzig",
        "Bayer Leverkusen": "Bayer_04_Leverkusen",
        "Eintracht Frankfurt": "Eintracht_Frankfurt",
        "Freiburg": "SC_Freiburg",
        "Wolfsburg": "VfL_Wolfsburg",
        "Mainz": "1._FSV_Mainz_05",
        "Augsburg": "FC_Augsburg",
        "Stuttgart": "VfB_Stuttgart",
        "Hoffenheim": "TSG_1899_Hoffenheim",
        "Union Berlin": "1._FC_Union_Berlin",
        "Heidenheim": "1._FC_Heidenheim",
        "St. Pauli": "FC_St._Pauli",
        "Darmstadt": "SV_Darmstadt_98",
        "Borussia Monchengladbach": "Borussia_Mönchengladbach",
        "Werder Bremen": "SV_Werder_Bremen",
        "Schalke 04": "FC_Schalke_04",
        "Hamburger SV": "Hamburger_SV",
        "Koln": "1._FC_Köln",
        "Atlanta Hawks": "Atlanta_Hawks",
        "Boston Celtics": "Boston_Celtics",
        "Brooklyn Nets": "Brooklyn_Nets",
        "New York Knicks": "New_York_Knicks",
        "Philadelphia 76ers": "Philadelphia_76ers",
        "Toronto Raptors": "Toronto_Raptors",
        "Chicago Bulls": "Chicago_Bulls",
        "Cleveland Cavaliers": "Cleveland_Cavaliers",
        "Detroit Pistons": "Detroit_Pistons",
        "Indiana Pacers": "Indiana_Pacers",
        "Milwaukee Bucks": "Milwaukee_Bucks",
        "Atlanta Hawks": "Atlanta_Hawks",
        "Charlotte Hornets": "Charlotte_Hornets",
        "Miami Heat": "Miami_Heat",
        "Orlando Magic": "Orlando_Magic",
        "Washington Wizards": "Washington_Wizards",
        "Denver Nuggets": "Denver_Nuggets",
        "Minnesota Timberwolves": "Minnesota_Timberwolves",
        "Oklahoma City Thunder": "Oklahoma_City_Thunder",
        "Portland Trail Blazers": "Portland_Trail_Blazers",
        "Utah Jazz": "Utah_Jazz",
        "Golden State Warriors": "Golden_State_Warriors",
        "LA Clippers": "Los_Angeles_Clippers",
        "Los Angeles Lakers": "Los_Angeles_Lakers",
        "Phoenix Suns": "Phoenix_Suns",
        "Sacramento Kings": "Sacramento_Kings",
        "Dallas Mavericks": "Dallas_Mavericks",
        "Houston Rockets": "Houston_Rockets",
        "Memphis Grizzlies": "Memphis_Grizzlies",
        "New Orleans Pelicans": "New_Orleans_Pelicans",
        "San Antonio Spurs": "San_Antonio_Spurs",
        "Arizona Cardinals": "Arizona_Cardinals",
        "Atlanta Falcons": "Atlanta_Falcons",
        "Baltimore Ravens": "Baltimore_Ravens",
        "Buffalo Bills": "Buffalo_Bills",
        "Carolina Panthers": "Carolina_Panthers",
        "Chicago Bears": "Chicago_Bears",
        "Cincinnati Bengals": "Cincinnati_Bengals",
        "Cleveland Browns": "Cleveland_Browns",
        "Dallas Cowboys": "Dallas_Cowboys",
        "Denver Broncos": "Denver_Broncos",
        "Detroit Lions": "Detroit_Lions",
        "Green Bay Packers": "Green_Bay_Packers",
        "Houston Texans": "Houston_Texans",
        "Indianapolis Colts": "Indianapolis_Colts",
        "Jacksonville Jaguars": "Jacksonville_Jaguars",
        "Kansas City Chiefs": "Kansas_City_Chiefs",
        "Las Vegas Raiders": "Las_Vegas_Raiders",
        "Los Angeles Chargers": "Los_Angeles_Chargers",
        "Los Angeles Rams": "Los_Angeles_Rams",
        "Miami Dolphins": "Miami_Dolphins",
        "Minnesota Vikings": "Minnesota_Vikings",
        "New England Patriots": "New_England_Patriots",
        "New Orleans Saints": "New_Orleans_Saints",
        "New York Giants": "New_York_Giants",
        "New York Jets": "New_York_Jets",
        "Philadelphia Eagles": "Philadelphia_Eagles",
        "Pittsburgh Steelers": "Pittsburgh_Steelers",
        "San Francisco 49ers": "San_Francisco_49ers",
        "Seattle Seahawks": "Seattle_Seahawks",
        "Tampa Bay Buccaneers": "Tampa_Bay_Buccaneers",
        "Tennessee Titans": "Tennessee_Titans",
        "Washington Commanders": "Washington_Commanders",
        "Arizona Diamondbacks": "Arizona_Diamondbacks",
        "Atlanta Braves": "Atlanta_Braves",
        "Baltimore Orioles": "Baltimore_Orioles",
        "Boston Red Sox": "Boston_Red_Sox",
        "Chicago Cubs": "Chicago_Cubs",
        "Chicago White Sox": "Chicago_White_Sox",
        "Cincinnati Reds": "Cincinnati_Reds",
        "Cleveland Guardians": "Cleveland_Guardians",
        "Colorado Rockies": "Colorado_Rockies",
        "Detroit Tigers": "Detroit_Tigers",
        "Houston Astros": "Houston_Astros",
        "Kansas City Royals": "Kansas_City_Royals",
        "Los Angeles Angels": "Los_Angeles_Angels",
        "Los Angeles Dodgers": "Los_Angeles_Dodgers",
        "Miami Marlins": "Miami_Marlins",
        "Milwaukee Brewers": "Milwaukee_Brewers",
        "Minnesota Twins": "Minnesota_Twins",
        "New York Mets": "New_York_Mets",
        "New York Yankees": "New_York_Yankees",
        "Oakland Athletics": "Oakland_Athletics",
        "Philadelphia Phillies": "Philadelphia_Phillies",
        "Pittsburgh Pirates": "Pittsburgh_Pirates",
        "San Diego Padres": "San_Diego_Padres",
        "San Francisco Giants": "San_Francisco_Giants",
        "Seattle Mariners": "Seattle_Mariners",
        "St. Louis Cardinals": "St._Louis_Cardinals",
        "Tampa Bay Rays": "Tampa_Bay_Rays",
        "Texas Rangers": "Texas_Rangers",
        "Toronto Blue Jays": "Toronto_Blue_Jays",
        "Washington Nationals": "Washington_Nationals",
    }
    
    if team_name in special_cases:
        wiki_name = special_cases[team_name]
    else:
        # Default transformation
        wiki_name = team_name.replace(" ", "_").replace(".", "")
    
    url = f"https://en.wikipedia.org/wiki/{quote_plus(wiki_name)}"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; BehindTheJersey/0.1)"}
    
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=20) as resp:
            content = resp.read().decode("utf-8", errors="replace")
            # Debug: Check if we got content
            if len(content) < 1000:
                print(f"  WARNING: Got very short content for {team_name}: {len(content)} chars")
            if "Owner" in content:
                print(f"  DEBUG: Found 'Owner' in content for {team_name}")
    except (URLError, HTTPError) as e:
        print(f"  WARNING: Could not fetch Wikipedia for {team_name}: {e}")
        return result
    
    # Extract owner from infobox
    # Pattern: | Owner(s) | value | or | Owner | value | (wiki-table format)
    # OR <th class="infobox-label">Owner</th><td class="infobox-data">value</td> (HTML format)
    owner_patterns = [
        r'\|\s*Owner\(s\)\s*\|\s*(.+?)\s*\|',
        r'\|\s*Owner\s*\|\s*(.+?)\s*\|',
        r'<th[^>]*class="[^"]*infobox-label[^"]*"[^>]*>Owner</th>\s*<td[^>]*class="[^"]*infobox-data[^"]*"[^>]*>(.+?)</td>',
    ]
    print(f"    DEBUG: Checking {len(owner_patterns)} owner patterns")
    for pattern in owner_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        print(f"    DEBUG: Testing pattern: {pattern}")
        if match:
            print(f"    DEBUG: Owner regex matched: {repr(match.group(0))}")
            # For HTML format, the value is in group 1
            # For wiki-table format, the value is in group 1
            owner_text = match.group(1).strip()
            print(f"    DEBUG: Raw owner_text: {repr(owner_text)}")
            # Clean up wiki markup and HTML
            # Remove [[Link|text]] or [[Link]] format
            owner_text = re.sub(r'\[\[([^\]]+)\|([^\]]+)\]\]', r'\2', owner_text)
            owner_text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', owner_text)
            # Remove [text](url) format
            owner_text = re.sub(r'\[[^\]]+\]\([^)]+\)', '', owner_text)
            # Remove HTML tags
            owner_text = re.sub(r'<[^>]+>', '', owner_text)
            owner_text = re.sub(r'<[^>]+>', '', owner_text).strip()
            owner_text = re.sub(r'\[\d+\]', '', owner_text).strip()
            # Skip if it looks like wiki markup or is too short
            if owner_text and not owner_text.startswith('|') and len(owner_text) > 2:
                if owner_text.lower() not in ('none', 'tbd', '—', '–', 'the', 'a', 'an', 'and', 'or', 'but'):
                    result["owner"] = owner_text
                    print(f"    DEBUG: Setting owner to: {repr(owner_text)}")
                else:
                    print(f"    DEBUG: Owner rejected as stop word: {repr(owner_text)}")
            else:
                print(f"    DEBUG: Owner rejected (empty or too short): {repr(owner_text)}")
            break
        else:
                        print(f"    DEBUG: Owner regex pattern did not match")
    sponsor_patterns = [
        r'\|\s*Shirt sponsor\s*\|\s*(.+?)\s*\|',
        r'\|\s*Kit manufacturer\s*\|\s*(.+?)\s*\|',
        r'\|\s*Sponsor\s*\|\s*(.+?)\s*\|',
        r'<th[^>]*class="[^"]*infobox-label[^"]*"[^>]*>Shirt sponsor</th>\s*<td[^>]*class="[^"]*infobox-data[^"]*"[^>]*>(.+?)</td>',
        r'<th[^>]*class="[^"]*infobox-label[^"]*"[^>]*>Kit manufacturer</th>\s*<td[^>]*class="[^"]*infobox-data[^"]*"[^>]*>(.+?)</td>',
        r'<th[^>]*class="[^"]*infobox-label[^"]*"[^>]*>Sponsor</th>\s*<td[^>]*class="[^"]*infobox-data[^"]*"[^>]*>(.+?)</td>',
    ]
    for pattern in sponsor_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            # For wiki-table format, the value is in group 1
            # For HTML format, the value is in group 1
            sponsor_text = match.group(1).strip()
            # Clean up wiki markup and HTML
            # Remove [[Link|text]] or [[Link]] format
            sponsor_text = re.sub(r'\[\[([^\]]+)\|([^\]]+)\]\]', r'\2', sponsor_text)
            sponsor_text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', sponsor_text)
            # Remove [text](url) format
            sponsor_text = re.sub(r'\[[^\]]+\]\([^)]+\)', '', sponsor_text)
            # Remove HTML tags
            sponsor_text = re.sub(r'<[^>]+>', '', sponsor_text)
            sponsor_text = re.sub(r'<[^>]+>', '', sponsor_text).strip()
            sponsor_text = re.sub(r'\[\d+\]', '', sponsor_text).strip()
            # Skip if it looks like wiki markup or is too short
            if sponsor_text and not sponsor_text.startswith('|') and len(sponsor_text) > 2:
                if sponsor_text.lower() not in ('none', 'tbd', '—', '–', 'the', 'a', 'an', 'and', 'or', 'but'):
                    result["sponsors"].append({
                        "name": sponsor_text,
                        "type": "company",
                        "category": "sponsor",
                        "rating": "D",
                        "rating_desc": "Unverified — needs review",
                        "flags": [],
                        "deal_value": None,
                        "sources": [url],
                        "verified": False,
                        "last_updated": datetime.now(timezone.utc).isoformat(),
                    })
                    print(f"    DEBUG: Adding sponsor: {repr(sponsor_text)}")
                else:
                    print(f"    DEBUG: Sponsor rejected as stop word: {repr(sponsor_text)}")
            else:
                print(f"    DEBUG: Sponsor rejected (empty or too short): {repr(sponsor_text)}")
            break  # Only take the first sponsor found
    
    # If no sponsor in infobox, look in Sponsorship section
    if not result["sponsors"]:
        sponsorship_match = re.search(r'==\s*Sponsorship\s*==\s*(.*?)(?=\n==|\Z)', content, re.IGNORECASE | re.DOTALL)
        if sponsorship_match:
            section = sponsorship_match.group(1)
            # Look for sponsor mentions
            sponsor_mentions = re.findall(r'(?:sponsored\s+by\s+|sponsorship\s+with\s+|main\s+sponsor\s*:?\s*|kit\s*manufacturer\s*:?\s*|shirt\s*sponsor\s*:?\s*)([^.\n]+?)(?:\s+as\s+|\s+is\s+|\s+brand|\s+starting|\s+\.|$)', section, re.IGNORECASE)
            print(f"    DEBUG: Found {len(sponsor_mentions)} potential sponsors in Sponsorship section")
            for mention in sponsor_mentions[:2]:  # Take up to 2 sponsors
                sponsor_text = mention.strip()
                # Clean up wiki markup
                # Remove [[Link|text]] or [[Link]] format
                sponsor_text = re.sub(r'\[\[([^\]]+)\|([^\]]+)\]\]', r'\2', sponsor_text)
                sponsor_text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', sponsor_text)
                # Remove [text](url) format
                sponsor_text = re.sub(r'\[[^\]]+\]\([^)]+\)', '', sponsor_text)
                sponsor_text = re.sub(r'<[^>]+>', '', sponsor_text).strip()
                sponsor_text = re.sub(r'\[\d+\]', '', sponsor_text).strip()
                sponsor_text = re.sub(r'^\s*(the|a|an|car|retailer)\s+', '', sponsor_text, flags=re.IGNORECASE)
                sponsor_text = sponsor_text.strip()
                if sponsor_text and len(sponsor_text) > 2 and sponsor_text.lower() not in ('none', 'tbd', '—', '–', 'and', 'or', 'but'):
                    result["sponsors"].append({
                        "name": sponsor_text,
                        "type": "company",
                        "category": "sponsor",
                        "rating": "D",
                        "rating_desc": "Unverified — needs review",
                        "flags": [],
                        "deal_value": None,
                        "sources": [url],
                        "verified": False,
                        "last_updated": datetime.now(timezone.utc).isoformat(),
                    })
                    print(f"    DEBUG: Adding sponsor from section: {repr(sponsor_text)}")
                else:
                    print(f"    DEBUG: Sponsor from section rejected: {repr(sponsor_text)}")
    
    return result

def update_team_json(file_path: Path) -> bool:
    """Update a single team JSON file with Wikipedia data."""
    try:
        with open(file_path) as fh:
            data = json.load(fh)
    except Exception as e:
        print(f"  ERROR: Could not read {file_path.name}: {e}")
        return False
    
    team_name = data.get("team", "")
    if not team_name:
        print(f"  WARNING: No team name in {file_path.name}")
        return False
    
    print(f"  Processing {team_name}...")
    
    # Fetch Wikipedia data
    wiki_data = fetch_wikipedia_data(team_name)
    print(f"    DEBUG: wiki_data owner: {repr(wiki_data.get('owner'))}")
    print(f"    DEBUG: data owner: {repr(data.get('owner'))}")
    
    # Update data if we found new information
    updated = False
    
    if wiki_data.get("owner") and not data.get("owner"):
        data["owner"] = wiki_data["owner"]
        updated = True
        print(f"    Found owner: {wiki_data['owner']}")
    
    if wiki_data.get("sponsors") and not data.get("sponsors"):
        data["sponsors"] = wiki_data["sponsors"]
        updated = True
        print(f"    Found {len(wiki_data['sponsors'])} sponsor(s)")
    
    if updated:
        data["last_updated"] = datetime.now(timezone.utc).isoformat()
        try:
            with open(file_path, 'w') as fh:
                json.dump(data, fh, indent=2)
            print(f"    Updated {file_path.name}")
            return True
        except Exception as e:
            print(f"  ERROR: Could not write {file_path.name}: {e}")
            return False
    else:
        print(f"    No new data found")
        return False

def main():
    """Main function to update all team JSON files."""
    if not DATA_DIR.exists():
        print(f"ERROR: Data directory not found: {DATA_DIR}")
        sys.exit(1)
    
    json_files = list(DATA_DIR.glob("*.json"))
    # Exclude index files
    team_files = [f for f in json_files if f.name not in ("index.json", "verified_data.json")]
    
    print(f"Found {len(team_files)} team JSON files to process")
    print("=" * 50)
    
    updated_count = 0
    for file_path in sorted(team_files):
        if update_team_json(file_path):
            updated_count += 1
        print()
    
    print("=" * 50)
    print(f"Summary: Updated {updated_count}/{len(team_files)} team files")
    
    # Regenerate index.json
    print("\nRegenerating index.json...")
    try:
        teams_list = []
        for file_path in sorted(team_files):
            with open(file_path) as fh:
                data = json.load(fh)
            teams_list.append({
                "name": data.get("team", ""),
                "sport": data.get("sport", ""),
                "league": data.get("league", ""),
                "file": file_path.name
            })
        
        index_data = {
            "version": "0.1",
            "last_updated": datetime.now(timezone.utc).isoformat(),
            "teams": teams_list,
            "total_teams": len(teams_list)
        }
        
        index_path = DATA_DIR / "index.json"
        with open(index_path, 'w') as fh:
            json.dump(index_data, fh, indent=2)
        print(f"Updated {index_path}")
        
    except Exception as e:
        print(f"ERROR: Could not regenerate index: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()