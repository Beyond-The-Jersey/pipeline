# Behind The Jersey — Open Source Data Pipeline

Open source pipeline for collecting, verifying, and compiling sports team sponsor data with human rights records into JSON files.

## Repos

| Repo | Visibility | Purpose |
|------|-----------|---------|
| [pipeline](https://github.com/Beyond-The-Jersey/pipeline) | Public | Scripts, prompts, agent configs |
| [data](https://github.com/Beyond-The-Jersey/data) | Private | JSON data files |

## How It Works

1. **Collect** — Agents scrape team/sponsor data from sport governing body sites
2. **Verify** — Cross-reference with HR databases (HRF, Amnesty, HRW, B&HR)
3. **Rate** — Assign A+ to F rating per sponsor
4. **Build** — Compile into structured JSON files
5. **Serve** — GitHub Pages reads JSON directly from data repo

## Data Flow

```
Sport Sites → collect_data.py → raw_data/
HR Databases → verify_quality.py → verified_data/
Rating Logic → build_json.py → data/*.json
GitHub Pages → reads data/*.json → website
```

## Usage

Other teams can run this pipeline for their own sports:

```bash
# Clone the pipeline
git clone https://github.com/Beyond-The-Jersey/pipeline.git
cd pipeline

# Configure your sport
cp prompts/sport_config.example.yaml prompts/sport_config.yaml
# Edit with your sport's governing body URLs

# Run collection
python3 scripts/collect_data.py

# Verify quality
python3 scripts/verify_quality.py

# Build JSON
python3 scripts/build_json.py
```

## Contributing

1. Fork the repo
2. Add your sport's collection scripts
3. Submit a PR
4. Once merged, data gets added to the data repo

## License

MIT — free to use, modify, and share.
