from flask import Blueprint

properties_bp = Blueprint(
    "properties",
    __name__,
    url_prefix="/api/properties"
)

@properties_bp.get("/")
def get_properties():

    return {
        "message": "Not implemented"
    }, 501

@properties_bp.get("/<id>")
def get_property(id):

    return {
        "message": "Not implemented"
    }, 501


@properties_bp.post("/")
def get_property():

    return {
        "message": "Not implemented"
    }, 501
