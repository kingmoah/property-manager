class TenantRepository:

    def get_all(self):
        raise NotImplementedError()

    def get_by_id(self, tenant_id):
        raise NotImplementedError()

    def create(self, tenant):
        raise NotImplementedError()

    def delete(self, tenant_id):
        raise NotImplementedError()
    
    def update(
        self,
        tenant_id,
        first_name=None,
        last_name=None,
        phone_number=None,
        email=None
    ):
        raise NotImplementedError()