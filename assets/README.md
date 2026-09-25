# Wikimedia asset sourcing

Every club in `normalized/clubs.json` now has a sourced crest, and every club with a
current-season shirt has sourced home / away / third kit images — pulled from
Wikipedia / Wikimedia Commons.

Source: `assets/wikimedia-assets.csv`

| column | meaning |
| --- | --- |
| `club` | `clubs.json` id |
| `asset` | `crest`, `kit-home`, `kit-away` or `kit-third` |
| `wikimedia_file` | Commons / en.wiki `File:` title, needed for attribution |
| `direct_url` | `upload.wikimedia.org` URL to download |
| `license` | licence as stated on the file page |
| `wikipedia_page` | page the asset was read from |

## Coverage

- **331 crests** for 331 clubs (331 of 331 — no club left without one).
- **432 kit images** (175 home, 136 away, 121 third), all from the **2026-27** season where Wikipedia has it.
- **0 unknown licences.** Every row carries a licence value.

## Licences — read this before shipping

762 rows total:

| licence | rows | note |
| --- | --- | --- |
| Non-free (fair use), en.wiki-hosted | 206 | club crests — copyrighted logos |
| Commons: Non-free (fair use) | 6 | crests uploaded to Commons under non-free terms |
| Commons: CC0 | 364 | kit templates, public domain dedication |
| Commons: Public domain | 95 | old crests, simple shapes |
| Public domain (en.wiki) | 10 | |
| Commons: CC BY-SA | 78 | attribution + share-alike |
| Commons: CC BY / GFDL / Unknown | 4 | |

**212 of 331 crests are non-free.** They are the actual club marks, not
free re-draws — which is what the site wants visually, but it means the crest layer is
*not* blanket-licensed. Keep the `wikimedia_file` value on file for attribution and
treat non-free crests as fair-use / nominative use.

Kit templates are almost entirely CC0 or CC BY-SA, so the shirt layer is clean.

## Reproduce

```bash
python3 assets/build_assets.py        # writes assets/wikimedia-assets.csv
```

Batched API use (~30 titles + full continuation handling per request) — a few hundred
requests total, well inside rate limits. No API key.
