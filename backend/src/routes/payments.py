from flask import Blueprint
from flask import request

from repositories.mock.mock_payment_repository import (
    MockPaymentRepository
)

from services.payment_service import (
    PaymentService
)

payment_bp = Blueprint(
    "payments",
    __name__,
    url_prefix="/api/payments"
)

payment_repository = MockPaymentRepository()

payment_service = PaymentService(
    payment_repository
)


@payment_bp.get("/")
def get_payments():

    payments = payment_service.get_all_payments()

    return [
        {
            "id": payment.id,
            "lease_id": payment.lease_id,
            "amount": payment.amount,
            "payment_date": payment.payment_date,
            "payment_method": payment.payment_method,
            "reference": payment.reference
        }
        for payment in payments
    ]


@payment_bp.get("/<int:payment_id>")
def get_payment(payment_id):

    payment = payment_service.get_payment(
        payment_id
    )

    if payment is None:
        return {
            "message": "Payment not found"
        }, 404

    return {
        "id": payment.id,
        "lease_id": payment.lease_id,
        "amount": payment.amount,
        "payment_date": payment.payment_date,
        "payment_method": payment.payment_method,
        "reference": payment.reference
    }


@payment_bp.post("/")
def create_payment():

    data = request.get_json()

    payment = payment_service.create_payment(
        data["lease_id"],
        data["amount"],
        data["payment_date"],
        data["payment_method"],
        data.get("reference")
    )

    return {
        "id": payment.id,
        "lease_id": payment.lease_id,
        "amount": payment.amount,
        "payment_date": payment.payment_date,
        "payment_method": payment.payment_method,
        "reference": payment.reference
    }, 201


@payment_bp.patch("/<int:payment_id>")
def update_payment(payment_id):

    data = request.get_json()

    payment = payment_service.update_payment(
        payment_id,
        data.get("lease_id"),
        data.get("amount"),
        data.get("payment_date"),
        data.get("payment_method"),
        data.get("reference")
    )

    if payment is None:
        return {
            "message": "Payment not found"
        }, 404

    return {
        "id": payment.id,
        "lease_id": payment.lease_id,
        "amount": payment.amount,
        "payment_date": payment.payment_date,
        "payment_method": payment.payment_method,
        "reference": payment.reference
    }


@payment_bp.delete("/<int:payment_id>")
def delete_payment(payment_id):

    deleted = payment_service.delete_payment(
        payment_id
    )

    if not deleted:
        return {
            "message": "Payment not found"
        }, 404

    return "", 204