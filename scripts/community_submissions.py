#!/usr/bin/env python3
"""Community submissions handler — like pushtoleave.org's Google Forms approach."""

import json
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

SUBMISSIONS_DIR = Path("submissions")
SUBMISSIONS_DIR.mkdir(exist_ok=True)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def validate_submission(submission: dict) -> dict:
    """Validate a community submission."""
    errors = []
    required_fields = ["type", "team", "sponsor", "source", "reporter"]

    for field in required_fields:
        if field not in submission or not submission[field]:
            errors.append(f"Missing required field: {field}")

    # Validate submission type
    valid_types = ["sponsor", "contact", "hr_issue", "correction", "new_team"]
    if submission.get("type") not in valid_types:
        errors.append(f"Invalid type: {submission.get('type')}. Must be one of {valid_types}")

    # Generate submission ID
    submission_id = hashlib.sha256(
        json.dumps(submission, sort_keys=True).encode()
    ).hexdigest()[:12]

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "submission_id": submission_id,
    }

def process_submission(submission: dict) -> dict:
    """Process a validated submission and update the data."""
    submission_type = submission.get("type")
    team_name = submission.get("team", "").lower().replace(" ", "-")

    result = {
        "submission_id": submission.get("submission_id"),
        "type": submission_type,
        "team": submission.get("team"),
        "processed": False,
        "action": None,
    }

    if submission_type == "sponsor":
        # Add sponsor to team JSON
        team_file = DATA_DIR / f"{team_name}.json"
        if team_file.exists():
            with open(team_file) as f:
                team_data = json.load(f)

            team_data["sponsors"].append({
                "name": submission.get("sponsor"),
                "type": submission.get("sponsor_type", "company"),
                "category": submission.get("sponsor_category", "unknown"),
                "rating": "D",  # Default until verified
                "flags": [],
                "deal_value": submission.get("deal_value"),
                "sources": [submission.get("source")],
                "verified": False,
                "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            })

            with open(team_file, "w") as f:
                json.dump(team_data, f, indent=2)

            result["processed"] = True
            result["action"] = f"Added sponsor '{submission.get('sponsor')}' to {submission.get('team')}"
        else:
            result["action"] = f"Team file not found: {team_name}.json"

    elif submission_type == "hr_issue":
        # Flag HR issue for a sponsor
        team_file = DATA_DIR / f"{team_name}.json"
        if team_file.exists():
            with open(team_file) as f:
                team_data = json.load(f)

            sponsor_name = submission.get("sponsor", "")
            for sponsor in team_data.get("sponsors", []):
                if sponsor_name.lower() in sponsor.get("name", "").lower():
                    sponsor["flags"].append({
                        "type": "hr_issue",
                        "description": submission.get("description", ""),
                        "source": submission.get("source"),
                        "reported_at": datetime.now(timezone.utc).isoformat(),
                    })
                    sponsor["rating"] = "D"  # Downgrade rating
                    result["processed"] = True
                    result["action"] = f"Flagged HR issue for {sponsor_name} in {submission.get('team')}"
                    break

            if not result["processed"]:
                result["action"] = f"Sponsor '{sponsor_name}' not found in {submission.get('team')}"
        else:
            result["action"] = f"Team file not found: {team_name}.json"

    elif submission_type == "contact":
        # Update team contact info
        team_file = DATA_DIR / f"{team_name}.json"
        if team_file.exists():
            with open(team_file) as f:
                team_data = json.load(f)

            contact = team_data.get("contact", {})
            if submission.get("phone"):
                contact["phone"] = submission["phone"]
            if submission.get("email"):
                contact["email"] = submission["email"]
            if submission.get("twitter"):
                contact["twitter"] = submission["twitter"]

            team_data["contact"] = contact

            with open(team_file, "w") as f:
                json.dump(team_data, f, indent=2)

            result["processed"] = True
            result["action"] = f"Updated contact info for {submission.get('team')}"
        else:
            result["action"] = f"Team file not found: {team_name}.json"

    return result

def save_submission(submission: dict, validation: dict) -> Path:
    """Save submission to file for review."""
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{validation['submission_id']}.json"
    filepath = SUBMISSIONS_DIR / filename

    submission_data = {
        "submission_id": validation["submission_id"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "validation": validation,
        "submission": submission,
    }

    with open(filepath, "w") as f:
        json.dump(submission_data, f, indent=2)

    return filepath

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/community_submissions.py <submission.json>")
        print("Or: python3 scripts/community_submissions.py --demo")
        sys.exit(1)

    if sys.argv[1] == "--demo":
        # Create a demo submission
        submission = {
            "type": "sponsor",
            "team": "Manchester United",
            "sponsor": "Chevrolet",
            "sponsor_type": "company",
            "sponsor_category": "automotive",
            "deal_value": "$50M/year",
            "source": "https://www.manutd.com/en/club/commerce",
            "reporter": "demo@example.com",
            "description": "Chevrolet is the main jersey sponsor for Manchester United",
        }
    else:
        # Load submission from file
        submission_file = Path(sys.argv[1])
        with open(submission_file) as f:
            submission = json.load(f)

    # Validate submission
    validation = validate_submission(submission)
    print(f"Validation: {'PASS' if validation['valid'] else 'FAIL'}")
    print(f"Submission ID: {validation['submission_id']}")

    if validation["errors"]:
        print(f"Errors: {validation['errors']}")
        sys.exit(1)

    # Save submission
    filepath = save_submission(submission, validation)
    print(f"Saved to: {filepath}")

    # Process submission
    result = process_submission(submission)
    print(f"Action: {result['action']}")
    print(f"Processed: {result['processed']}")

if __name__ == "__main__":
    main()