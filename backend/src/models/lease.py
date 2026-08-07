class Lease:

    def __init__(
        self,
        lease_id,
        tenant_id,
        property_id,
        start_date,
        end_date,
        monthly_rent
    ):
        self.id = lease_id
        self.tenant_id = tenant_id
        self.property_id = property_id
        self.start_date = start_date
        self.end_date = end_date
        self.monthly_rent = monthly_rent