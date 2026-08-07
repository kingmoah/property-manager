from models.lease import Lease


class LeaseService:

    def __init__(self, repository):
        self._repository = repository

    def get_all_leases(self):
        return self._repository.get_all()

    def get_lease(self, lease_id):
        return self._repository.get_by_id(lease_id)

    def create_lease(
        self,
        tenant_id,
        property_id,
        start_date,
        end_date,
        monthly_rent
    ):

        lease = Lease(
            0,
            tenant_id,
            property_id,
            start_date,
            end_date,
            monthly_rent
        )

        return self._repository.create(lease)

    def update_lease(
        self,
        lease_id,
        tenant_id=None,
        property_id=None,
        start_date=None,
        end_date=None,
        monthly_rent=None
    ):

        return self._repository.update(
            lease_id,
            tenant_id,
            property_id,
            start_date,
            end_date,
            monthly_rent
        )

    def delete_lease(self, lease_id):
        return self._repository.delete(lease_id)