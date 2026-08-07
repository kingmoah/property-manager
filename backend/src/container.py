from repositories.mock.mock_tenant_repository import (
    MockTenantRepository
)

from repositories.mock.mock_property_repository import (
    MockPropertyRepository
)

from repositories.mock.mock_lease_repository import (
    MockLeaseRepository
)

from repositories.mock.mock_payment_repository import (
    MockPaymentRepository
)

from services.tenant_service import (
    TenantService
)

from services.property_service import (
    PropertyService
)

from services.lease_service import (
    LeaseService
)

from services.payment_service import (
    PaymentService
)


class Container:

    def __init__(self):

        self.tenant_repository = (
            MockTenantRepository()
        )

        self.property_repository = (
            MockPropertyRepository()
        )

        self.lease_repository = (
            MockLeaseRepository()
        )

        self.payment_repository = (
            MockPaymentRepository()
        )

        self.tenant_service = (
            TenantService(
                self.tenant_repository
            )
        )

        self.property_service = (
            PropertyService(
                self.property_repository
            )
        )

        self.lease_service = (
            LeaseService(
                self.lease_repository
            )
        )

        self.payment_service = (
            PaymentService(
                self.payment_repository
            )
        )


container = Container()