"""Turn the US-league research batches into pipeline records.

Reads /tmp/ingest_b*_out.json (patch sponsor + arena naming rights per club) and writes
/tmp/data/us_ingest.py, which build_normalized.py merges the same way it merges
research_additions.

Modelling, as agreed: a jersey patch is a sponsor ON the jersey kit (placement "patch"),
an arena naming-rights deal is a DEAL (placement "stadium"), and the venue name goes in the
deal note so it is not lost.
"""
import json
import os
import pprint
import re
import sys

OUT = "/tmp/data/us_ingest.py"
BATCHES = ["/tmp/ingest_b%d_out.json" % i for i in range(1, 8)]


def slug(s):
    s = (s or "").lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def main():
    # the batches reuse existing sponsor ids (att, crypto-com, ford...). Reuse the existing
    # owner too, or the same company lands twice under two ids and the owner check fires.
    try:
        existing_sp = {x["id"]: x for x in json.load(open("/tmp/data/normalized/sponsors.json"))}
        existing_ow = {x["id"]: x for x in json.load(open("/tmp/data/normalized/owners.json"))}
    except Exception:
        existing_sp, existing_ow = {}, {}
    ow_by_name = {}
    for _o in existing_ow.values():
        ow_by_name.setdefault(slug(_o.get("name")), _o["id"])
    seen_owner, seen_sponsor, seen_kit, seen_deal = {}, {}, {}, {}
    owners, sponsors, kits, deals, claims = [], [], [], [], []
    unresolved, reused = [], set()
    n = 0

    for path in BATCHES:
        if not os.path.exists(path):
            continue
        try:
            data = json.load(open(path))
        except Exception as e:
            print("  %s unreadable: %s" % (os.path.basename(path), e))
            continue
        for row in data.get("clubs", []):
            n += 1
            cid = row.get("clubId")
            if not cid:
                continue

            def ensure_org(entry, kind, club):
                """Create-or-reuse the owner + sponsor for one researched organisation."""
                org = (entry or {}).get("orgName")
                if not org:
                    return None
                hint = slug(entry.get("sponsorIdHint") or org)
                # reuse the owner record whenever this company already has one under any id,
                # so one company never lands twice (the owner check fires on exactly that)
                if hint in existing_sp:
                    oid = existing_sp[hint]["ownerId"]
                    reused.add(hint)
                else:
                    oid = ow_by_name.get(slug(org)) or (hint + "-owner")
                if oid not in seen_owner:
                    if oid in existing_ow:
                        seen_owner[oid] = dict(existing_ow[oid])
                    else:
                        seen_owner[oid] = {
                            "id": oid, "name": org, "type": "unknown",
                            "parentId": None, "note": "%s of %s (2026-27)." % (kind, club),
                        }
                    owners.append(seen_owner[oid])
                if hint in existing_sp and hint not in seen_sponsor:
                    seen_sponsor[hint] = dict(existing_sp[hint])
                    sponsors.append(seen_sponsor[hint])
                if hint not in seen_sponsor:
                    seen_sponsor[hint] = {
                        "id": hint, "name": org, "ownerId": oid, "ownership": "owned",
                        "tier": "unrated", "status": "unrated", "verdict": None,
                        "claimIds": [], "aliases": [],
                        "note": "%s of %s (2026-27)." % (kind.capitalize(), club),
                    }
                    sponsors.append(seen_sponsor[hint])
                # one documented claim per sponsor so the rating pass has something to attach to
                cl_id = "%s-2026" % hint
                if cl_id not in {c["id"] for c in claims}:
                    src = entry.get("source") or {}
                    claims.append({
                        "id": cl_id, "ownerIds": [oid],
                        "text": "%s is the %s of %s for 2026-27." % (org, kind, club),
                        "short": "%s %s 2026-27" % (kind.capitalize(), org),
                        "source": {"name": src.get("name") or "see url",
                                   "date": src.get("date") or "2026-01-01",
                                   "url": src.get("url")},
                        "reviewed": True,
                    })
                return hint

            club = row.get("clubId")
            patch = ensure_org(row.get("patch"), "jersey patch partner", club)
            arena = ensure_org(row.get("arena"), "arena naming-rights holder", club)

            # every club gets a jersey, even the patchless ones
            place = "training-kit" if row.get("league") == "nfl" else "patch"
            kid = "%s-2026-27-home" % cid
            if kid not in seen_kit:
                placements = []
                if patch:
                    psrc = row["patch"].get("source") or {}
                    placements.append({
                        "sponsorId": patch, "placement": place,
                        "source": {"name": psrc.get("name") or "see url",
                                   "date": psrc.get("date") or "2026-01-01",
                                   "url": psrc.get("url")},
                    })
                seen_kit[kid] = {
                    "id": kid, "clubId": cid, "season": "2026-27", "kitType": "home",
                    "periodLabel": "2026/27", "periodFrom": "2026-27", "periodTo": "2026-27",
                    "photos": {},
                    "sponsors": placements,
                    "sponsorsComplete": bool(patch),
                    "summary": (("Practice-jersey patch: %s." if place == "training-kit"
                                 else "Jersey patch: %s.") % row["patch"].get("orgName"))
                               if patch else "No patch partner for 2026-27.",
                    "change": None,
                }
                kits.append(seen_kit[kid])

            if patch:
                _y = re.search(r"(?:19|20)\d\d", str(row["patch"].get("since") or ""))
                start = _y.group(0) if _y else "2026"
                did = "%s-%s-patch" % (cid, patch)
                if did not in seen_deal:
                    src = row["patch"].get("source") or {}
                    seen_deal[did] = {
                        "id": did, "clubId": cid, "orgName": row["patch"].get("orgName"),
                        "sponsorId": patch, "placement": place,
                        "from": start, "to": None, "value": None,
                        "source": {"name": src.get("name") or "see url",
                                   "date": src.get("date") or "2026-01-01",
                                   "url": src.get("url")},
                        "note": "Practice-jersey patch." if place == "training-kit" else "Jersey patch.",
                    }
                    deals.append(seen_deal[did])

            if arena:
                did = "%s-%s-stadium" % (cid, arena)
                if did not in seen_deal:
                    src = row["arena"].get("source") or {}
                    venue = row["arena"].get("venueName")
                    seen_deal[did] = {
                        "id": did, "clubId": cid, "orgName": row["arena"].get("orgName"),
                        "sponsorId": arena, "placement": "stadium",
                        "from": "2026", "to": None, "value": None,
                        "source": {"name": src.get("name") or "see url",
                                   "date": src.get("date") or "2026-01-01",
                                   "url": src.get("url")},
                        "note": ("Arena naming rights: %s." % venue) if venue else "Arena naming rights.",
                    }
                    deals.append(seen_deal[did])

            if not patch and not arena:
                unresolved.append(cid)

    with open(OUT, "w", encoding="utf-8") as f:
        f.write('"""US league patch and arena records, generated by make_us_ingest.py."""\n\n')
        for name, val in (("NEW_OWNERS", owners), ("NEW_SPONSORS", sponsors),
                          ("NEW_KITS", kits), ("NEW_DEALS", deals), ("EXTRA_CLAIMS", claims)):
            f.write("%s = " % name)
            # this module is imported as Python, so it needs None/True, not JSON null/true
            f.write(pprint.pformat(val, width=118, sort_dicts=False))
            f.write("\n\n")

    print("clubs read %d | owners %d sponsors %d kits %d deals %d claims %d"
          % (n, len(owners), len(sponsors), len(kits), len(deals), len(claims)))
    if unresolved:
        print("no patch and no arena (%d): %s" % (len(unresolved), ", ".join(unresolved)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
