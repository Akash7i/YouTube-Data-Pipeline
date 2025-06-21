import requests
import json
import os
from datetime import datetime

def fetch_data():
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&regionCode=IN&maxResults=10&key={api_key}"

    response = requests.get(url)
    data = response.json()

    today = datetime.now().strftime('%Y-%m-%d')
    os.makedirs("data/raw", exist_ok=True)
    with open(f"data/raw/raw_data_{today}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("✅ Data fetched and saved.")
