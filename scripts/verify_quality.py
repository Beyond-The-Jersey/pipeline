#!/usr/bin/env python3
"""Cross-reference sponsors with human rights databases."""

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

DATA_DIR = Path("data")
VERIFIED_DIR = Path("verified_data")
VERIFIED_DIR.mkdir(exist_ok=True)

# Known human rights databases to check against
HR_DATABASES = {
    "hrf": {"name": "Human Rights First", "url": "https://hrforum.org"},
    "amnesty": {"name": "Amnesty International", "url": "https://amnesty.org"},
    "hrw": {"name": "Human Rights Watch", "url": "https://hrw.org"},
    "bhr": {"name": "Business & Human Rights Resource Centre", "url": "https://business-humanrights.org"},
}

MIN_SOURCES = 2

# Known sponsor-HR associations (from initial research)
KNOWN_HR_ISSUES = {
    "TeamViewer": {"source": "hrw", "issue": "Sponsored Russian entities amid Ukraine invasion"},
    "Etihad Airways": {"source": "amnesty", "issue": "UAE human rights concerns"},
    "Emirates": {"source": "hrw", "issue": "UAE labor rights record"},
    "Aramco": {"source": "hrw", "issue": "Saudi Arabia human rights concerns"},
    "Qatar Airways": {"source": "amnesty", "issue": "Qatar labor rights concerns"},
    "Saudi Aramco": {"source": "hrw", "issue": "Saudi Arabia human rights concerns"},
}

def check_sponsor_hr(sponsor_name: str) -> dict:
    """Check a sponsor against HR databases."""
    sponsor_lower = sponsor_name.lower()
    
    # Check against known HR issues
    for known_sponsor, hr_data in KNOWN_HR_ISSUES.items():
        if known_sponsor.lower() in sponsor_lower or sponsor_lower in known_sponsor.lower():
            return {
                "found": True,
                "source": hr_data["source"],
                "issue": hr_data["issue"],
                "database": HR_DATABASES[hr_data["source"]]["name"],
            }
    
    return {"found": False, "source": None, "issue": None, "database": None}

def verify_team(team_data: dict) -> dict:
    """Verify a team's data quality and HR cross-references."""
    errors = []
    warnings = []
    hr_flags = []

    # Check required fields
    for field in ["team", "sport", "league", "country"]:
        if field not in team_data or not team_data[field]:
            errors.append(f"Missing required field: {field}")

    # Check contact info
    contact = team_data.get("contact", {})
    for field in ["phone", "email", "twitter"]:
        if field not in contact or not contact[field]:
            errors.append(f"Missing contact field: {field}")

    # Check shame info
    shame = team_data.get("shame", {})
    for field in ["description", "methods"]:
        if field not in shame or not shame[field]:
            errors.append(f"Missing shame field: {field}")

    methods = shame.get("methods", [])
    if len(methods) < 1:
        errors.append("No shame methods defined")

    # Check sponsors for HR issues
    sponsors = team_data.get("sponsors", [])
    for sponsor in sponsors:
        sponsor_name = sponsor.get("name", "")
        hr_check = check_sponsor_hr(sponsor_name)
        if hr_check["found"]:
            hr_flags.append({
                "sponsor": sponsor_name,
                "source": hr_check["source"],
                "issue": hr_check["issue"],
                "database": hr_check["database"],
            })
            warnings.append(f"HR issue found: {sponsor_name} — {hr_check['issue']}")

    verified = len(errors) == 0
    return {
        "team": team_data.get("team", "unknown"),
        "verified": verified,
        "errors": errors,
        "warnings": warnings,
        "hr_flags": hr_flags,
        "contact_present": bool(contact.get("email") and contact.get("twitter")),
        "shame_present": bool(shame.get("methods")),
        "sponsor_count": len(sponsors),
        "hr_issue_count": len(hr_flags),
    }

def main():
    # Load all team JSON files
    json_files = sorted(DATA_DIR.glob("*.json"))
    json_files = [f for f in json_files if f.name != "index.json"]

    results = {
        "version": "0.1",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "hr_databases": {k: v["url"] for k, v in HR_DATABASES.items()},
        "teams": {},
        "summary": {},
    }

    total_teams = 0
    verified_teams = 0
    total_errors = 0
    total_warnings = 0
    total_hr_flags = 0
    contact_ok = 0
    shame_ok = 0

    for json_file in json_files:
        with open(json_file) as f:
            team_data = json.load(f)

        result = verify_team(team_data)
        results["teams"][json_file.stem] = result
        total_teams += 1

        if result["verified"]:
            verified_teams += 1
        total_errors += len(result["errors"])
        total_warnings += len(result["warnings"])
        total_hr_flags += len(result["hr_flags"])

        if result["contact_present"]:
            contact_ok += 1
        if result["shame_present"]:
            shame_ok += 1

        if result["hr_flags"]:
            print(f"HR: {json_file.stem} — {len(result['hr_flags'])} HR issue(s)")
            for flag in result["hr_flags"]:
                print(f"  ⚠ {flag['sponsor']}: {flag['issue']} ({flag['database']})")
        elif result["errors"]:
            print(f"FAIL: {json_file.stem} — {', '.join(result['errors'])}")
        elif result["warnings"]:
            print(f"WARN: {json_file.stem} — {', '.join(result['warnings'])}")
        else:
            print(f"PASS: {json_file.stem}")

    results["summary"] = {
        "total_teams": total_teams,
        "verified": verified_teams,
        "verification_rate": round(verified_teams / total_teams * 100, 1) if total_teams > 0 else 0,
        "total_errors": total_errors,
        "total_warnings": total_warnings,
        "total_hr_flags": total_hr_flags,
        "contact_present": contact_ok,
        "shame_present": shame_ok,
    }

    # Save verified data
    output_file = VERIFIED_DIR / "verified_data.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved verified data to {output_file}")

    # Print summary
    print(f"\n=== Quality Verification ===")
    print(f"Total teams checked: {total_teams}")
    print(f"Verified: {verified_teams} ({results['summary']['verification_rate']}%)")
    print(f"Errors: {total_errors}")
    print(f"Warnings: {total_warnings}")
    print(f"HR flags: {total_hr_flags}")
    print(f"Contact info present: {contact_ok}/{total_teams}")
    print(f"Shame methods present: {shame_ok}/{total_teams}")

if __name__ == "__main__":
    main()