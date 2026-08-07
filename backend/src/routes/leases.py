from flask import Blueprint
from flask import request

from repositories.mock.mock_lease_repository import (
    MockLeaseRepository
)

from services.lease_service import (
    LeaseService
)

lease_bp = Blueprint(
    "leases",
    __name__,
    url_prefix="/api/leases"
)

lease_repository = MockLeaseRepository()

lease_service = LeaseService(
    lease_repository
)


@lease_bp.get("/")
def get_leases():

    leases = lease_service.get_all_leases()

    return [
        {
            "id": lease.id,
            "tenant_id": lease.tenant_id,
            "property_id": lease.property_id,
            "start_date": lease.start_date,
            "end_date": lease.end_date,
            "monthly_rent": lease.monthly_rent
        }
        for lease in leases
    ]


@lease_bp.get("/<int:lease_id>")
def get_lease(lease_id):

    lease = lease_service.get_lease(
        lease_id
    )

    if lease is None:
        return {
            "message": "Lease not found"
        }, 404

    return {
        "id": lease.id,
        "tenant_id": lease.tenant_id,
        "property_id": lease.property_id,
        "start_date": lease.start_date,
        "end_date": lease.end_date,
        "monthly_rent": lease.monthly_rent
    }


@lease_bp.post("/")
def create_lease():

    data = request.get_json()

    lease = lease_service.create_lease(
        data["tenant_id"],
        data["property_id"],
        data["start_date"],
        data["end_date"],
        data["monthly_rent"]
    )

    return {
        "id": lease.id,
        "tenant_id": lease.tenant_id,
        "property_id": lease.property_id,
        "start_date": lease.start_date,
        "end_date": lease.end_date,
        "monthly_rent": lease.monthly_rent
    }, 201


@lease_bp.patch("/<int:lease_id>")
def update_lease(lease_id):

    data = request.get_json()

    lease = lease_service.update_lease(
        lease_id,
        data.get("tenant_id"),
        data.get("property_id"),
        data.get("start_date"),
        data.get("end_date"),
        data.get("monthly_rent")
    )

    if lease is None:
        return {
            "message": "Lease not found"
        }, 404

    return {
        "id": lease.id,
        "tenant_id": lease.tenant_id,
        "property_id": lease.property_id,
        "start_date": lease.start_date,
        "end_date": lease.end_date,
        "monthly_rent": lease.monthly_rent
    }


@lease_bp.delete("/<int:lease_id>")
def delete_lease(lease_id):

    deleted = lease_service.delete_lease(
        lease_id
    )

    if not deleted:
        return {
            "message": "Lease not found"
        }, 404

    return "", 204