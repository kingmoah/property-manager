from flask import Blueprint
from flask import request

from container import tenant_service

tenant_bp = Blueprint(
    "tenants",
    __name__,
    url_prefix="/api/tenants"
)


@tenant_bp.get("/")
def get_tenants():

    tenants = tenant_service.get_all_tenants()

    return [
        {
            "id": t.id,
            "first_name": t.first_name,
            "last_name": t.last_name,
            "phone_number": t.phone_number,
            "email": t.email
        }
        for t in tenants
    ]

@tenant_bp.get("/<int:tenant_id>")
def get_tenant(tenant_id):

    tenant = tenant_service.get_tenant(tenant_id)

    if tenant is None:
        return {
            "message": "Tenant not found"
        }, 404

    return {
        "id": tenant.id,
        "first_name": tenant.first_name,
        "last_name": tenant.last_name,
        "phone_number": tenant.phone_number,
        "email": tenant.email
    }

@tenant_bp.post("/")
def create_tenant():

    data = request.get_json()
    
    #should i do 
    tenant = tenant_service.create_tenant(
        data["first_name"],
        data["last_name"],
        data["phone_number"],
        data["email"]
    )


    return {
        "id": tenant.id,
        "first_name": tenant.first_name,
        "last_name": tenant.last_name,
        "phone_number": tenant.phone_number,
        "email": tenant.email
    }, 201

@tenant_bp.delete("/<int:tenant_id>")
def delete_tenant(tenant_id):

    deleted = tenant_service.delete_tenant(
        tenant_id
    )

    if not deleted:
        return {
            "message": "Tenant not found"
        }, 404

    return {
        "message": "Tenant deleted"
    }


@tenant_bp.patch("/<int:tenant_id>")
def update_tenant(tenant_id):

    data = request.get_json()

    tenant = tenant_service.update_tenant(
        tenant_id,
        data.get("first_name"),
        data.get("last_name"),
        data.get("phone_number"),
        data.get("email")
    )

    if tenant is None:
        return {
            "message": "Tenant not found"
        }, 404

    return {
        "id": tenant.id,
        "first_name": tenant.first_name,
        "last_name": tenant.last_name,
        "phone_number": tenant.phone_number,
        "email": tenant.email
    }