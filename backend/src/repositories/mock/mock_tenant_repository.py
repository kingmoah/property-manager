from models.tenant import Tenant


class MockTenantRepository:

    def __init__(self):

        self._tenants = [
            Tenant(
                1,
                "John",
                "Smith",
                "0821111111",
                "john@example.com"
            ),
            Tenant(
                2,
                "Jane",
                "Doe",
                "0822222222",
                "jane@example.com"
            )
        ]
        self._next_id = 3

    def get_all(self):
        return self._tenants

    def get_by_id(self, tenant_id):

        for tenant in self._tenants:

            if tenant.id == tenant_id:
                return tenant

        return None

    def create(
        self,
        tenant
    ):

        tenant.id = self._next_id

        self._next_id += 1

        self._tenants.append(tenant)

        return tenant

    def delete(self, tenant_id):

        tenant = self.get_by_id(tenant_id)

        if tenant is None:
            return False

        self._tenants.remove(tenant)

        return True
    
    def update(
        self,
        tenant_id,
        first_name=None,
        last_name=None,
        phone_number=None,
        email=None
    ):

        tenant = self.get_by_id(tenant_id)

        if tenant is None:
            return None

        if first_name is not None:
            tenant.first_name = first_name

        if last_name is not None:
            tenant.last_name = last_name

        if phone_number is not None:
            tenant.phone_number = phone_number

        if email is not None:
            tenant.email = email

        return tenant