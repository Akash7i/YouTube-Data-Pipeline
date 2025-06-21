from datetime import datetime
import pandas as pd
import os

def clean_data():
    # Sample dummy data for testing
    data = {'title': ['Video 1', 'Video 2'], 'views': [1000, 2000]}
    df = pd.DataFrame(data)

    # Ensure 'data/cleaned/' folder exists
    os.makedirs('data/cleaned', exist_ok=True)

    # Generate filename with today's date
    today = datetime.now().strftime('%Y-%m-%d')
    file_path = f"data/cleaned/cleaned_data_{today}.csv"

    # Save to CSV
    df.to_csv(file_path, index=False)
    print(f"✅ Cleaned data saved to {file_path}")
