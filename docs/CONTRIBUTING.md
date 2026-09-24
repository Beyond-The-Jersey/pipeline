# Contributor Guide — Behind The Jersey

## How to contribute

We have three ways to help:

### 1. Run our agents

Point the pipeline at a club nobody has checked and open a pull request with what it finds.

```bash
# Clone the pipeline
git clone https://github.com/BigBossRabbit/Behind-The-Jersey.git
cd Behind-The-Jersey

# Run collection
python3 pipelines/collect_data.py

# Verify quality
python3 pipelines/verify_quality.py

# Build JSON
python3 pipelines/build_json.py
```

### 2. Bring your own agent

Any agent can help if it writes our evidence format: one claim, one source, one file.

See [EVIDENCE_FORMAT.md](EVIDENCE_FORMAT.md) for the format specification.

### 3. Check a club by hand

No code needed. Pick a club, note who sponsors it and who owns them, and link your sources.

1. Find a club nobody has checked yet
2. Note the current sponsors (front, back, sleeve)
3. Find who owns each sponsor
4. Link sources for each claim
5. Open a PR with the evidence files

### 4. Submit contact info (Shame criterion)

Help fans pressure clubs by finding phone and email addresses:

1. Find the club's official contact page
2. Note the fan services email, phone number, and social media handles
3. Open a PR with the contact info added to the team JSON

## Evidence format

One file per claim:

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

## Quality standards

- Every claim must have a source cited
- Wikipedia data gets extra scrutiny (see PIPELINE_PLAN.md)
- Contradictory data flagged for manual review
- "Not rated yet" if sources conflict

## Rating scale

- **Clean**: Every sponsor checked, nothing found
- **Spotted**: Lesser link to a state or state-owned entity
- **Stained**: Serious sponsor on the front of the shirt
- **Soaked**: Severe sponsor on the front, or two serious ones

## Contact

For questions, open an issue or contact the team through the GitHub org.