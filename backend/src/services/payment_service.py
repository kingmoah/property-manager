from models.payment import Payment


class PaymentService:

    def __init__(self, repository):
        self._repository = repository

    def get_all_payments(self):
        return self._repository.get_all()

    def get_payment(self, payment_id):
        return self._repository.get_by_id(payment_id)

    def create_payment(
        self,
        lease_id,
        amount,
        payment_date,
        payment_method,
        reference
    ):

        payment = Payment(
            0,
            lease_id,
            amount,
            payment_date,
            payment_method,
            reference
        )

        return self._repository.create(payment)

    def update_payment(
        self,
        payment_id,
        lease_id=None,
        amount=None,
        payment_date=None,
        payment_method=None,
        reference=None
    ):

        return self._repository.update(
            payment_id,
            lease_id,
            amount,
            payment_date,
            payment_method,
            reference
        )

    def delete_payment(self, payment_id):
        return self._repository.delete(payment_id)