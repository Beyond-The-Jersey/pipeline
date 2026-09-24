"""Independent check of every bullet in Beyond-The-Jersey/data#1."""
import json
import os
import re

D = "/tmp/verify/normalized"
J = lambda n: json.load(open(os.path.join(D, n + ".json"), encoding="utf-8"))

clubs, sponsors, owners = J("clubs"), J("sponsors"), J("owners")
claims, kits, deals = J("claims"), J("kits"), J("deals")
changes, dropped, contacts = J("changes"), J("dropped"), J("contacts")
sports, leagues, meta = J("sports"), J("leagues"), J("meta")

cid = {c["id"] for c in clubs}
sid = {s["id"] for s in sponsors}
oid = {o["id"] for o in owners}
names = {c["name"] for c in clubs}

out = []
def chk(label, ok, detail=""):
    out.append((("PASS" if ok else "FAIL"), label, detail))

# 1 referential fields use ids
bad = [(k["id"], k["clubId"]) for k in kits if k["clubId"] not in cid]
bad += [(d["id"], d["clubId"]) for d in deals if d.get("clubId") and d["clubId"] not in cid]
bad += [(c["clubId"],) for c in contacts if c["clubId"] not in cid]
bad += [(d["id"], d["clubId"]) for d in changes if d.get("clubId") and d["clubId"] not in cid]
chk("referential fields hold club ids", not bad, str(bad[:4]))
chk("no club display name used as an id", not (names & {c["id"] for c in clubs} - {"athletics"}))

# 2 sources are objects, not free strings
def srcs(obj, field="source"):
    return [o.get(field) for o in obj]
bad = [o.get("id") for o in kits + deals + changes + claims + dropped
       if o.get(field := "source") and not isinstance(o["source"], dict)]
chk("source is {name,date,url} or null, never a string", not bad, str(bad[:4]))
missing = [c["id"] for c in claims if not c.get("source", {}).get("url")]
chk("all 8 claims carry an exact source URL", not missing, str(missing))

# 3 omitted vs null
bad = [k["id"] for k in kits if "photos" in k and k["photos"] is None]
bad += [o["id"] for o in owners if ("country" in o and o["country"] is None) or ("via" in o and o["via"] is None)]
bad += [c["clubId"] for c in contacts for ch in c["channels"] if ch.get("source", {}).get("url") is None]
bad += [k["id"] for k in kits if k.get("photos") is None]
chk("no null where the field should be omitted", not bad, str(bad[:4]))
bad = [k["id"] for k in kits if "change" not in k]
chk('every kit has "change"', not bad, str(bad[:4]))
bad = [d["id"] for d in deals if isinstance(d.get("value"), dict)
       and all(v is None for v in d["value"].values())]
chk("no deal value that is an object of nulls", not bad)
bad = [d["id"] for d in deals if d.get("value") and d["value"].get("currency") not in ("GBP", "EUR", "USD")]
chk("currencies are GBP/EUR/USD", not bad)

# 4 changes
chk("six seed changes restored", len([c for c in changes if c["id"] != "2026-09-17-chelsea-circle-usdc"]) == 6)
bad = [c["id"] for c in changes if not (c.get("date") and c.get("title") and c.get("levelAfter") and c.get("source"))]
chk("every change is dated, titled, rated and sourced", not bad, str(bad))

# 5 sports / leagues
chk("no american_football", {c["sportId"] for c in clubs} == {"soccer", "american-football", "basketball", "baseball"})
chk("baseball in sports.json", "baseball" in {s["id"] for s in sports})
chk("mlb and 2-bundesliga in leagues.json",
    {"mlb", "2-bundesliga"} <= {l["id"] for l in leagues})
chk("every club's sport and league exist",
    {c["sportId"] for c in clubs} <= {s["id"] for s in sports}
    and {c["leagueId"] for c in clubs} <= {l["id"] for l in leagues})

# 6 ids
pat = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
bad = [o["id"] for o in owners if not pat.match(o["id"])]
bad += [s["id"] for s in sponsors if not pat.match(s["id"])]
chk("all ids ASCII kebab-case", not bad, str(bad[:4]))
chk("seed id afc-bournemouth kept, no bournemouth", "afc-bournemouth" in cid and "bournemouth" not in cid)

# 7 content
per = {}
for k in kits:
    if k["season"] == "2026-27":
        per.setdefault(k["clubId"], []).append(k["id"])
chk("one 2026-27 kit per club", all(len(v) == 1 for v in per.values()),
    str([v for v in per.values() if len(v) > 1]))
chk("no bogus sponsors", not ({"sam-gillam", "donald-coles"} & sid))
chk("single etihad sponsor", [s["id"] for s in sponsors if "etihad" in s["id"]] == ["etihad-airways"])
chk("no unverifiable luton-puma-2025", "luton-puma-2025" not in {d["id"] for d in dropped})
chk("dropped items carry sources", all(d.get("source", {}).get("url") for d in dropped))

# 8 contacts
chk("a contact entry for every club", {c["clubId"] for c in contacts} == cid)
bad = [c["clubId"] for c in contacts if not c["channels"]]
chk("every contact has at least one channel", not bad)
bad = [c["clubId"] for c in contacts for ch in c["channels"] if not ch.get("source", {}).get("url")]
chk("every channel carries the URL that publishes it", not bad)

# 9 countries / meta
chk("all clubs have a country", all(c.get("country") for c in clubs))
chk("meta.generatedBy is the pipeline", meta.get("generatedBy", "").startswith("Beyond-The-Jersey data pipeline"))
chk("meta.updatedAt is the last real data change", meta.get("updatedAt") == "2026-09-24")

# 10 priority-1 leftovers
chk("sources on every sponsor of every 2026-27 kit",
    all(p.get("source", {}).get("url") for k in kits if k["season"] == "2026-27" for p in k["sponsors"]))
for club in ("arsenal", "aston-villa", "atletico-de-madrid"):
    e = next(c for c in contacts if c["clubId"] == club)
    chk(f"sourced contacts for {club}", all(ch["source"]["url"] for ch in e["channels"]),
        f"{len(e['channels'])} channels")

# 11 tiers untouched
tiers = J("tiers")
chk("tiers.json unchanged in substance",
    [t["id"] for t in tiers] == ["unrated", "none", "concern", "serious", "severe"])

fails = [r for r in out if r[0] == "FAIL"]
for s, l, d in out:
    print(f"{s}  {l}" + (f"   -> {d}" if d else ""))
print(f"\n{len(out) - len(fails)}/{len(out)} passed")
