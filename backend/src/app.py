from flask import Flask

from config import Config
from database import Database

from models.database.db_models import Base

from routes.health import health_bp
from routes.tenants import tenant_bp
from routes.properties import property_bp
from routes.leases import lease_bp
from routes.payments import payment_bp


# --------------------------------------------------
# Database
# --------------------------------------------------

database = Database(
    Config.DATABASE_URL
)

Base.metadata.create_all(
    bind=database.engine
)

# --------------------------------------------------
# Flask
# --------------------------------------------------

app = Flask(__name__)

app.register_blueprint(
    health_bp
)

app.register_blueprint(
    tenant_bp
)

app.register_blueprint(
    property_bp
)

app.register_blueprint(
    lease_bp
)

app.register_blueprint(
    payment_bp
)

# --------------------------------------------------
# Application Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )