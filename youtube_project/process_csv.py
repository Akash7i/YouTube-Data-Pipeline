import pandas as pd
import os
from datetime import datetime

def clean_csv(file_path):
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:

        df = pd.read_csv(file_path, encoding='latin1')


    df.dropna(subset=['title', 'views'], inplace=True)

 
    df['views'] = pd.to_numeric(df['views'], errors='coerce')
    df.dropna(subset=['views'], inplace=True)


    today = datetime.now().strftime('%Y-%m-%d')
    cleaned_path = os.path.join('data', 'cleaned', f'cleaned_data_{today}.csv')
    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
    df.to_csv(cleaned_path, index=False)

    return cleaned_path
