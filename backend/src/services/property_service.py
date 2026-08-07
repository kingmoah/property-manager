class PropertyService:

    def __init__(self, repository):
        self._repository = repository

    def get_all_properties(self):
        return self._repository.get_all()

    def create_property(self, property):
        return self._repository.create(property)

    def update_tenant(
        self,
        tenant_id,
        first_name=None,
        last_name=None,
        phone_number=None,
        email=None
    ):
        return self._repository.update(
            tenant_id,
            first_name,
            last_name,
            phone_number,
            email
        )