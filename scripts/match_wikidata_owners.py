#!/usr/bin/env python3
"""Match Wikidata owners/sponsors to our team slugs with better name matching."""

import json
import re
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import quote_plus

OUTPUT_DIR = Path("raw_data")
OUTPUT_DIR.mkdir(exist_ok=True)

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
    # La Liga
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
    # Bundesliga
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
    # NBA
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
    # NFL
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
    # MLB
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
    "pitchers-pirates": ["Pittsburgh Pirates", "Pirates"],
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
    
    # Try partial match (unknown name contains team name or vice versa)
    best_match = None
    best_score = 0
    
    for slug, aliases in team_names.items():
        for alias in aliases:
            normalized_alias = normalize(alias)
            # Check if one contains the other
            if normalized_alias in normalized_unknown or normalized_unknown in normalized_alias:
                # Score by length ratio (longer match = better)
                score = min(len(normalized_alias), len(normalized_unknown)) / max(len(normalized_alias), len(normalized_unknown))
                if score > best_score:
                    best_score = score
                    best_match = slug
    
    # Only return if confidence is high
    if best_score >= 0.6:
        return best_match
    
    return None

def main():
    print("MATCHING WIKIDATA TO OUR TEAMS WITH BETTER NAME MATCHING")
    print("=" * 60)
    
    # Get Wikidata data (same query as before)
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
    
    print(f"Found {len(results)} owner relationships in Wikidata")
    
    # Build owners dict
    owners_by_club = {}
    for r in results:
        club = r.get("clubLabel", {}).get("value", "unknown")
        owner = r.get("ownerLabel", {}).get("value", "unknown")
        
        if club not in owners_by_club:
            owners_by_club[club] = []
        
        owners_by_club[club].append(owner)
    
    # Match to our teams
    print("\nMatching Wikidata owners to our teams...")
    matched_owners = {}
    unmatched_clubs = []
    
    for club, owners in owners_by_club.items():
        slug = find_match(club, TEAM_NAMES)
        if slug:
            if slug not in matched_owners:
                matched_owners[slug] = []
            matched_owners[slug].extend(owners)
        else:
            unmatched_clubs.append(club)
    
    # Remove duplicates
    for slug in matched_owners:
        matched_owners[slug] = list(set(matched_owners[slug]))
    
    print(f"\nMatched {len(matched_owners)} teams with owner data")
    print(f"Unmatched clubs: {len(unmatched_clubs)}")
    
    # Print matched teams
    print("\n" + "=" * 60)
    print("MATCHED TEAMS WITH OWNER DATA")
    print("=" * 60)
    
    for slug in sorted(matched_owners.keys()):
        owners = matched_owners[slug]
        print(f"\n{slug}:")
        for owner in owners:
            print(f"  - {owner}")
    
    # Save to file
    output_path = OUTPUT_DIR / "wikidata_owners_matched.json"
    with open(output_path, 'w') as f:
        json.dump(matched_owners, f, indent=2)
    print(f"\n\nSaved matched owners to {output_path}")
    
    # Also save unmatched for debugging
    unmatched_path = OUTPUT_DIR / "wikidata_unmatched_clubs.json"
    with open(unmatched_path, 'w') as f:
        json.dump(unmatched_clubs, f, indent=2)
    print(f"Saved unmatched clubs to {unmatched_path}")

if __name__ == "__main__":
    main()