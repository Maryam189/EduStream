from kafka import KafkaProducer
import json
import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scrapers.hec_scrapers import scrape_hec
from scrapers.daad_germany_scraper import scrape_daad
from scrapers.scholarshipportal_mock import scrape_mock

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Get scraped data
scholarships = scrape_hec() + scrape_daad() + scrape_mock()

# Send each scholarship to Kafka
for item in scholarships:
    print(f"Producing: {item['title']}")
    producer.send("scholarships-topic", value=item)

producer.flush()
print("✅ Produced all scholarship data to Kafka.")

