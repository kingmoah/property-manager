import re

from models.tenant import Tenant


class TenantService:

    EMAIL_REGEX = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    def __init__(self, repository):
        self._repository = repository

    def get_all_tenants(self):
        return self._repository.get_all()

    def get_tenant(self, tenant_id):
        return self._repository.get_by_id(tenant_id)

    def create_tenant(
        self,
        first_name,
        last_name,
        phone_number,
        email
    ):

        email = self.validate_email(email)

        tenant = Tenant(
            0,
            first_name,
            last_name,
            phone_number,
            email
        )

        return self._repository.create(tenant)

    def delete_tenant(self, tenant_id):
        return self._repository.delete(tenant_id)

    def update_tenant(
        self,
        tenant_id,
        first_name=None,
        last_name=None,
        phone_number=None,
        email=None
    ):

        email = (
            self.validate_email(email)
            if email is not None
            else None
        )

        return self._repository.update(
            tenant_id,
            first_name,
            last_name,
            phone_number,
            email
        )

    def validate_email(self, email):

        if not self.EMAIL_REGEX.fullmatch(email):
            raise ValueError(
                f"Invalid email address: {email}"
            )

        return email