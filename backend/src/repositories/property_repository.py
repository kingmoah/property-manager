class PropertyRepository:

    def get_all(self):
        raise NotImplementedError()

    def get_by_id(self, tenant_id):
        raise NotImplementedError()

    def create(self, tenant):
        raise NotImplementedError()

    def delete(self, tenant_id):
        raise NotImplementedError()