from models.property import Property


class MockPropertyRepository:

    def __init__(self):
        self._properties = []
        self._next_id = 1
    
    def get_all(self):
        return self._properties

    def get_by_id(self, property_id):

        for property in self._properties:

            if property.id == property_id:
                return property

        return None

    def create(self, property):

        property.id = self._next_id

        self._next_id += 1

        self._properties.append(property)

        return property

    def delete(self, property_id):

        property = self.get_by_id(property_id)

        if property is None:
            return False

        self._properties.remove(property)

        return True

    def update(
        self,
        property_id,
        name=None,
        address=None,
        city=None,
        province=None,
        postal_code=None
    ):

        property = self.get_by_id(property_id)

        if property is None:
            return None

        if name is not None:
            property.name = name

        if address is not None:
            property.address = address

        if city is not None:
            property.city = city

        if province is not None:
            property.province = province

        if postal_code is not None:
            property.postal_code = postal_code

        return property