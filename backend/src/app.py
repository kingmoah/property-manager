from flask import Flask

from config import Config
from database import initialize_database

initialize_database(Config.DATABASE_URL)

app = Flask(__name__)

@app.route("/health")
def health():
    return {
        "status": "ok"
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )