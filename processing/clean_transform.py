import re
import pandas as pd
from datetime import datetime

def clean_data(scholarship):
    cleaned = {}

    cleaned["title"] = scholarship.get("title", "").strip() or "No Title Provided"
    cleaned["country"] = scholarship.get("country", "").strip() or "Unknown"
    cleaned["source"] = scholarship.get("source", "").strip() or "Unknown"
    cleaned["link"] = scholarship.get("link", "").strip() or "N/A"

    # Clean amount
    amount = scholarship.get("amount", "N/A")
    cleaned["amount"] = re.sub(r"\s+", " ", amount).strip()

    # Normalize deadline
    raw_deadline = scholarship.get("deadline", "").strip()
    try:
        parsed_date = pd.to_datetime(raw_deadline, errors='coerce')
        cleaned["deadline"] = parsed_date.strftime('%Y-%m-%d') if not pd.isnull(parsed_date) else "Unknown"
    except:
        cleaned["deadline"] = "Unknown"

    return cleaned

if __name__ == "__main__":
    test_data = {
        "title": "   Global Tech Scholars Program ",
        "deadline": "2025-01-31",
        "amount": " € 8000 ",
        "country": "Germany ",
        "link": "https://example.com/scholarship",
        "source": "ScholarshipPortal"
    }
    print(clean_data(test_data))

