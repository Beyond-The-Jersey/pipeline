# Frontend Handoff — Behind The Jersey

**Data repo:** `/tmp/data/` | **Pipeline repo:** `/tmp/pipeline/`

---

## JSON Schema

### Team File (`data/<slug>.json`)

```
{
  "team":        string,     // e.g. "Manchester United"
  "sport":       string,     // "soccer" | "basketball"
  "league":      string,     // "Premier League" | "NBA"
  "country":     string,
  "contact":     { phone, email, twitter, website },
  "sponsors":    [{ name, type, category, rating, rating_desc, flags[], deal_value, sources[], verified, last_updated }],
  "shame":       { description, methods[{ type, address|handle, label }] },
  "last_updated": "YYYY-MM-DD",
  "data_version": "0.1"
}
```

### Index File (`data/index.json`)

```
{
  "version": "0.1",
  "last_updated": "YYYY-MM-DD",
  "teams": [{ name, sport, league, country, file }],
  "total_teams": 50
}
```

### Verified Data (`data/verified_data/verified_data.json`)

```
{ "version": "0.1", "checked_at": ISO8601, "teams": { "<slug>": { verified, errors[], warnings[], hr_flags[], contact_present, shame_present, sponsor_count, hr_issue_count } } }
```

---

## Consuming the Data

1. Load `index.json` → get team list + file mapping.
2. Fetch individual `<slug>.json` per team or in parallel.
3. Optionally cross-reference `verified_data.json` for quality flags (errors/warnings/hr_flags).
4. Teams directory: 51 files (32 soccer, 19 basketball).

---

## Contact / Shame Fields

**`contact`** — team's public channels:
| Field | Type | Notes |
|-------|------|-------|
| phone | string | May be `"+44 800 ..."` placeholder |
| email | string | Marketing/support address |
| twitter | string | `@handle` |
| website | string | Full URL |

**`shame.methods`** — actions a fan can take; each has:
- `type`: `"email"`, `"phone"`, `"twitter"`
- `address` / `handle`: target
- `label`: human-readable description

---

## Rating System

| Grade | Meaning |
|-------|---------|
| **A+** | Strong human rights supporter, no controversies |
| **A**  | Positive record, minor concerns only |
| **B**  | Some concerns, no major violations |
| **C**  | Mixed record, some documented issues |
| **D**  | Significant concerns, multiple incidents |
| **F**  | Severe violations, complicity in abuses |

- Sponsors with no rating default to **D** until verified.
- Cross-team consistency check flags same company rated differently.

---

## Testing Checklist

- [ ] All 51 team files parse as valid JSON
- [ ] Required top-level keys present: `team`, `sport`, `league`, `country`, `contact`, `shame`
- [ ] `contact` has phone + email + twitter (website optional)
- [ ] `shame.methods` has ≥1 method with valid type
- [ ] Sponsor `rating` is one of A+/A/B/C/D/F
- [ ] `index.json` `total_teams` matches actual file count
- [ ] `index.json` `teams[].file` points to existing file
- [ ] `verified_data.json` has entry for every team slug
- [ ] No duplicate sponsor names within a team
- [ ] `last_updated` dates are valid ISO-8601 or YYYY-MM-DD
- [ ] All `sources` URLs in sponsors are valid HTTP links
- [ ] Cross-reference: same sponsor rated differently across teams → flag for review
