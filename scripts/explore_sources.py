#!/usr/bin/env python3
"""Explore additional data sources for sponsor/owner data."""

import json
import re
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import quote_plus

# Test URLs for additional sources
SOURCES = {
    # Wikidata SPARQL endpoint
    "wikidata": "https://query.wikidata.org/sparql?format=json&query=",
    
    # Transfermarkt team pages (structured owner data)
    "transfermarkt": "https://www.transfermarkt.com/{slug}/startseite/verein/{id}",
    
    # Sports Business Journal
    "sportico": "https://www.sportico.com/",
    
    # Company sponsor pages
    "sponsor_companies": [
        "https://www.emirates.com/",  # Arsenal sponsor
        "https://www.teamviewer.com/",  # ManUtd sponsor
    ],
    
    # News archives for sponsorship announcements
    "news": "https://news.google.com/search?q={team}+sponsor+OR+ownership",
}

# Wikidata SPARQL query for football club owners
WIKIDATA_QUERY = """
SELECT ?club ?clubLabel ?owner ?ownerLabel WHERE {
  ?club wdt:P31 wd:Q476028.
  ?club wdt:P127 ?owner.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
LIMIT 50
"""

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

def test_wikidata():
    """Test Wikidata SPARQL for owner data."""
    print("=" * 60)
    print("TESTING WIKIDATA (Structured Wikipedia data)")
    print("=" * 60)
    
    query = WIKIDATA_QUERY.strip()
    encoded_query = quote_plus(query)
    url = f"{SOURCES['wikidata']}{encoded_query}"
    
    print(f"URL: {url[:100]}...")
    content = fetch(url)
    
    if content.startswith("ERROR"):
        print(f"Failed: {content}")
        return {}
    
    try:
        data = json.loads(content)
        results = data.get("results", {}).get("bindings", [])
        print(f"Found {len(results)} owner relationships")
        
        owners = {}
        for r in results[:10]:
            club = r.get("clubLabel", {}).get("value", "unknown")
            owner = r.get("ownerLabel", {}).get("value", "unknown")
            owners[club] = owner
            print(f"  {club}: {owner}")
        
        return owners
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        print(f"Content preview: {content[:500]}")
        return {}

def test_transfermarkt():
    """Test Transfermarkt for team owner data."""
    print("\n" + "=" * 60)
    print("TESTING TRANSMARKET (Soccer team ownership)")
    print("=" * 60)
    
    # Test with a known team
    test_urls = [
        ("Manchester United", "manchester-united/startseite/verein/985"),
        ("Arsenal", "arsenal-fc/startseite/verein/11"),
        ("FC Barcelona", "fc-barcelona/startseite/verein/131"),
    ]
    
    results = {}
    for name, path in test_urls:
        url = f"https://www.transfermarkt.com/{path}"
        print(f"\nFetching: {name}")
        print(f"URL: {url}")
        content = fetch(url)
        
        if content.startswith("ERROR"):
            print(f"  Failed: {content}")
            continue
        
        # Look for owner information
        owner_patterns = [
            r'Owner.*?<.*?>(.*?)<',
            r'Besitzer.*?<.*?>(.*?)<',  # German
            r'Owner',
            r'President',
            r'Chairman',
        ]
        
        found = False
        for pattern in owner_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                print(f"  Found: {pattern} -> {match.group(0)[:100]}")
                found = True
                break
        
        if not found:
            # Look for any mention of owner/president/chairman
            owner_matches = re.findall(r'(?:owner|president|chairman|besitzer|präsident).{0,100}', content, re.IGNORECASE)
            if owner_matches:
                print(f"  Found {len(owner_matches)} potential owner mentions")
                for m in owner_matches[:3]:
                    print(f"    - {m[:80]}")
            else:
                print(f"  No owner info found")
        
        results[name] = {"url": url, "content_length": len(content), "found": found}
    
    return results

