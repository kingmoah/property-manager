from flask import Flask

from config import Config
from database import initialize_database
from routes.health import health_bp
from routes.tenants import tenant_bp


initialize_database(Config.DATABASE_URL)

app = Flask(__name__)

app.register_blueprint(health_bp)
app.register_blueprint(tenant_bp)

for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )