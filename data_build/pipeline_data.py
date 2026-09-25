"""Curated additions merged into the website seed to build normalized/.

Rules (from Beyond-The-Jersey/website docs/data-request):
  * seed is the base; seed ids are kept
  * ids are ASCII kebab-case
  * no invented facts: unknown stays null / omitted
  * Wikipedia/Wikidata are leads; cite the primary or named document
"""

D = "2026-09-24"

# ---------------------------------------------------------------- sources
SRC = {
    "scoreandchange-la-liga": {
        "name": "Score and Change, Overview of the 2026/2027 La Liga sponsors",
        "date": "2026-09-06",
        "url": "https://www.scoreandchange.com/la-liga-sponsors/",
    },
    "marketinginstitut": {
        "name": "Deutsches Institut fuer Marketing, Trikotsponsoren der Bundesliga (stand 4 Aug 2026)",
        "date": "2026-08-04",
        "url": "https://www.marketinginstitut.biz/blog/trikotsponsoren-bundesliga/",
    },
    "footballkitarchive": {
        "name": "Football Kit Archive, Bundesliga 2026-27 kits",
        "date": "2026-09-24",
        "url": "https://www.footballkitarchive.com/bundesliga-kits-2026-27-l34/",
    },
    "sportspro-barca-spotify": {
        "name": "SportsPro, Barcelona Spotify and Camp Nou naming rights",
        "date": "2025-10",
        "url": "https://www.sportspro.com/news/sponsorship-marketing/sponsorship/barcelona-spotify-shirt-sponsor-camp-nou-naming-rights-october-2025/",
    },
    "scoreandchange-pl": {
        "name": "Score and Change, Overview of the 2026/2027 Premier League sponsors",
        "date": "2026-09-17",
        "url": "https://www.scoreandchange.com/overview-of-the-2026-2027-premier-league-sponsors/",
    },
    "scoreandchange-laliga": {
        "name": "Score and Change, La Liga sponsors 2026/27",
        "date": "2026-09-06",
        "url": "https://www.scoreandchange.com/la-liga-sponsors/",
    },
    "sportspro-snapdragon": {
        "name": "SportsPro, Manchester United and Qualcomm Snapdragon shirt deal",
        "date": "2024-08",
        "url": "https://www.sportspro.com/news/manchester-united-qualcomm-snapdragon-shirt-sponsorship/",
    },
    "sportspro-pl-business": {
        "name": "SportsPro, The business of the 2026/27 Premier League season",
        "date": "2026-09",
        "url": "https://www.sportspro.com/analysis/finance-investment/premier-league-2026-27-season-tv-rights-sponsors-finances-valuations/",
    },
    "guardian-visit-saudi": {
        "name": "The Guardian, FIFA admits defeat over Saudi sponsorship of Women's World Cup",
        "date": "2023-03-16",
        "url": "https://www.theguardian.com/football/2023/mar/16/fifa-defeat-saudi-sponsorship-womens-world-cup-plans-infantino",
    },
    "espn-uefa-gazprom": {
        "name": "The Athletic, UEFA ends partnership with Gazprom",
        "date": "2022-02-28",
        "url": "https://www.nytimes.com/athletic/4181788/2022/02/28/uefa-ends-partnership-with-russian-energy-company-gazprom/",
    },
    "espn-haas-uralkali": {
        "name": "ESPN, Haas terminates contracts with Nikita Mazepin and title sponsor Uralkali",
        "date": "2022-03-05",
        "url": "https://www.espn.com/f1/story/_/id/33419710/haas-terminates-contracts-russian-driver-nikita-mazepin-title-sponsor-uralkali",
    },
    "sky-f1-russian-gp": {
        "name": "Sky Sports, Formula 1 terminates Russian GP contract",
        "date": "2022-03-03",
        "url": "https://www.skysports.com/f1/news/12433/12556381/formula-1-terminates-russian-gp-contract-in-wake-of-ukraine-invasion",
    },
}

# ---------------------------------------------------------------- sports / leagues
NEW_SPORTS = [
    {"id": "baseball", "label": "Baseball", "status": "not-mapped", "aliases": ["mlb"]},
]

NEW_LEAGUES = [
    {
        "id": "mlb",
        "aliases": ["major league baseball", "usa"],
        "sportId": "baseball",
        "name": "MLB",
        "country": "USA and Canada",
        "clubCount": 30,
        "season": "2026",
        "status": "not-started",
        "notes": [],
    },
    {
        "id": "2-bundesliga",
        "aliases": ["zweite bundesliga", "germany second division"],
        "sportId": "soccer",
        "name": "2. Bundesliga",
        "country": "Germany",
        "clubCount": 18,
        "season": "2026-27",
        "status": "not-started",
        "notes": [
            "VfL Wolfsburg was relegated in 2026 after 29 seasons in the Bundesliga.",
        ],
    },
]

# clubs: (id, name, shortName, code, sportId, leagueId, country)
def _c(*rows):
    out = []
    for r in rows:
        out.append(
            {
                "id": r[0],
                "name": r[1],
                "shortName": r[2],
                "code": r[3],
                "sportId": r[4],
                "leagueId": r[5],
                "country": r[6],
                "crest": None,
                "aliases": list(r[7]) if len(r) > 7 else [],
                "hasTeamPageDesign": False,
            }
        )
    return out


