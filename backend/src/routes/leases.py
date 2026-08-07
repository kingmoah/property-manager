from flask import Blueprint

leases_bp = Blueprint(
    "leases",
    __name__,
    url_prefix="/api/leases"
)

@tenant_bp.get("/")
def get_leases():

    return {
        "message": "Not implemented"
    }, 501