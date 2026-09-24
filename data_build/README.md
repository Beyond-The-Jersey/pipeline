# data_build — how `Beyond-The-Jersey/data` `normalized/` is produced

The builders live here so the data repo's `meta.generatedBy` is honest and the build
is reproducible. Run from the `data` repo root:

    pip3 install requests jsonschema
    python3 data_build/build_contacts.py     # network; writes data_build/contacts_build.json
    python3 data_build/build_normalized.py   # writes normalized/ and runs validate.py

`build_normalized.py` starts from the website seed (`website/data/seed`) and merges the
curated additions in `pipeline_data.py`. `build_from_seed.py` is the earlier seed-only
builder, kept for history.

Set `BTJ_SEED` and `BTJ_VALIDATE` if the website checkout is not at `/tmp/website`.

## Schema rules the merge enforces

* referential fields (`clubId`, `sponsorId`, `ownerId`, `claimIds`) hold **ids**, never names
* ids are ASCII kebab-case; seed ids are never renamed (`afc-bournemouth` stays)
* `source` is `{name, date, url}` of the primary document, or omitted / null while looking
* optional fields are omitted when unknown; `null` only where the schema means it
  (undisclosed deal value, no kit change)
* currencies are `GBP` / `EUR` / `USD`
* one kit per club per season
* Wikipedia and Wikidata are leads, never cited as the source

## Verification

`verify_issue_1.py` re-checks every bullet of `data` issue #1 against a **clean clone**:

    python3 verify_issue_1.py

It expects the clone at `/tmp/verify`. Run it against the clone, not the working tree, so
the result covers what is actually pushed.