LA_LIGA = _c(
    ("athletic-club", "Athletic Club", "Athletic Club", "ATH", "soccer", "la-liga", "Spain", ["athletic bilbao", "bilbao"]),
    ("osasuna", "CA Osasuna", "Osasuna", "OSA", "soccer", "la-liga", "Spain", []),
    ("celta-vigo", "Celta Vigo", "Celta", "CEL", "soccer", "la-liga", "Spain", ["celta"]),
    ("deportivo-alaves", "Deportivo Alaves", "Alaves", "ALA", "soccer", "la-liga", "Spain", ["alaves"]),
    ("elche", "Elche CF", "Elche", "ELC", "soccer", "la-liga", "Spain", []),
    ("barcelona", "FC Barcelona", "Barcelona", "BAR", "soccer", "la-liga", "Spain", ["barca", "fcb"]),
    ("getafe", "Getafe CF", "Getafe", "GET", "soccer", "la-liga", "Spain", []),
    ("levante", "Levante UD", "Levante", "LEV", "soccer", "la-liga", "Spain", []),
    ("malaga", "Malaga CF", "Malaga", "MAL", "soccer", "la-liga", "Spain", []),
    ("racing-santander", "Racing Santander", "Racing", "RAC", "soccer", "la-liga", "Spain", ["racing"]),
    ("rayo-vallecano", "Rayo Vallecano", "Rayo", "RAY", "soccer", "la-liga", "Spain", ["rayo"]),
    ("deportivo-la-coruna", "Deportivo A Coruna", "Deportivo", "DEP", "soccer", "la-liga", "Spain", ["deportivo"]),
    ("espanyol", "RCD Espanyol", "Espanyol", "ESP", "soccer", "la-liga", "Spain", []),
    ("real-betis", "Real Betis", "Betis", "BET", "soccer", "la-liga", "Spain", []),
    ("real-sociedad", "Real Sociedad", "Real Sociedad", "RSO", "soccer", "la-liga", "Spain", ["la real"]),
    ("sevilla", "Sevilla FC", "Sevilla", "SEV", "soccer", "la-liga", "Spain", []),
    ("valencia", "Valencia CF", "Valencia", "VAL", "soccer", "la-liga", "Spain", []),
    ("villarreal", "Villarreal CF", "Villarreal", "VIL", "soccer", "la-liga", "Spain", []),
)

BUNDESLIGA = _c(
    ("fc-augsburg", "FC Augsburg", "Augsburg", "FCA", "soccer", "bundesliga", "Germany", []),
    ("union-berlin", "Union Berlin", "Union Berlin", "FCU", "soccer", "bundesliga", "Germany", []),
    ("werder-bremen", "Werder Bremen", "Werder", "SVW", "soccer", "bundesliga", "Germany", ["bremen"]),
    ("borussia-dortmund", "Borussia Dortmund", "Dortmund", "BVB", "soccer", "bundesliga", "Germany", ["bvb"]),
    ("sv-elversberg", "SV Elversberg", "Elversberg", "ELV", "soccer", "bundesliga", "Germany", []),
    ("eintracht-frankfurt", "Eintracht Frankfurt", "Frankfurt", "SGE", "soccer", "bundesliga", "Germany", ["sge"]),
    ("sc-freiburg", "SC Freiburg", "Freiburg", "SCF", "soccer", "bundesliga", "Germany", []),
    ("hamburger-sv", "Hamburger SV", "Hamburg", "HSV", "soccer", "bundesliga", "Germany", ["hsv"]),
    ("tsg-hoffenheim", "TSG Hoffenheim", "Hoffenheim", "TSG", "soccer", "bundesliga", "Germany", []),
    ("fc-koln", "1. FC Koeln", "Koeln", "KOE", "soccer", "bundesliga", "Germany", ["koln", "cologne"]),
    ("rb-leipzig", "RB Leipzig", "Leipzig", "RBL", "soccer", "bundesliga", "Germany", []),
    ("bayer-leverkusen", "Bayer Leverkusen", "Leverkusen", "B04", "soccer", "bundesliga", "Germany", ["leverkusen"]),
    ("mainz-05", "Mainz 05", "Mainz", "M05", "soccer", "bundesliga", "Germany", []),
    ("borussia-monchengladbach", "Borussia Moenchengladbach", "Gladbach", "BMG", "soccer", "bundesliga", "Germany", ["gladbach"]),
    ("sc-paderborn-07", "SC Paderborn", "Paderborn", "SCP", "soccer", "bundesliga", "Germany", []),
    ("vfb-stuttgart", "VfB Stuttgart", "Stuttgart", "VFB", "soccer", "bundesliga", "Germany", []),
)

ZWEITE = _c(
    ("vfl-wolfsburg", "VfL Wolfsburg", "Wolfsburg", "WOB", "soccer", "2-bundesliga", "Germany", []),
)

NBA = _c(
    ("atlanta-hawks", "Atlanta Hawks", "Hawks", "ATL", "basketball", "nba", "USA"),
    ("boston-celtics", "Boston Celtics", "Celtics", "BOS", "basketball", "nba", "USA"),
    ("brooklyn-nets", "Brooklyn Nets", "Nets", "BKN", "basketball", "nba", "USA"),
    ("charlotte-hornets", "Charlotte Hornets", "Hornets", "CHA", "basketball", "nba", "USA"),
    ("chicago-bulls", "Chicago Bulls", "Bulls", "CHI", "basketball", "nba", "USA"),
    ("cleveland-cavaliers", "Cleveland Cavaliers", "Cavaliers", "CLE", "basketball", "nba", "USA"),
    ("dallas-mavericks", "Dallas Mavericks", "Mavericks", "DAL", "basketball", "nba", "USA"),
    ("denver-nuggets", "Denver Nuggets", "Nuggets", "DEN", "basketball", "nba", "USA"),
    ("detroit-pistons", "Detroit Pistons", "Pistons", "DET", "basketball", "nba", "USA"),
    ("golden-state-warriors", "Golden State Warriors", "Warriors", "GSW", "basketball", "nba", "USA"),
    ("houston-rockets", "Houston Rockets", "Rockets", "HOU", "basketball", "nba", "USA"),
    ("indiana-pacers", "Indiana Pacers", "Pacers", "IND", "basketball", "nba", "USA"),
    ("los-angeles-lakers", "Los Angeles Lakers", "Lakers", "LAL", "basketball", "nba", "USA"),
    ("memphis-grizzlies", "Memphis Grizzlies", "Grizzlies", "MEM", "basketball", "nba", "USA"),
    ("miami-heat", "Miami Heat", "Heat", "MIA", "basketball", "nba", "USA"),
    ("milwaukee-bucks", "Milwaukee Bucks", "Bucks", "MIL", "basketball", "nba", "USA"),
    ("minnesota-timberwolves", "Minnesota Timberwolves", "Timberwolves", "MIN", "basketball", "nba", "USA"),
    ("new-orleans-pelicans", "New Orleans Pelicans", "Pelicans", "NOP", "basketball", "nba", "USA"),
    ("new-york-knicks", "New York Knicks", "Knicks", "NYK", "basketball", "nba", "USA"),
    ("oklahoma-city-thunder", "Oklahoma City Thunder", "Thunder", "OKC", "basketball", "nba", "USA"),
    ("orlando-magic", "Orlando Magic", "Magic", "ORL", "basketball", "nba", "USA"),
    ("philadelphia-76ers", "Philadelphia 76ers", "76ers", "PHI", "basketball", "nba", "USA"),
    ("phoenix-suns", "Phoenix Suns", "Suns", "PHX", "basketball", "nba", "USA"),
    ("portland-trail-blazers", "Portland Trail Blazers", "Trail Blazers", "POR", "basketball", "nba", "USA"),
    ("sacramento-kings", "Sacramento Kings", "Kings", "SAC", "basketball", "nba", "USA"),
    ("san-antonio-spurs", "San Antonio Spurs", "Spurs", "SAS", "basketball", "nba", "USA"),
    ("toronto-raptors", "Toronto Raptors", "Raptors", "TOR", "basketball", "nba", "Canada"),
    ("utah-jazz", "Utah Jazz", "Jazz", "UTA", "basketball", "nba", "USA"),
    ("washington-wizards", "Washington Wizards", "Wizards", "WAS", "basketball", "nba", "USA"),
)

