class PaymentService:

    def __init__(self, repository):
        self._repository = repository

    def get_all_payments(self):
        return self._repository.get_all()

    def create_payment(self, tenant):
        return self._repository.create(tenant)