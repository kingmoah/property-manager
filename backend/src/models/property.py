class Property:

    def __init__(
        self,
        property_id,
        name,
        address,
        city,
        province,
        postal_code
    ):
        self.id = property_id
        self.name = name
        self.address = address
        self.city = city
        self.province = province
        self.postal_code = postal_code