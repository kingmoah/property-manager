class LeaseService:

    def __init__(self, repository):
        self._repository = repository

    def get_all_leases(self):
        return self._repository.get_all()

    def create_lease(self, lease):
        return self._repository.create(lease)
    
    def get_lease(self, id):
        return self._repository.get_by_id(id)