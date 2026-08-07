from flask import Blueprint

payments_bp = Blueprint(
    "payments",
    __name__,
    url_prefix="/api/payments"
)

@tenant_bp.get("/")
def get_payments():

    return {
        "message": "Not implemented"
    }, 501