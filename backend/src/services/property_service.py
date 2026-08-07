from models.property import Property


class PropertyService:

    def __init__(self, repository):
        self._repository = repository

    def get_all_properties(self):
        return self._repository.get_all()

    def get_property(self, property_id):
        return self._repository.get_by_id(property_id)

    def create_property(
        self,
        name,
        address,
        city,
        province,
        postal_code
    ):

        property = Property(
            0,
            name,
            address,
            city,
            province,
            postal_code
        )

        return self._repository.create(property)

    def update_property(
        self,
        property_id,
        name=None,
        address=None,
        city=None,
        province=None,
        postal_code=None
    ):

        return self._repository.update(
            property_id,
            name,
            address,
            city,
            province,
            postal_code
        )

    def delete_property(self, property_id):
        return self._repository.delete(property_id)