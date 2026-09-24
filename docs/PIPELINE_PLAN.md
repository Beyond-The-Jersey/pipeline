# Behind The Jersey — Data Pipeline Plan

## How we collect, ascertain quality, and build JSON files

Inspired by the collection and parsing methods of:
- **surveillancewatch.io** — interactive map revealing connections between surveillance companies, funding sources, and affiliations
- **pushtoleave.org** — barcode scanning app that checks if brands are still active in Russia, with user-contributed data and KSE grade rating system

---

## Step 1: Data Collection

### 1.1 Sources (in priority order)

| Source | What we get | Method | Quality |
|---|---|---|---|
| Official league sites | Team lists, sponsor logos | Web scrape + API | High |
| Wikipedia | Owner, sponsor history | Structured parsing | Medium (scrutinized) |
| Wikidata | Owner relationships, structured data | SPARQL queries | Medium (cross-checked) |
| Team official sites | Contact info, sponsor pages | Web scrape | High |
| News archives | Deal announcements, changes | RSS + search | Medium |
| Community submissions | User-reported deals, corrections | GitHub issues | Varies |

### 1.2 Collection Pipeline

```
collect_data.py → verify_quality.py → build_json.py → verified_data/
```

1. **collect_data.py** — Fetches official league data + Wikipedia enrichment
2. **verify_quality.py** — Validates JSON schema, checks for missing fields
3. **build_json.py** — Assembles final JSON files with sponsor/owner data
4. **update_sponsors.py** — Back-fills sponsor/owner data from cached Wikipedia

### 1.3 Collection Frequency

- **Daily:** Check for sponsor changes (deal announcements, terminations)
- **Weekly:** Full pipeline run, verification, push to GitHub
- **Monthly:** Quality audit, source cross-check, update Wikidata mappings

---

## Step 2: Quality Assurance

### 2.1 Validation Checks

Every JSON file must pass these checks before going live:

| Check | Method | Pass Criteria |
|---|---|---|
| Schema validation | verify_quality.py | All required fields present |
| Sponsor accuracy | Cross-check against 2+ sources | Match at least 2 sources |
| Owner accuracy | Wikidata + Wikipedia + official site | Match at least 1 source |
| Contact info | Team official site + league site | Phone or email present |
| Deal value | Press reports | Source cited, date stamped |
| Regime flag | Authoritarian regime list | Flagged if sponsor from regime |

### 2.2 Scrutiny Rules (Wikipedia Data)

Wikipedia-sourced data gets **extra scrutiny**:
- Every claim must have a source cited
- Owner names must match official records
- Sponsor deals must be verified against press reports
- Contradictory data flagged for manual review
- "Not rated yet" if sources conflict

### 2.3 Evidence Format

One evidence file per claim:

```json
{
  "club": "aston-villa",
  "season": "2026/27",
  "sponsor": "Visit Rwanda",
  "placement": "front",
  "owner": "Government of Rwanda",
  "value": "up to £20m a year",
  "sources": ["sportspro.com/..."],
  "verified": true,
  "last_checked": "2026-09-24"
}
```

### 2.4 Rating Method (from Beyond-The-Jersey/data#1)

The website defines the rating method. **We don't publish club levels** — the website derives them.

| Tier | Definition |
|---|---|
| **unrated** | Not yet researched — owner chain and claims not sourced |
| **none** | No human-rights concern found |
| **concern** | Lesser link (state-part-owned sponsor) |
| **serious** | Serious human-rights concern (state-owned sponsor, exec order, sanctions) |
| **severe** | Severe concern (regime sponsor, mass executions, Khashoggi, M23 troops) |

**Rules:**
- Tiers, not grades. Don't map A–F onto tiers.
- A sponsor stays `unrated` until owner chain and claims are sourced and reviewed
- The website derives each club's blood level (Clean/Spotted/Stained/Soaked) from sponsors' tiers and placements
- Never publish club levels — only the website does that
- Wikipedia and Wikidata are leads, not sources — cite the primary document

**The 8 claims the ratings rest on:**
1. `rwanda-troops-m23` — UN Group of Experts on DR Congo, final report 2024
2. `m23-coltan-levies` — UN Group of Experts on DR Congo, final report 2024
3. `rubaya-smuggling` — Global Witness, June 2026
4. `rubaya-tantalum-share` — Global Witness, June 2026
5. `coltan-supply-chain` — Global Witness, June 2026
6. `saudi-executions-2024` — Amnesty International, 2025
7. `khashoggi-assessment` — US ODNI, February 2021
8. `uae-mass-trial-2024` — Human Rights Watch, July 2024

