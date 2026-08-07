class MockPaymentRepository:

    def __init__(self):
        self._payments = []
        self._next_id = 1

    def get_all(self):
        return self._payments

    def get_by_id(self, payment_id):

        for payment in self._payments:

            if payment.id == payment_id:
                return payment

        return None

    def create(self, payment):

        payment.id = self._next_id

        self._next_id += 1

        self._payments.append(payment)

        return payment

    def update(
        self,
        payment_id,
        lease_id=None,
        amount=None,
        payment_date=None,
        payment_method=None,
        reference=None
    ):

        payment = self.get_by_id(payment_id)

        if payment is None:
            return None

        if lease_id is not None:
            payment.lease_id = lease_id

        if amount is not None:
            payment.amount = amount

        if payment_date is not None:
            payment.payment_date = payment_date

        if payment_method is not None:
            payment.payment_method = payment_method

        if reference is not None:
            payment.reference = reference

        return payment

    def delete(self, payment_id):

        payment = self.get_by_id(payment_id)

        if payment is None:
            return False

        self._payments.remove(payment)

        return True