NFL = _c(
    ("arizona-cardinals", "Arizona Cardinals", "Cardinals", "ARI", "american-football", "nfl", "USA"),
    ("atlanta-falcons", "Atlanta Falcons", "Falcons", "ATL", "american-football", "nfl", "USA"),
    ("baltimore-ravens", "Baltimore Ravens", "Ravens", "BAL", "american-football", "nfl", "USA"),
    ("buffalo-bills", "Buffalo Bills", "Bills", "BUF", "american-football", "nfl", "USA"),
    ("carolina-panthers", "Carolina Panthers", "Panthers", "CAR", "american-football", "nfl", "USA"),
    ("chicago-bears", "Chicago Bears", "Bears", "CHI", "american-football", "nfl", "USA"),
    ("cincinnati-bengals", "Cincinnati Bengals", "Bengals", "CIN", "american-football", "nfl", "USA"),
    ("cleveland-browns", "Cleveland Browns", "Browns", "CLE", "american-football", "nfl", "USA"),
    ("dallas-cowboys", "Dallas Cowboys", "Cowboys", "DAL", "american-football", "nfl", "USA"),
    ("denver-broncos", "Denver Broncos", "Broncos", "DEN", "american-football", "nfl", "USA"),
    ("detroit-lions", "Detroit Lions", "Lions", "DET", "american-football", "nfl", "USA"),
    ("green-bay-packers", "Green Bay Packers", "Packers", "GB", "american-football", "nfl", "USA"),
    ("houston-texans", "Houston Texans", "Texans", "HOU", "american-football", "nfl", "USA"),
    ("indianapolis-colts", "Indianapolis Colts", "Colts", "IND", "american-football", "nfl", "USA"),
    ("jacksonville-jaguars", "Jacksonville Jaguars", "Jaguars", "JAX", "american-football", "nfl", "USA"),
    ("kansas-city-chiefs", "Kansas City Chiefs", "Chiefs", "KC", "american-football", "nfl", "USA"),
    ("las-vegas-raiders", "Las Vegas Raiders", "Raiders", "LV", "american-football", "nfl", "USA"),
    ("los-angeles-chargers", "Los Angeles Chargers", "Chargers", "LAC", "american-football", "nfl", "USA"),
    ("miami-dolphins", "Miami Dolphins", "Dolphins", "MIA", "american-football", "nfl", "USA"),
    ("minnesota-vikings", "Minnesota Vikings", "Vikings", "MIN", "american-football", "nfl", "USA"),
    ("new-england-patriots", "New England Patriots", "Patriots", "NE", "american-football", "nfl", "USA"),
    ("new-orleans-saints", "New Orleans Saints", "Saints", "NO", "american-football", "nfl", "USA"),
    ("new-york-giants", "New York Giants", "Giants", "NYG", "american-football", "nfl", "USA"),
    ("new-york-jets", "New York Jets", "Jets", "NYJ", "american-football", "nfl", "USA"),
    ("philadelphia-eagles", "Philadelphia Eagles", "Eagles", "PHI", "american-football", "nfl", "USA"),
    ("pittsburgh-steelers", "Pittsburgh Steelers", "Steelers", "PIT", "american-football", "nfl", "USA"),
    ("san-francisco-49ers", "San Francisco 49ers", "49ers", "SF", "american-football", "nfl", "USA"),
    ("seattle-seahawks", "Seattle Seahawks", "Seahawks", "SEA", "american-football", "nfl", "USA"),
    ("tampa-bay-buccaneers", "Tampa Bay Buccaneers", "Buccaneers", "TB", "american-football", "nfl", "USA"),
    ("tennessee-titans", "Tennessee Titans", "Titans", "TEN", "american-football", "nfl", "USA"),
    ("washington-commanders", "Washington Commanders", "Commanders", "WAS", "american-football", "nfl", "USA"),
)

