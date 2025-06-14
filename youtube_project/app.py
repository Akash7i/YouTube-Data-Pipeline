from flask import Flask, render_template, request, send_file
from process_csv import clean_csv
from store_data import store_data
import os
from datetime import datetime
import mysql.connector

app = Flask(__name__)


UPLOAD_FOLDER = 'data/uploaded'
CLEANED_FOLDER = 'data/cleaned'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CLEANED_FOLDER, exist_ok=True)

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'akashmuthu',
    'database': 'youtube_db'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_pipeline', methods=['POST'])
def run_pipeline():
    if 'file' not in request.files:
        return "❌ No file part in the request.", 400

    file = request.files['file']
    if file.filename == '':
        return "❌ No selected file.", 400

    today = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    upload_path = os.path.join(UPLOAD_FOLDER, f"raw_{today}.csv")
    file.save(upload_path)

    cleaned_path = clean_csv(upload_path)
    store_data(cleaned_path)

    return render_template("success.html")

@app.route('/results')
def results():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)


        cursor.execute("SELECT title, views FROM youtube_data ORDER BY views DESC LIMIT 5")
        videos_raw = cursor.fetchall()

        cursor.close()
        conn.close()

        videos = [{"title": str(v["title"]), "views": int(v["views"])} for v in videos_raw]

        return render_template("results.html", videos=videos)

    except Exception as e:
        print("❌ Error fetching results:", e)
        return f"❌ Error fetching results: {str(e)}", 500

@app.route('/download')
def download():
    if not os.listdir(CLEANED_FOLDER):
        return "❌ No cleaned files available to download.", 404

 
    latest_file = sorted(
        [f for f in os.listdir(CLEANED_FOLDER) if f.endswith('.csv')],
        key=lambda x: os.path.getmtime(os.path.join(CLEANED_FOLDER, x))
    )[-1]

    return send_file(os.path.join(CLEANED_FOLDER, latest_file), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
