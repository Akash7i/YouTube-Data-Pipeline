import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="akashmuthu",
        database="youtube_data"
    )
