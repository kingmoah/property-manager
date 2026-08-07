from flask import Blueprint
from flask import request

from repositories.mock.mock_property_repository import (
    MockPropertyRepository
)
from services.property_service import (
    PropertyService
)

property_bp = Blueprint(
    "properties",
    __name__,
    url_prefix="/api/properties"
)

property_repository = MockPropertyRepository()

property_service = PropertyService(
    property_repository
)


@property_bp.get("/")
def get_properties():

    properties = property_service.get_all_properties()

    return [
        {
            "id": property.id,
            "name": property.name,
            "address": property.address,
            "city": property.city,
            "province": property.province,
            "postal_code": property.postal_code
        }
        for property in properties
    ]


@property_bp.get("/<int:property_id>")
def get_property(property_id):

    property = property_service.get_property(
        property_id
    )

    if property is None:
        return {
            "message": "Property not found"
        }, 404

    return {
        "id": property.id,
        "name": property.name,
        "address": property.address,
        "city": property.city,
        "province": property.province,
        "postal_code": property.postal_code
    }


@property_bp.post("/")
def create_property():

    data = request.get_json()

    required = [
        "name",
        "address",
        "city",
        "province",
        "postal_code"
    ]

    for field in required:
        if field not in data:
            return {
                "message": f"Missing field '{field}'"
            }, 400

    property = property_service.create_property(
        data["name"],
        data["address"],
        data["city"],
        data["province"],
        data["postal_code"]
    )

    return {
        "id": property.id,
        "name": property.name,
        "address": property.address,
        "city": property.city,
        "province": property.province,
        "postal_code": property.postal_code
    }, 201


@property_bp.patch("/<int:property_id>")
def update_property(property_id):

    data = request.get_json()

    property = property_service.update_property(
        property_id,
        data.get("name"),
        data.get("address"),
        data.get("city"),
        data.get("province"),
        data.get("postal_code")
    )

    if property is None:
        return {
            "message": "Property not found"
        }, 404

    return {
        "id": property.id,
        "name": property.name,
        "address": property.address,
        "city": property.city,
        "province": property.province,
        "postal_code": property.postal_code
    }


@property_bp.delete("/<int:property_id>")
def delete_property(property_id):

    deleted = property_service.delete_property(
        property_id
    )

    if not deleted:
        return {
            "message": "Property not found"
        }, 404

    return "", 204