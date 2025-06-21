from flask import Flask
from yt_fetch import fetch_data
from clean_data import clean_data
from store_data import store_data

app = Flask(__name__)

@app.route('/')
def home():
    return "<h3>Welcome! Use <a href='/run_pipeline'>/run_pipeline</a> to run the data pipeline.</h3>"

@app.route('/run_pipeline')
def run_pipeline():
    fetch_data()
    clean_data()
    store_data()
    return "✅ Data pipeline completed and stored in DB!"

if __name__ == "__main__":
    app.run(debug=True)
