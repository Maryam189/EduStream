def is_valid_schema(data):
    required_keys = {
        "title": str,
        "deadline": str,
        "amount": str,
        "country": str,
        "link": str,
        "source": str
    }

    for key, expected_type in required_keys.items():
        if key not in data:
            print(f"❌ Missing key: {key}")
            return False
        if not isinstance(data[key], expected_type):
            print(f"❌ Invalid type for key '{key}': Expected {expected_type}, got {type(data[key])}")
            return False
        if not data[key].strip():
            print(f"❌ Empty value for key: {key}")
            return False

    return True

if __name__ == "__main__":
    sample = {
        "title": "Women in STEM",
        "deadline": "2025-02-15",
        "amount": "$10,000",
        "country": "USA",
        "link": "https://example.com",
        "source": "ScholarshipPortal"
    }

    print("✅ Schema Valid!" if is_valid_schema(sample) else "❌ Invalid Schema")

