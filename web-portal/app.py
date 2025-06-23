from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_scholarships.csv')
    scholarships = []

    try:
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                scholarships.append(row)
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")

    return render_template('index.html', scholarships=scholarships)

if __name__ == '__main__':
    app.run(debug=True)