def test_official_league_sites():
    """Test official league sites with different URL patterns."""
    print("\n" + "=" * 60)
    print("TESTING OFFICIAL LEAGUE SITES (Alternative URLs)")
    print("=" * 60)
    
    test_urls = {
        "Premier League": [
            "https://www.premierleague.com/clubs",
            "https://www.premierleague.com/clubs/1/Arsenal",
            "https://www.premierleague.com/clubs/2/Aston-Villa",
        ],
        "La Liga": [
            "https://www.laliga.com/en-GB/laliga-easports/clubs",
            "https://www.laliga.com/en-GB/laliga-easports/clubs/barcelona",
            "https://www.laliga.com/en-GB/laliga-easports/clubs/real-madrid",
        ],
        "Bundesliga": [
            "https://www.bundesliga.com/en/bundesliga/clubs",
            "https://www.bundesliga.com/en/bundesliga/clubs/bayern-munich",
            "https://www.bundesliga.com/en/bundesliga/clubs/borussia-dortmund",
        ],
        "NBA": [
            "https://www.nba.com/teams",
            "https://www.nba.com/warriors",
            "https://www.nba.com/lakers",
        ],
        "NFL": [
            "https://www.nfl.com/teams/",
            "https://www.nfl.com/teams/kansas-city-chiefs/",
            "https://www.nfl.com/teams/dallas-cowboys/",
        ],
        "MLB": [
            "https://www.mlb.com/dodgers",
            "https://www.mlb.com/yankees",
            "https://www.mlb.com/red-sox",
        ],
    }
    
    results = {}
    for league, urls in test_urls.items():
        print(f"\n{league}:")
        results[league] = []
        for url in urls[:2]:  # Test first 2 URLs per league
            print(f"  Testing: {url}")
            content = fetch(url)
            
            if content.startswith("ERROR"):
                print(f"    Failed: {content}")
                results[league].append({"url": url, "status": "error"})
                continue
            
            # Check for sponsor/owner keywords
            sponsor_keywords = ["sponsor", "owner", "partnership", "kit", "shirt sponsor", "stadium naming"]
            found_keywords = []
            for keyword in sponsor_keywords:
                if keyword.lower() in content.lower():
                    found_keywords.append(keyword)
            
            status = "has sponsor/owner data" if found_keywords else "no sponsor/owner data"
            print(f"    Status: {status}")
            if found_keywords:
                print(f"    Keywords found: {', '.join(found_keywords)}")
            
            results[league].append({
                "url": url,
                "status": status,
                "keywords": found_keywords,
                "content_length": len(content)
            })
    
    return results

def test_news_search():
    """Test news search for sponsorship announcements."""
    print("\n" + "=" * 60)
    print("TESTING NEWS SEARCH (Sponsorship announcements)")
    print("=" * 60)
    
    search_queries = [
        "Arsenal FC sponsor 2024",
        "Manchester United shirt sponsor",
        "FC Barcelona owner",
        "Real Madrid sponsor deal",
    ]
    
    results = {}
    for query in search_queries:
        url = f"https://news.google.com/search?q={quote_plus(query)}"
        print(f"\nSearching: {query}")
        print(f"URL: {url}")
        content = fetch(url)
        
        if content.startswith("ERROR"):
            print(f"  Failed: {content}")
            continue
        
        # Look for article titles
        articles = re.findall(r'<a[^>]*class="DY5T1d".*?>(.*?)</a>', content)
        if not articles:
            articles = re.findall(r'<h3.*?>(.*?)</h3>', content)
        
        print(f"  Found {len(articles)} articles")
        for a in articles[:3]:
            print(f"    - {a[:80]}")
        
        results[query] = {"articles": len(articles), "url": url}
    
    return results

def main():
    print("EXPLORING ADDITIONAL DATA SOURCES FOR SPONSOR/OWNER DATA")
    print("=" * 60)
    
    # Test Wikidata
    wikidata_owners = test_wikidata()
    
    # Test Transfermarkt
    transfermarkt_results = test_transfermarkt()
    
    # Test official league sites
    league_results = test_official_league_sites()
    
    # Test news search
    news_results = test_news_search()
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Wikidata: {len(wikidata_owners)} owner relationships found")
    print(f"Transfermarkt: {len(transfermarkt_results)} teams tested")
    print(f"League sites: {len(league_results)} leagues tested")
    print(f"News search: {len(news_results)} queries tested")
    
    # Save results
    output = {
        "wikidata_owners": wikidata_owners,
        "transfermarkt": transfermarkt_results,
        "league_sites": league_results,
        "news_search": news_results,
    }
    
    output_path = Path("raw_data/source_exploration.json")
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {output_path}")

if __name__ == "__main__":
    main()