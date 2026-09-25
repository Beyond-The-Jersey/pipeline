"""Turn the researched ratings into a Python module the builder can consume.

Reads /tmp/ratings.json (produced by a research pass) and writes ratings_data.py.
Two ratings are adjusted here, with the reason recorded alongside the research
note so the reviewer can see the join between research and judgement.
"""
import json
import os
import pprint
import re

SRC = ["/tmp/ratings.json", "/tmp/ratings2.json",
       "/tmp/rate_batch_1_out.json", "/tmp/rate_batch_2_out.json",
       "/tmp/rate_batch_3_out.json"]
OUT = "/tmp/data/ratings_data.py"

# sponsorId -> ownership on the shirt's owner chain
PART_OWNED = {"turkish-airlines", "deutsche-telekom", "lbbw"}

# Judgement calls layered on top of the research, never instead of it.
# SC: two multi-hundred-million-dollar forfeitures over four decades of working
# around Iran/Sudan sanctions is a sustained structural adverse record, not a
# one-off fine -> concern under tiers.json's "a lesser link".
# Uralkali: no state stake, but the ultimate owner sits in a belligerent state
# and was itself sanctioned -> concern.
OVERRIDE = {
    "standard-chartered": (
        "concern",
        "Raised from none: the 2012 and 2019 forfeitures are a sustained structural "
        "record, not a one-off fine, which is what tiers.json calls 'a lesser link'.",
    ),
    "uralkali": (
        "concern",
        "Raised from none: no state stake, but the ultimate owner sits inside a "
        "belligerent state and was sanctioned with it.",
    ),
}


def short_of(text, limit=165):
    t = re.sub(r"\s+", " ", (text or "").strip())
    first = t.split(". ")[0].strip()
    if len(first) > limit:
        first = first[: limit - 1].rsplit(" ", 1)[0] + "…"
    return first if first.endswith((".", "!", "?")) else first + "."


def verdict_for(tier, owner, short):
    name = owner["name"]
    if tier == "none":
        return f"Owned by {name}. Nothing found."
    if tier == "concern":
        return f"{short}"
    return short


def main():
    rows = []
    seen = set()
    for path in SRC:
        if not os.path.exists(path):
            print("missing", path)
            continue
        raw = json.load(open(path, encoding="utf-8"))
        for r in (raw["ratings"] if isinstance(raw, dict) else raw):
            if r["sponsorId"] in seen:
                continue
            seen.add(r["sponsorId"])
            rows.append(r)
    out = []
    for r in rows:
        sid = r["sponsorId"]
        tier = r["tier"]
        note = (r.get("note") or "").strip()
        if sid in OVERRIDE and tier == "unrated":
            tier = OVERRIDE[sid][0]
        if sid in OVERRIDE:
            tier, why = OVERRIDE[sid]
            note = (note + " " if note else "") + "ADJUSTED: " + why
        owner = r["owner"]
        claim = r.get("claim") or {}
        src = claim.get("source") or {}
        if not src.get("url"):
            continue  # a tier above unrated needs a source with a URL
        text = re.sub(r"\s+", " ", claim.get("text", "")).strip()
        short = short_of(text)
        out.append({
            "sponsorId": sid,
            "tier": tier,
            "ownership": "part-owned" if sid in PART_OWNED else "owned",
            "owner": {
                "id": owner["id"],
                "name": owner["name"],
                "type": owner["type"],
                "country": owner.get("country"),
                "note": note or None,
            },
            "claim": {
                "text": text,
                "short": short,
                "source": {"name": src.get("name"), "date": src.get("date"), "url": src.get("url")},
            },
            "verdict": verdict_for(tier, owner, short),
            "confidence": r.get("confidence"),
            "note": note or None,
        })
    out.sort(key=lambda x: x["sponsorId"])

    with open(OUT, "w", encoding="utf-8") as f:
        f.write('"""Sponsor ratings with the owner chain and the evidence behind each one."""\n\n')
        f.write("RATINGS = ")
        # this file is imported as Python, so it needs None/True, not JSON null/true
        f.write(pprint.pformat(out, width=118, sort_dicts=False))
        f.write("\n")
    print("wrote", OUT, len(out), "ratings")
    from collections import Counter
    print("tiers:", dict(Counter(x["tier"] for x in out)))


if __name__ == "__main__":
    main()
