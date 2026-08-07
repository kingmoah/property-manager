from repositories.mock.mock_tenant_repository import MockTenantRepository
from services.tenant_service import TenantService

tenant_repository = MockTenantRepository()

tenant_service = TenantService(
    tenant_repository
)