---

## Step 3: JSON File Structure

### 3.1 Team JSON Schema

```json
{
  "team": "aston-villa",
  "name": "Aston Villa",
  "sport": "soccer",
  "league": "premier_league",
  "country": "England",
  "owner": "Nassef Sawiris & Wes Edens",
  "alternate_owners": [],
  "regime_sponsors": [
    {
      "name": "Visit Rwanda",
      "regime": "Rwanda",
      "regime_type": "authoritarian",
      "placement": "front"
    }
  ],
  "sponsors": [
    {
      "name": "Visit Rwanda",
      "type": "company",
      "category": "shirt_sponsor",
      "placement": "front",
      "rating": "Severe",
      "rating_desc": "Government of Rwanda, UN experts say 3,000-4,000 troops fighting alongside M23 rebels",
      "flags": ["regime:rwanda", "authoritarian"],
      "deal_value": "up to £20m a year",
      "sources": ["sportspro.com/..."],
      "verified": true,
      "last_updated": "2026-09-24"
    }
  ],
  "contact": {
    "email": "info@avfc.co.uk",
    "phone": "+44 800 XXX XXXX",
    "website": "https://www.avfc.co.uk",
    "social": {"twitter": "@AVFC", "instagram": "@avfc"}
  },
  "blood_level": "Soaked",
  "blood_meter": 4,
  "last_updated": "2026-09-24"
}
```

### 3.2 Shame/Contact Field

Each team JSON includes contact info for fans to express discomfort:

```json
"contact": {
  "email": "info@avfc.co.uk",
  "phone": "+44 800 XXX XXXX",
  "website": "https://www.avfc.co.uk",
  "social": {"twitter": "@AVFC", "instagram": "@avfc"},
  "fan_email": "supporters@avfc.co.uk",
  "complaints": "https://www.avfc.co.uk/contact",
  "social_media": {
    "twitter": "@AVFC",
    "instagram": "@avfc",
    "facebook": "AstonVillaFC"
  }
}
```

**How fans use this:**
- Email the club's fan services address to express concern about sponsors
- Call the club's phone number and ask about sponsor ethics
- Tweet at the club using the social media handles
- Use the complaints page to file formal concerns

This is the "shame" mechanism — giving fans the tools to pressure clubs, similar to "call your congressman" campaigns.

---

## Step 4: GitHub Repo Structure

```
Behind-The-Jersey/
├── data/                    # Team JSON files (private)
│   ├── index.json          # Master index
│   ├── verified_data/      # Verified JSON files
│   └── *.json              # Individual team files
├── pipelines/              # Collection scripts (public)
│   ├── collect_data.py
│   ├── verify_quality.py
│   ├── build_json.py
│   └── update_sponsors.py
├── evidence/               # Evidence files (public)
│   ├── aston-villa/
│   │   ├── visit-rwanda-front.json
│   │   └── ...
│   └── ...
├── agents/                 # Tracing agents (public)
│   ├── owner-tracer.py
│   └── sponsor-finder.py
├── docs/                   # Documentation
│   ├── CONTRIBUTING.md
│   ├── EVIDENCE_FORMAT.md
│   └── RATING_METHOD.md
├── scripts/                # Utility scripts
│   └── attribute_regime_sponsors.py
└── README.md
```

---

## Step 5: Workflow

1. **Collect** — Run `collect_data.py` to fetch official league data
2. **Enrich** — Run `update_sponsors.py` to back-fill from Wikipedia/Wikidata
3. **Verify** — Run `verify_quality.py` to validate schema and quality
4. **Review** — Manual review of flagged items (Wikipedia scrutiny)
5. **Build** — Run `build_json.py` to assemble final JSON files
6. **Publish** — Push to GitHub, create PR for review
7. **Contribute** — Community submits evidence, we review and merge

---

## Step 6: Community Contributions

Three ways to help (from the brief):

1. **Run our agents** — Point the pipeline at a club nobody has checked, open a PR
2. **Bring your own agent** — Any agent can help if it writes our evidence format
3. **Check a club by hand** — No code needed, note sponsors and owners, link sources

### Shame/Contact Contribution
- Fans can submit contact info they've found for clubs
- Community can report outdated contact info
- Verified contact info gets added to team JSONs

---

## Next Steps

1. Set up GitHub repo structure
2. Create evidence files for rated clubs (Aston Villa, Arsenal, Real Madrid, Atlético)
3. Build contact/shame database for all 150 teams
4. Create CONTRIBUTING.md and evidence format docs
5. Set up CI pipeline for automated quality checks

---

*Last updated: 2026-09-24*