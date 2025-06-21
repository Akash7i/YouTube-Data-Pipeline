import pandas as pd
import mysql.connector
from datetime import datetime

def store_data():
    today = datetime.now().strftime('%Y-%m-%d')
    file_path = f"data/cleaned/cleaned_data_{today}.csv"
    df = pd.read_csv(file_path)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akashmuthu",
        database="youtube_data"
    )

    cursor = conn.cursor()

    # Insert data only for title and views
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO youtube_trending (title, views)
            VALUES (%s, %s)
        """, (
            row['title'],
            int(row['views'])
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print("[✔] Data stored in MySQL database.")
