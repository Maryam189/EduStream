def scrape_mock():
    scholarships = [
        {
            "title": "Global Tech Scholars Program",
            "deadline": "2025-01-31",
            "amount": "€8,000 per year",
            "country": "Germany",
            "link": "https://www.scholarshipportal.com/scholarship/global-tech-scholars",
            "source": "ScholarshipPortal"
        },
        {
            "title": "Women in STEM Excellence Award",
            "deadline": "2024-12-15",
            "amount": "$10,000",
            "country": "USA",
            "link": "https://www.scholarshipportal.com/scholarship/women-in-stem-excellence-award",
            "source": "ScholarshipPortal"
        },
        {
            "title": "Undergraduate Arts Talent Grant",
            "deadline": "2025-02-10",
            "amount": "$5,000",
            "country": "UK",
            "link": "https://www.scholarshipportal.com/scholarship/arts-talent-grant",
            "source": "ScholarshipPortal"
        },
        {
            "title": "Canadian Research Masters Fellowship",
            "deadline": "2025-03-01",
            "amount": "CAD 15,000",
            "country": "Canada",
            "link": "https://www.scholarshipportal.com/scholarship/canadian-research-fellowship",
            "source": "ScholarshipPortal"
        },
        {
            "title": "Asia Pacific Leadership Scholarship",
            "deadline": "2024-11-30",
            "amount": "$7,500",
            "country": "Australia",
            "link": "https://www.scholarshipportal.com/scholarship/apac-leadership-scholarship",
            "source": "ScholarshipPortal"
        }
    ]
    return scholarships

if __name__ == "__main__":
    for scholarship in scrape_mock():
        print(scholarship)

