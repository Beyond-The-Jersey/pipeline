# Behind The Jersey

Sports team human rights sponsor tracker — data pipeline and JSON files.

## What we do

We collect, verify, and publish data about who sponsors sports teams and what human-rights records those sponsors have. Every claim is sourced, every rating is reviewed by a person before going live.

## Rating scale

**Clean → Spotted → Stained → Soaked**

- **Clean**: Every sponsor checked, nothing found
- **Spotted**: Lesser link to a state or state-owned entity
- **Stained**: Serious sponsor on the front of the shirt
- **Soaked**: Severe sponsor on the front, or two serious ones

## Data

- 150 teams across 6 leagues (Premier League, La Liga, Bundesliga, NBA, NFL, MLB)
- Sponsor and owner data for every team
- Authoritarian regime sponsors flagged
- Contact/shame info for fan pressure campaigns

## Shame/Contact Criterion

Each team includes contact info so fans can pressure clubs to drop bad sponsors:

```json
"contact": {
  "email": "info@avfc.co.uk",
  "phone": "+44 800 XXX XXXX",
  "website": "https://www.avfc.co.uk",
  "fan_email": "supporters@avfc.co.uk",
  "complaints": "https://www.avfc.co.uk/contact",
  "social_media": {"twitter": "@AVFC", "instagram": "@avfc"}
}
```

**How fans use this:**
- Email the club's fan services to express concern about sponsors
- Call the club's phone number and ask about sponsor ethics
- Tweet at the club using the social media handles
- Use the complaints page to file formal concerns

This is the "shame" mechanism — giving fans the tools to pressure clubs, similar to "call your congressman" campaigns.

## How It Works

1. **Collect** — Agents scrape team/sponsor data from sport governing body sites + Wikipedia/Wikidata
2. **Verify** — Cross-reference with HR databases (HRF, Amnesty, HRW, B&HR) and official sources
3. **Scrutinize** — Wikipedia data gets extra scrutiny: every claim sourced, contradictory data flagged
4. **Rate** — Assign Clean/Spotted/Stained/Soaked per sponsor and club
5. **Build** — Compile into structured JSON files with contact/shame info
6. **Serve** — GitHub repo reads JSON directly for frontend

## Data Flow

```
Sport Sites → collect_data.py → raw_data/
Wikipedia → update_sponsors.py → raw_data/
Wikidata → extract_wikidata.py → raw_data/
HR Databases → verify_quality.py → verified_data/
Contact Info → attribute_shame.py → data/*.json
Rating Logic → build_json.py → data/*.json
GitHub → JSON files → frontend team
```

## Contributing

1. Fork the repo
2. Add your sport's collection scripts or evidence files
3. Submit a PR
4. Once merged, data gets added to the data repo

## License

MIT — free to use, modify, and share.