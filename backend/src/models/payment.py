class Payment:

    def __init__(
        self,
        payment_id,
        lease_id,
        amount,
        payment_date,
        payment_method,
        reference
    ):
        self.id = payment_id
        self.lease_id = lease_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.reference = reference