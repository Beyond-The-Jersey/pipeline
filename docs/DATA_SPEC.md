# Data Specification — Behind The Jersey

## JSON Schema

### Team File (`data/manutd.json`)
```json
{
  "team": "Manchester United",
  "sport": "soccer",
  "league": "Premier League",
  "country": "England",
  "sponsors": [
    {
      "name": "TeamViewer",
      "type": "company",
      "category": "technology",
      "rating": "C",
      "rating_desc": "Mixed / some concerns",
      "flags": ["Russia operations post-2022"],
      "deal_value": null,
      "sources": ["https://www.manutd.com/en/information/sponsors"],
      "verified": true,
      "last_updated": "2026-09-22"
    }
  ],
  "last_updated": "2026-09-22",
  "data_version": "0.1"
}
```

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
