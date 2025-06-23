from kafka import KafkaConsumer
import json
import sys
import os
import csv

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from processing.clean_transform import clean_data
from processing.schema_validation import is_valid_schema  # ✅ Import schema validator

# Kafka consumer setup
consumer = KafkaConsumer(
    'scholarships-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='edustream-group-v2',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

output_file = 'data/sample_scholarships.csv'
fieldnames = ["title", "deadline", "amount", "country", "link", "source"]

# Check if file already exists
write_header = not os.path.exists(output_file)

# Open file in append mode
with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header if file is new
    if write_header:
        writer.writeheader()

    print("🔁 Waiting for scholarship data...")
    for msg in consumer:
        try:
            print("🔹 Received raw:", msg.value)
            cleaned = clean_data(msg.value)
            print("✅ Cleaned:", cleaned)

            # ✅ Schema validation
            if not is_valid_schema(cleaned):
                print("⚠️ Skipped invalid schema:", cleaned)
                continue

            writer.writerow(cleaned)
            print(f"📝 Saved: {cleaned.get('title', '')}")
        except Exception as e:
            print(f"❌ Error processing message: {e}")

