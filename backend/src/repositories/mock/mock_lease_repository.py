class MockLeaseRepository:

    def __init__(self):
        self._leases = []
        self._next_id = 1

    def get_all(self):
        return self._leases

    def get_by_id(self, lease_id):

        for lease in self._leases:

            if lease.id == lease_id:
                return lease

        return None

    def create(self, lease):

        lease.id = self._next_id

        self._next_id += 1

        self._leases.append(lease)

        return lease

    def update(
        self,
        lease_id,
        tenant_id=None,
        property_id=None,
        start_date=None,
        end_date=None,
        monthly_rent=None
    ):

        lease = self.get_by_id(lease_id)

        if lease is None:
            return None

        if tenant_id is not None:
            lease.tenant_id = tenant_id

        if property_id is not None:
            lease.property_id = property_id

        if start_date is not None:
            lease.start_date = start_date

        if end_date is not None:
            lease.end_date = end_date

        if monthly_rent is not None:
            lease.monthly_rent = monthly_rent

        return lease

    def delete(self, lease_id):

        lease = self.get_by_id(lease_id)

        if lease is None:
            return False

        self._leases.remove(lease)

        return True