MLB = _c(
    ("arizona-diamondbacks", "Arizona Diamondbacks", "Diamondbacks", "ARI", "baseball", "mlb", "USA"),
    ("athletics", "Athletics", "Athletics", "ATH", "baseball", "mlb", "USA", ["a's", "oakland athletics"]),
    ("atlanta-braves", "Atlanta Braves", "Braves", "ATL", "baseball", "mlb", "USA"),
    ("baltimore-orioles", "Baltimore Orioles", "Orioles", "BAL", "baseball", "mlb", "USA"),
    ("boston-red-sox", "Boston Red Sox", "Red Sox", "BOS", "baseball", "mlb", "USA"),
    ("chicago-cubs", "Chicago Cubs", "Cubs", "CHC", "baseball", "mlb", "USA"),
    ("chicago-white-sox", "Chicago White Sox", "White Sox", "CWS", "baseball", "mlb", "USA"),
    ("cincinnati-reds", "Cincinnati Reds", "Reds", "CIN", "baseball", "mlb", "USA"),
    ("cleveland-guardians", "Cleveland Guardians", "Guardians", "CLE", "baseball", "mlb", "USA"),
    ("colorado-rockies", "Colorado Rockies", "Rockies", "COL", "baseball", "mlb", "USA"),
    ("detroit-tigers", "Detroit Tigers", "Tigers", "DET", "baseball", "mlb", "USA"),
    ("houston-astros", "Houston Astros", "Astros", "HOU", "baseball", "mlb", "USA"),
    ("kansas-city-royals", "Kansas City Royals", "Royals", "KC", "baseball", "mlb", "USA"),
    ("los-angeles-angels", "Los Angeles Angels", "Angels", "LAA", "baseball", "mlb", "USA"),
    ("los-angeles-dodgers", "Los Angeles Dodgers", "Dodgers", "LAD", "baseball", "mlb", "USA"),
    ("miami-marlins", "Miami Marlins", "Marlins", "MIA", "baseball", "mlb", "USA"),
    ("milwaukee-brewers", "Milwaukee Brewers", "Brewers", "MIL", "baseball", "mlb", "USA"),
    ("minnesota-twins", "Minnesota Twins", "Twins", "MIN", "baseball", "mlb", "USA"),
    ("new-york-mets", "New York Mets", "Mets", "NYM", "baseball", "mlb", "USA"),
    ("new-york-yankees", "New York Yankees", "Yankees", "NYY", "baseball", "mlb", "USA"),
    ("philadelphia-phillies", "Philadelphia Phillies", "Phillies", "PHI", "baseball", "mlb", "USA"),
    ("pittsburgh-pirates", "Pittsburgh Pirates", "Pirates", "PIT", "baseball", "mlb", "USA"),
    ("san-diego-padres", "San Diego Padres", "Padres", "SD", "baseball", "mlb", "USA"),
    ("san-francisco-giants", "San Francisco Giants", "Giants", "SF", "baseball", "mlb", "USA"),
    ("seattle-mariners", "Seattle Mariners", "Mariners", "SEA", "baseball", "mlb", "USA"),
    ("st-louis-cardinals", "St. Louis Cardinals", "Cardinals", "STL", "baseball", "mlb", "USA"),
    ("tampa-bay-rays", "Tampa Bay Rays", "Rays", "TB", "baseball", "mlb", "USA"),
    ("texas-rangers", "Texas Rangers", "Rangers", "TEX", "baseball", "mlb", "USA"),
    ("toronto-blue-jays", "Toronto Blue Jays", "Blue Jays", "TOR", "baseball", "mlb", "Canada"),
    ("washington-nationals", "Washington Nationals", "Nationals", "WAS", "baseball", "mlb", "USA"),
)

NEW_CLUBS = LA_LIGA + BUNDESLIGA + ZWEITE + NBA + NFL + MLB


def _o(oid, name, otype, country, parent=None, via=None, note=None):
    d = {"id": oid, "name": name, "type": otype, "parentId": parent}
    if country:
        d["country"] = country
    if via:
        d["via"] = via
    if note:
        d["note"] = note
    return d


# owner chains for the new front sponsors (owners are entities, not page facts)
NEW_OWNERS = [
    _o("3m-company", "3M Company", "listed-company", "USA"),
    _o("blockratize", "Blockratize, Inc. (dba Polymarket)", "private-company", "USA"),
    _o("recruit-holdings", "Recruit Holdings", "listed-company", "Japan"),
    _o("indeed-inc", "Indeed, Inc.", "private-company", "USA", parent="recruit-holdings"),
    _o("deutsche-telekom-ag", "Deutsche Telekom AG", "listed-company", "Germany"),
    _o("vodafone-group", "Vodafone Group", "listed-company", "United Kingdom"),
    _o("red-bull-gmbh", "Red Bull GmbH", "private-company", "Austria"),
    _o("barmenia-versicherungen", "Barmenia Versicherungen", "private-company", "Germany"),
    _o("koemmerling-kunststoffe", "Koemmerling Kunststoffe", "private-company", "Germany"),
    _o("ursapharm", "URSAPHARM Arzneimittel", "private-company", "Germany"),
    _o("sap-se", "SAP SE", "listed-company", "Germany"),
    _o("lexware-gmbh", "Lexware (Haufe Group)", "private-company", "Germany"),
    _o("wwk-versicherungen", "WWK Versicherungen", "private-company", "Germany"),
    _o("raisin-ds", "Raisin DS", "private-company", "Germany"),
    _o("matthaei-bau", "Matthaei Bauunternehmung", "private-company", "Germany"),
    _o("land-baden-wuerttemberg", "State of Baden-Wuerttemberg", "state", "Germany"),
    _o("lbbw", "Landesbank Baden-Wuerttemberg", "listed-company", "Germany", via="Land Baden-Wuerttemberg"),
    _o("c-hedenkamp", "C. Hedenkamp GmbH", "private-company", "Germany"),
    _o("beumer-group", "BEUMER Group", "private-company", "Germany"),
    _o("rewe-group", "REWE Group", "private-company", "Germany"),
    _o("reuter-gruppe", "Reuter Gruppe", "private-company", "Germany"),
    _o("hansemerkur", "HanseMerkur Versicherungsgruppe", "private-company", "Germany"),
    _o("spotify-technology", "Spotify Technology S.A.", "listed-company", "Sweden"),
    _o("kutxabank", "Kutxabank", "private-company", "Spain"),
    _o("kosner", "Kosner", "private-company", "Spain"),
    _o("estrella-galicia", "Hijos de Rivera (Estrella Galicia)", "private-company", "Spain"),
    _o("mk-tiyu-news", "MK TIYU News", "private-company", "China"),
    _o("flexicar", "Flexicar", "private-company", "Spain"),
    _o("tecnocasa-group", "Tecnocasa Group", "private-company", "Italy"),
    _o("sesame-hr", "Sesame HR", "private-company", "Spain"),
    _o("sabor-a-malaga", "Sabor a Malaga", "private-company", "Spain"),
    _o("plenitude-eni", "Plenitude (Eni)", "listed-company", "Italy"),
    _o("digi-communications", "Digi Communications", "listed-company", "Romania"),
    _o("arctempus", "Arctempus", "private-company", "Spain"),
    _o("gree-electric", "Gree Electric Appliances", "listed-company", "China"),
    _o("baghdadi-capital", "Baghdadi Capital", "private-company", "Spain"),
    _o("fundacion-1890", "Fundacion 1890", "private-company", "Spain"),
    _o("tm-real-estate-group", "TM Real Estate Group", "private-company", "Spain"),
    _o("pamesa-ceramica", "Pamesa Ceramica", "private-company", "Spain"),
    _o("circle-internet-group", "Circle Internet Group", "listed-company", "USA"),
    _o("corendon-airlines", "Corendon Airlines", "private-company", "Turkey"),
    _o("halo-service-management", "Halo Service Solutions", "private-company", "United Kingdom"),
]


