# Evidence Format Specification

## One file per claim

Each evidence file contains a single claim with its sources. This makes it easy to review, verify, and merge individual claims.

## File structure

```
evidence/
├── club-slug/
│   ├── sponsor-name-placement.json
│   └── ...
└── ...
```

Example: `evidence/aston-villa/visit-rwanda-front.json`

## JSON schema

```json
{
  "club": "aston-villa",
  "season": "2026/27",
  "sponsor": "Visit Rwanda",
  "placement": "front",
  "owner": "Government of Rwanda",
  "value": "up to £20m a year",
  "sources": [
    "sportspro.com/news/..."
  ],
  "verified": true,
  "last_checked": "2026-09-24"
}
```

## Field definitions

| Field | Required | Description |
|---|---|---|
| `club` | Yes | Team slug (e.g., "aston-villa") |
| `season` | Yes | Season the deal is active (e.g., "2026/27") |
| `sponsor` | Yes | Sponsor name (e.g., "Visit Rwanda") |
| `placement` | Yes | Where on the shirt: "front", "back", "sleeve", "helmet" |
| `owner` | Yes | Who owns the sponsor (e.g., "Government of Rwanda") |
| `value` | Optional | Deal value (e.g., "up to £20m a year") |
| `sources` | Yes | Array of source URLs |
| `verified` | Yes | Has a person reviewed this claim? |
| `last_checked` | Yes | Date the claim was last verified (YYYY-MM-DD) |

## Contact/Shame info

Each team JSON includes contact info for fans to express discomfort:

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

This enables the "shame" criterion — giving fans the tools to pressure clubs to drop bad sponsors, similar to "call your congressman" campaigns.

## Review process

1. Agent collects sponsor/owner data
2. Evidence file created with sources
3. Person reviews each claim before it goes live
4. Claim goes live with date logged publicly
5. Community can submit corrections via PR

## Source quality hierarchy

1. **Official** — Club statements, league announcements, press releases
2. **Press** — SportsPro, The Athletic, Sky Sports, BBC Sport
3. **NGO** — Human Rights Watch, Amnesty International, Global Witness
4. **Wikipedia** — Requires extra scrutiny, must be cross-checked
5. **Community** — User-submitted, requires verification