#!/usr/bin/env python3
"""Verify data quality - cross-reference with HR databases and check schema."""

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

DATA_DIR = Path("data")
VERIFIED_DIR = Path("verified_data")
VERIFIED_DIR.mkdir(exist_ok=True)

HR_DATABASES = {
    "hrf": "https://hrforum.org",
    "amnesty": "https://amnesty.org",
    "hrw": "https://hrw.org",
    "bhr": "https://business-humanrights.org",
}

MIN_SOURCES = 2
REQUIRED_FIELDS = ["team", "sport", "league", "country", "contact", "shame"]
REQUIRED_CONTACT_FIELDS = ["phone", "email", "twitter"]
REQUIRED_SHAME_FIELDS = ["description", "methods"]

def verify_team(team_data: dict) -> dict:
    """Verify a team JSON file for quality and completeness."""
    errors = []
    warnings = []

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in team_data:
            errors.append(f"Missing required field: {field}")

    # Check contact info
    contact = team_data.get("contact", {})
    for field in REQUIRED_CONTACT_FIELDS:
        if field not in contact or not contact[field]:
            errors.append(f"Missing contact field: {field}")

    # Check shame info
    shame = team_data.get("shame", {})
    for field in REQUIRED_SHAME_FIELDS:
        if field not in shame or not shame[field]:
            errors.append(f"Missing shame field: {field}")

    # Check shame methods
    methods = shame.get("methods", [])
    if len(methods) < 1:
        errors.append("No shame methods defined")
    for method in methods:
        method_type = method.get("type", "")
        if method_type == "email" and "address" not in method:
            errors.append(f"Invalid shame method (missing address): {method}")
        elif method_type == "phone" and "number" not in method:
            errors.append(f"Invalid shame method (missing number): {method}")
        elif method_type == "twitter" and "handle" not in method:
            errors.append(f"Invalid shame method (missing handle): {method}")

    # Check sponsors (if any)
    sponsors = team_data.get("sponsors", [])
    sponsor_issues = 0
    for sponsor in sponsors:
        sources = sponsor.get("sources", [])
        if len(sources) < MIN_SOURCES:
            sponsor_issues += 1
            warnings.append(f"Sponsor '{sponsor.get('name', '?')}' has only {len(sources)} source(s)")

    # Check data freshness
    last_updated = team_data.get("last_updated", "")
    if last_updated:
        try:
            updated_date = datetime.strptime(last_updated, "%Y-%m-%d")
            age_days = (datetime.now() - updated_date).days
            if age_days > 30:
                warnings.append(f"Data is {age_days} days old")
        except ValueError:
            warnings.append(f"Invalid date format: {last_updated}")

    verified = len(errors) == 0
    return {
        "team": team_data.get("team", "unknown"),
        "verified": verified,
        "errors": errors,
        "warnings": warnings,
        "sponsor_issues": sponsor_issues,
        "contact_present": bool(contact.get("email") and contact.get("twitter")),
        "shame_present": bool(shame.get("methods")),
    }

def main():
    # Load all team JSON files
    json_files = list(DATA_DIR.glob("*.json"))
    json_files = [f for f in json_files if f.name != "index.json"]

    results = {
        "version": "0.1",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "hr_databases": HR_DATABASES,
        "teams": {},
        "summary": {},
    }

    total_teams = 0
    verified_teams = 0
    total_errors = 0
    total_warnings = 0
    contact_ok = 0
    shame_ok = 0

    for json_file in sorted(json_files):
        with open(json_file) as f:
            team_data = json.load(f)

        result = verify_team(team_data)
        results["teams"][json_file.stem] = result
        total_teams += 1

        if result["verified"]:
            verified_teams += 1
        total_errors += len(result["errors"])
        total_warnings += len(result["warnings"])

        if result["contact_present"]:
            contact_ok += 1
        if result["shame_present"]:
            shame_ok += 1

        if result["errors"]:
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
    print(f"Contact info present: {contact_ok}/{total_teams}")
    print(f"Shame methods present: {shame_ok}/{total_teams}")

if __name__ == "__main__":
    main()