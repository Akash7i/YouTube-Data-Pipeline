import pandas as pd
from db_config import get_connection

def store_data(cleaned_path):
    df = pd.read_csv(cleaned_path)
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS youtube_trending (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT,
            views BIGINT
        )
    """)

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO youtube_trending (title, views)
            VALUES (%s, %s)
        """, (row['title'], int(row['views'])))

    conn.commit()
    cursor.close()
    conn.close()

def fetch_top_videos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT title, views FROM youtube_trending ORDER BY views DESC LIMIT 5")
    videos = cursor.fetchall()

    cursor.close()
    conn.close()
    return videos
