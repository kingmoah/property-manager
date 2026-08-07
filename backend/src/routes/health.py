from flask import Blueprint, jsonify
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

import database

health_bp = Blueprint(
    "health",
    __name__
)

@health_bp.get("/health")
def health():
    return jsonify({
        "status": "ok"
    })

@health_bp.get("/db-test")
def db_test():
    try:

        with database.engine.connect() as connection:

            version = connection.execute(
                text("SELECT version();")
            ).scalar_one()

        return jsonify({
            "status": "ok",
            "postgres": version
        })

    except SQLAlchemyError as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500