def _s(sid, name, owner, ownership, aliases=None, note=None):
    d = {
        "id": sid,
        "name": name,
        "ownerId": owner,
        "ownership": ownership,
        "tier": "unrated",
        "status": "unrated",
        "verdict": None,
        "claimIds": [],
        "aliases": aliases or [],
    }
    if note:
        d["note"] = note
    return d


NEW_SPONSORS = [
    _s("3m", "3M", "3m-company", "owned", note="Cadillac F1 team partner."),
    _s("polymarket", "Polymarket", "blockratize", "owned",
       note="Crypto prediction market. Not an ADM-licensed operator in Italy, so the Lazio deal is branded on its information site."),
    # Bundesliga 2026/27 fronts
    _s("deutsche-telekom", "Deutsche Telekom", "deutsche-telekom-ag", "owned", ["telekom", "t-mobile"]),
    _s("vodafone", "Vodafone", "vodafone-group", "owned"),
    _s("red-bull", "Red Bull", "red-bull-gmbh", "owned"),
    _s("indeed", "Indeed", "indeed-inc", "owned"),
    _s("barmenia", "Barmenia", "barmenia-versicherungen", "owned"),
    _s("koemmerling", "Koemmerling", "koemmerling-kunststoffe", "owned"),
    _s("hylo", "HYLO", "ursapharm", "owned", note="Eye-drop brand of URSAPHARM"),
    _s("sap", "SAP", "sap-se", "owned"),
    _s("lexware", "Lexware", "lexware-gmbh", "owned"),
    _s("wwk", "WWK", "wwk-versicherungen", "owned"),
    _s("raisin", "Raisin", "raisin-ds", "owned"),
    _s("matthaei", "Matthaei", "matthaei-bau", "owned"),
    _s("lbbw", "LBBW", "lbbw", "part-owned", note="Landesbank Baden-Wuerttemberg, part-owned by the state of Baden-Wuerttemberg"),
    _s("c-hedenkamp", "C. Hedenkamp", "c-hedenkamp", "owned"),
    _s("beumer-group", "BEUMER Group", "beumer-group", "owned"),
    _s("rewe", "REWE", "rewe-group", "owned"),
    _s("reuter", "Reuter", "reuter-gruppe", "owned"),
    _s("hansemerkur", "HanseMerkur", "hansemerkur", "owned"),
    # La Liga 2026/27 fronts
    _s("spotify", "Spotify", "spotify-technology", "owned"),
    _s("kutxabank", "Kutxabank", "kutxabank", "owned"),
    _s("kosner", "Kosner", "kosner", "owned"),
    _s("estrella-galicia", "Estrella Galicia", "estrella-galicia", "owned"),
    _s("mk-tiyu-news", "MK TIYU News", "mk-tiyu-news", "owned"),
    _s("flexicar", "Flexicar", "flexicar", "owned"),
    _s("tecnocasa-group", "Tecnocasa Group", "tecnocasa-group", "owned"),
    _s("sesame-hr", "Sesame HR", "sesame-hr", "owned"),
    _s("sabor-a-malaga", "Sabor a Malaga", "sabor-a-malaga", "owned"),
    _s("plenitude", "Plenitude", "plenitude-eni", "owned", note="Energy arm of Eni"),
    _s("digi", "Digi", "digi-communications", "owned"),
    _s("arctempus", "Arctempus", "arctempus", "owned"),
    _s("gree", "Gree", "gree-electric", "owned"),
    _s("baghdadi-capital", "Baghdadi Capital", "baghdadi-capital", "owned"),
    _s("fundacion-1890", "Fundacion 1890", "fundacion-1890", "owned", note="Sevilla charity, named for the club's founding year"),
    _s("tm-real-estate-group", "TM Real Estate Group", "tm-real-estate-group", "owned"),
    _s("pamesa-ceramica", "Pamesa Ceramica", "pamesa-ceramica", "owned"),
    # Premier League 2026/27 fronts the seed did not carry
    _s("circle-usdc", "USDC (Circle)", "circle-internet-group", "owned", ["usdc", "circle"]),
    _s("corendon", "Corendon", "corendon-airlines", "owned"),
    _s("halo", "Halo", "halo-service-management", "owned"),
]

# (clubId, sponsorId) 2026-27 home fronts, and the source to cite for the shirt
FRONTS = [
    # La Liga
    ("athletic-club", "kutxabank", "scoreandchange-la-liga"),
    ("osasuna", "kosner", "scoreandchange-la-liga"),
    ("celta-vigo", "estrella-galicia", "scoreandchange-la-liga"),
    ("deportivo-alaves", "mk-tiyu-news", "scoreandchange-la-liga"),
    ("elche", "flexicar", "scoreandchange-la-liga"),
    ("barcelona", "spotify", "scoreandchange-la-liga"),
    ("getafe", "tecnocasa-group", "scoreandchange-la-liga"),
    ("levante", "sesame-hr", "scoreandchange-la-liga"),
    ("malaga", "sabor-a-malaga", "scoreandchange-la-liga"),
    ("racing-santander", "plenitude", "scoreandchange-la-liga"),
    ("rayo-vallecano", "digi", "scoreandchange-la-liga"),
    ("deportivo-la-coruna", "estrella-galicia", "scoreandchange-la-liga"),
    ("espanyol", "arctempus", "scoreandchange-la-liga"),
    ("real-betis", "gree", "scoreandchange-la-liga"),
    ("real-sociedad", "baghdadi-capital", "scoreandchange-la-liga"),
    ("sevilla", "fundacion-1890", "scoreandchange-la-liga"),
    ("valencia", "tm-real-estate-group", "scoreandchange-la-liga"),
    ("villarreal", "pamesa-ceramica", "scoreandchange-la-liga"),
    # Bundesliga
    ("fc-augsburg", "wwk", "marketinginstitut"),
    ("union-berlin", "raisin", "marketinginstitut"),
    ("werder-bremen", "matthaei", "marketinginstitut"),
    ("borussia-dortmund", "vodafone", "marketinginstitut"),
    ("sv-elversberg", "reuter", "footballkitarchive"),
    ("eintracht-frankfurt", "indeed", "footballkitarchive"),
    ("sc-freiburg", "lexware", "marketinginstitut"),
    ("hamburger-sv", "hansemerkur", "marketinginstitut"),
    ("tsg-hoffenheim", "sap", "marketinginstitut"),
    ("fc-koln", "rewe", "marketinginstitut"),
    ("rb-leipzig", "red-bull", "marketinginstitut"),
    ("bayer-leverkusen", "barmenia", "footballkitarchive"),
    ("mainz-05", "koemmerling", "footballkitarchive"),
    ("borussia-monchengladbach", "hylo", "footballkitarchive"),
    ("sc-paderborn-07", "c-hedenkamp", "marketinginstitut"),
    ("vfb-stuttgart", "lbbw", "marketinginstitut"),
    ("bayern-munich", "deutsche-telekom", "marketinginstitut"),
    ("schalke-04", "beumer-group", "marketinginstitut"),
]

# deals worth recording with a value, or with a named source for an undisclosed one
# (clubId, sponsorId, placement, from, to, value-or-None, sourceKey, note)
NEW_DEALS = [
    ("barcelona", "spotify", "front", "2022-23", "2029-30",
     {"amount": 65, "currency": "EUR", "unit": "m", "per": "year", "upTo": False, "usdApprox": 75},
     "sportspro-barca-spotify",
     "Reported EUR65m a year for the shirt plus training wear and naming rights."),
    ("bayern-munich", "deutsche-telekom", "front", None, "2028-29",
     {"amount": 60, "currency": "EUR", "unit": "m", "per": "year", "upTo": True, "usdApprox": 69},
     "marketinginstitut", "Reported EUR60-65m a season, the club's largest single deal."),
    ("borussia-dortmund", "vodafone", "front", "2025-26", "2029-30",
     {"amount": 30, "currency": "EUR", "unit": "m", "per": "year", "upTo": False, "usdApprox": 34},
     "marketinginstitut", "Five-year deal to 2030; replaces the 1&1 (league) and Evonik (cup) split."),
    ("rb-leipzig", "red-bull", "front", None, None,
     {"amount": 35, "currency": "EUR", "unit": "m", "per": "year", "upTo": False, "usdApprox": 40},
     "marketinginstitut", "Red Bull owns 99% of the club's football company."),
    ("werder-bremen", "matthaei", "front", "2023-24", None,
     {"amount": 7, "currency": "EUR", "unit": "m", "per": "year", "upTo": True, "usdApprox": 8},
     "marketinginstitut", None),
    ("fc-augsburg", "wwk", "front", None, None,
     {"amount": 4, "currency": "EUR", "unit": "m", "per": "year", "upTo": True, "usdApprox": 5},
     "marketinginstitut", "Also holds the naming rights to the WWK Arena."),
    ("schalke-04", "beumer-group", "front", "2026-27", "2028-29",
     {"amount": 3.5, "currency": "EUR", "unit": "m", "per": "year", "upTo": True, "usdApprox": 4},
     "marketinginstitut", "Three seasons, independent of the division."),
    ("tsg-hoffenheim", "sap", "front", None, None,
     {"amount": 6, "currency": "EUR", "unit": "m", "per": "year", "upTo": True, "usdApprox": 7},
     "marketinginstitut", "Unofficial figure; SAP co-founder Dietmar Hopp is the club's patron."),
    ("eintracht-frankfurt", "indeed", "front", None, "2028-29",
     {"amount": 13, "currency": "EUR", "unit": "m", "per": "year", "upTo": True, "usdApprox": 15},
     "marketinginstitut", "Extended three seasons to 2029; reported volume about EUR40m."),
]

# undisclosed La Liga / Bundesliga fronts still get a record with a source
UNDISCLOSED_DEALS = [
    ("osasuna", "kosner", "scoreandchange-la-liga"),
    ("celta-vigo", "estrella-galicia", "scoreandchange-la-liga"),
    ("deportivo-alaves", "mk-tiyu-news", "scoreandchange-la-liga"),
    ("elche", "flexicar", "scoreandchange-la-liga"),
    ("getafe", "tecnocasa-group", "scoreandchange-la-liga"),
    ("levante", "sesame-hr", "scoreandchange-la-liga"),
    ("malaga", "sabor-a-malaga", "scoreandchange-la-liga"),
    ("racing-santander", "plenitude", "scoreandchange-la-liga"),
    ("rayo-vallecano", "digi", "scoreandchange-la-liga"),
    ("deportivo-la-coruna", "estrella-galicia", "scoreandchange-la-liga"),
    ("espanyol", "arctempus", "scoreandchange-la-liga"),
    ("real-betis", "gree", "scoreandchange-la-liga"),
    ("real-sociedad", "baghdadi-capital", "scoreandchange-la-liga"),
    ("valencia", "tm-real-estate-group", "scoreandchange-la-liga"),
    ("villarreal", "pamesa-ceramica", "scoreandchange-la-liga"),
    ("union-berlin", "raisin", "marketinginstitut"),
    ("sv-elversberg", "reuter", "footballkitarchive"),
    ("sc-freiburg", "lexware", "marketinginstitut"),
    ("hamburger-sv", "hansemerkur", "marketinginstitut"),
    ("fc-koln", "rewe", "marketinginstitut"),
    ("bayer-leverkusen", "barmenia", "footballkitarchive"),
    ("mainz-05", "koemmerling", "footballkitarchive"),
    ("borussia-monchengladbach", "hylo", "footballkitarchive"),
    ("sc-paderborn-07", "c-hedenkamp", "marketinginstitut"),
    ("vfb-stuttgart", "lbbw", "marketinginstitut"),
    # Premier League fronts recorded from the 2026/27 sponsor overview
    ("manchester-united", "snapdragon", "front", None, "2029-30",
     {"amount": 60, "currency": "GBP", "unit": "m", "per": "year", "upTo": False, "usdApprox": 80},
     "sportspro-snapdragon", "Reported GBP60m a year, among the largest shirt deals in the league."),
    ("chelsea", "circle-usdc", "front", None, None, None, "scoreandchange-pl",
     "USDC stablecoin branding; replaces the front that had been vacant."),
    ("hull-city", "corendon", "front", None, None, None, "scoreandchange-pl", None),
    ("ipswich-town", "halo", "front", None, None, None, "scoreandchange-pl", None),
    ("leeds-united", "red-bull", "front", None, None, None, "scoreandchange-pl", None),
]

# ---------------------------------------------------------------- claims / sources
CLAIM_URLS = {
    "rwanda-troops-m23": ("https://docs.un.org/en/S/2024/432", "Final report of the UN Group of Experts on the DR Congo, S/2024/432."),
    "m23-coltan-levies": ("https://docs.un.org/en/S/2024/432", "Final report of the UN Group of Experts on the DR Congo, S/2024/432."),
    "rubaya-smuggling": ("https://globalwitness.org/en/campaigns/transition-minerals/who-buys-rwandas-smuggled-coltan-the-global-journey-of-conflict-coltan-from-drc-to-the-worlds-electronics/", "Who buys Rwanda's smuggled coltan?"),
    "rubaya-tantalum-share": ("https://globalwitness.org/en/campaigns/transition-minerals/who-buys-rwandas-smuggled-coltan-the-global-journey-of-conflict-coltan-from-drc-to-the-worlds-electronics/", "Who buys Rwanda's smuggled coltan?"),
    "coltan-supply-chain": ("https://globalwitness.org/en/campaigns/transition-minerals/who-buys-rwandas-smuggled-coltan-the-global-journey-of-conflict-coltan-from-drc-to-the-worlds-electronics/", "Who buys Rwanda's smuggled coltan?"),
    "saudi-executions-2024": ("https://www.amnesty.org/en/documents/act50/8800/2025/en/", "Death Sentences and Executions 2024."),
    "khashoggi-assessment": ("https://www.dni.gov/files/ODNI/documents/assessments/Assessment-Saudi-Gov-Role-in-JK-Death-20210226v2.pdf", "Declassified assessment, 26 Feb 2021."),
    "uae-mass-trial-2024": ("https://www.hrw.org/news/2024/07/10/uae-unfair-trial-unjust-sentences", "Abu Dhabi Federal Appeals Court, 10 July 2024."),
}

# extra, Abu Dhabi-specific evidence for Etihad (requested double-check)
EXTRA_CLAIMS = [
    {
        "id": "uae-mass-trial-upheld-2025",
        "ownerIds": ["uae", "government-of-abu-dhabi", "government-of-dubai"],
        "text": "The UAE's Federal Supreme Court upheld the mass-trial convictions in March 2025.",
        "short": "Mass-trial convictions upheld on appeal in March 2025",
        "source": {
            "name": "Human Rights Watch",
            "date": "2025-03-04",
            "url": "https://www.hrw.org/news/2025/03/04/uae-unfair-mass-trial-convictions-upheld",
        },
        "reviewed": False,
    },
]

DROPPED_SOURCES = {
    "bayern-visit-rwanda-2025": {
        "name": "Deutsche Welle, Bayern Munich end Rwanda sponsorship after pressure",
        "date": "2025-08",
        "url": "https://www.dw.com/en/bayern-munich-end-rwanda-sponsorship-after-pressure/a-73574184",
        "note": "The club ended the commercial deal with the Rwanda Development Board after fan and media pressure.",
    },
    "bayern-qatar-airways-2023": {
        "name": "Deutsche Welle, Bayern Munich end Qatar deal after fan pressure",
        "date": "2023",
        "url": "https://www.dw.com/en/football-bayern-munich-end-qatar-deal-after-fan-pressure/a-63418536",
        "note": "Deal ended by mutual agreement on 30 June 2023 after five years.",
    },
    "schalke-gazprom-2022": {
        "name": "RFE/RL",
        "date": "2022-03",
        "url": "https://www.rferl.org/a/gazprom-uefa-ferencvaros-hungary-soccer-ukraine-war-schalke/32941442.html",
        "note": "Schalke cut ties at the same time as UEFA, ending a 15-year front-of-shirt deal.",
    },
    "manutd-aeroflot-2022": {
        "name": "ESPN",
        "date": "2022-02-25",
        "url": "https://www.espn.com/soccer/story/_/id/37625797/man-united-cut-sponsorship-russian-airline-aeroflot-amid-ukraine-invasion",
        "note": "United withdrew Aeroflot's sponsorship rights and said it shared fans' concerns.",
    },
    "wwc-visit-saudi-2023": {
        "name": "The Guardian, FIFA admits defeat over Saudi sponsorship of Women's World Cup",
        "date": "2023-03-16",
        "url": "https://www.theguardian.com/football/2023/mar/16/fifa-defeat-saudi-sponsorship-womens-world-cup-plans-infantino",
    },
    "uefa-gazprom-2022": {
        "name": "The Athletic, UEFA ends partnership with Gazprom",
        "date": "2022-02-28",
        "url": "https://www.nytimes.com/athletic/4181788/2022/02/28/uefa-ends-partnership-with-russian-energy-company-gazprom/",
    },
    "haas-uralkali-2022": {
        "name": "ESPN, Haas terminates contracts with Mazepin and Uralkali",
        "date": "2022-03-05",
        "url": "https://www.espn.com/f1/story/_/id/33419710/haas-terminates-contracts-russian-driver-nikita-mazepin-title-sponsor-uralkali",
    },
    "f1-russian-gp-2022": {
        "name": "Sky Sports, Formula 1 terminates Russian GP contract",
        "date": "2022-03-03",
        "url": "https://www.skysports.com/f1/news/12433/12556381/formula-1-terminates-russian-gp-contract-in-wake-of-ukraine-invasion",
    },
}

# Premier League 2026/27 fronts the seed did not have (Score and Change, 17 Sep 2026)
PL_FILL = {
    "chelsea": "circle-usdc",
    "hull-city": "corendon",
    "ipswich-town": "halo",
    "leeds-united": "red-bull",
}

PL_FILL_SOURCE = {
    "name": "Score and Change, Overview of the 2026/2027 Premier League sponsors",
    "date": "2026-09-17",
    "url": "https://www.scoreandchange.com/overview-of-the-2026-2027-premier-league-sponsors/",
}

# real, dated events worth a timeline entry (seed's own six are kept as-is)
EXTRA_CHANGES = [
    {
        "id": "2026-09-17-chelsea-circle-usdc",
        "date": "2026-09-17",
        "datePrecision": "day",
        "clubId": "chelsea",
        "sponsorId": "circle-usdc",
        "kind": "new",
        "levelAfter": "not-rated",
        "title": "Finally fills the empty front",
        "text": ("Chelsea started the season with no front-of-shirt sponsor and have now put "
                 "Circle's USDC on it. Not rated yet."),
        "source": PL_FILL_SOURCE,
    },
]

# ---------------------------------------------------------------------------
# Orphan kits: shirt images the website holds that no kit pointed at.
# ---------------------------------------------------------------------------
ORPHAN_KITS = [
    {
        "id": "bayern-munich-2022-23-home",
        "clubId": "bayern-munich",
        "season": "2022-23",
        "kitType": "home",
        "periodLabel": "2022-23",
        "periodFrom": "2022",
        "periodTo": "2023",
        "photos": {},
        "sponsors": [{
            "sponsorId": "deutsche-telekom",
            "placement": "front",
            "source": {
                "name": "Footy Headlines, FC Bayern 2022-23 home kit",
                "date": "2022-03-01",
                "url": "https://www.bavarianfootballworks.com/2022/3/1/22954757/bayern-munich-kit-leak-deutsche-telekom-sponsor-logo-change-bundesliga-pokal-champions-league",
            },
        }],
        "sponsorsComplete": False,
        "summary": "Telekom's long run on the Bayern front, in the season the logo changed.",
        "change": None,
    },
    {
        "id": "schalke-04-2021-22-home",
        "clubId": "schalke-04",
        "season": "2021-22",
        "kitType": "home",
        "periodLabel": "2021-22",
        "periodFrom": "2021",
        "periodTo": "2022",
        "photos": {},
        "sponsors": [{
            "sponsorId": "gazprom",
            "placement": "front",
            "source": {
                "name": "Footy Headlines, Schalke 04 21-22 home kit released",
                "date": "2021-07-02",
                "url": "https://www.footyheadlines.com/2021/06/schalke-04-21-22-kit.html",
            },
        }],
        "sponsorsComplete": False,
        "summary": "The last Schalke shirt launched with Gazprom on the front.",
        "change": {
            "kind": "better",
            "text": "Gazprom came off mid-season after 15 years, foiled over by the housing "
                    "company Vivawest in March 2022.",
            "badge": "Gazprom gone",
        },
    },
]

# Gazprom leaving Schalke mid-shirt: real, dated, sourced.
ORPHAN_CHANGES = [
    {
        "id": "2022-03-05-schalke-vivawest",
        "date": "2022-03-05",
        "datePrecision": "day",
        "clubId": "schalke-04",
        "sponsorId": "gazprom",
        "kind": "better",
        "levelAfter": "not-rated",
        "title": "Schalke foiled over Gazprom mid-season",
        "text": "Schalke ended a 15-year Gazprom deal days after the invasion of Ukraine and "
                "covered the logo with Vivawest, initially a deal to the end of the season.",
        "source": {
            "name": "FC Schalke 04, VIVAWEST become new partner",
            "date": "2022-03-05",
            "url": "https://schalke04.de/en/partner-en/vivawest-become-new-partner-fc-schalke-04",
        },
    },
]

# The seed rated American Express 'none' but left it with no claim, so it was the
# one rated sponsor with nothing behind it. Give it the ownership check.
SEED_CLAIMS = [
    {
        "id": "amex-listed-no-state",
        "ownerIds": ["american-express-company"],
        "text": "American Express Company is a NYSE-listed bank holding company; its "
                "shareholder register is institutional and free float with no state or "
                "state-fund holder.",
        "short": "A listed US company with no state shareholder.",
        "source": {
            "name": "American Express investor relations, stock information",
            "date": "2026",
            "url": "https://ir.americanexpress.com/stock-information",
        },
        "reviewed": False,
    },
]
SEED_CLAIM_FIX = {"american-express": ["amex-listed-no-state"]}
