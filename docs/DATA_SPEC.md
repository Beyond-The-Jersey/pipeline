# Data Specification — Behind The Jersey

## JSON Schema

### Team File (`data/manutd.json`) — Updated
```json
{
  "team": "Manchester United",
  "sport": "soccer",
  "league": "Premier League",
  "country": "England",
  "contact": {
    "phone": "+44 800 ...",
    "email": "marketing@manutd.com",
    "twitter": "@ManUtd",
    "website": "https://www.manutd.com"
  },
  "sponsors": [...],
  "shame": {
    "description": "Contact the team to express discomfort about sponsor ratings",
    "methods": [
      {"type": "email", "address": "marketing@manutd.com", "label": "Marketing dept"},
      {"type": "phone", "number": "+44 800 ...", "label": "Main line"},
      {"type": "twitter", "handle": "@ManUtd", "label": "Tweet your concern"}
    ]
  },
  "last_updated": "2026-09-22",
  "data_version": "0.1"
}
```

## Contact/Shame Feature

For each team, include contact information so fans can pressure teams about their sponsor ratings:
- Phone number
- Email address
- Twitter/social media handle
- Website

Copy-paste templates:
- Email: "I'm concerned about [sponsor] rated [rating]. Please reconsider."
- Phone: "Hi, I'm calling about [team]'s sponsor [name] rated [rating]"
- Social: #BehindTheJersey #[TeamName]

### Index File (`data/index.json`)
```json
{
  "version": "0.1",
  "last_updated": "2026-09-22",
  "teams": [
    {
      "name": "Manchester United",
      "sport": "soccer",
      "league": "Premier League",
      "file": "manutd.json"
    }
  ],
  "stats": {
    "total_teams": 10,
    "total_sponsors": 45,
    "verified_percentage": 80
  }
}
```

## Rating Scale

| Rating | Description |
|--------|-------------|
| A+ | Strong human rights supporter, no controversies |
| A | Positive record, minor concerns only |
| B | Some concerns, no major violations |
| C | Mixed record, some documented issues |
| D | Significant concerns, multiple incidents |
| F | Severe violations, complicity in abuses |

## Data Collection Rules

1. **Minimum 2 sources** per data point
2. **Unverified** flag if only 1 source
3. **F-level** flags default rating to D until confirmed
4. **Cross-team consistency** check — same company rated differently = flag
5. **Orphan sponsors** — listed but no team = flag

## Sports Covered (MVP)
- Soccer (Premier League, La Liga, Serie A, Bundesliga, Ligue 1)
- Basketball (NBA)
- American Football (NFL)

## Data Sources

### Tier 1 — Financial Disclosures
- Champions League / UEFA sponsorship listings
- FIFA sponsorship disclosures
- NBA/NFL/MLB official partner pages

### Tier 2 — Human Rights Reports
- Human Rights Foundation (hrforum.org)
- Amnesty International (amnesty.org)
- Human Rights Watch (hrw.org)
- Business & Human Rights Resource Centre (business-humanrights.org)

### Tier 3 — News & Investigations
- News articles about sponsorship deals
- Government statements
- Stadium protest incidents

---

## Pipeline Implementation

### Scripts
| Script | Purpose |
|--------|---------|
| `scripts/collect_data.py` | Collects team data from Wikipedia (static HTML) |
| `scripts/verify_quality.py` | Cross-references HR databases, validates schema |
| `scripts/build_json.py` | Compiles verified data into JSON files |
| `scripts/run_pipeline.py` | Master workflow — runs all 3 steps |

### Master Workflow
```bash
python3 scripts/run_pipeline.py
```
Runs: Collect → Verify → Build JSON

### Quality Checks
- Required fields present (team, sport, league, country, contact, shame)
- Contact info complete (phone, email, twitter)
- Shame methods complete (email, phone, twitter)
- HR cross-reference against known issues database
- 100% verification rate required for MVP
