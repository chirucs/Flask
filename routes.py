from flask_restful import Api
from constants import *
from api import *

BASE_ROUTE = "/beer-company"
BEER_COMPANY_ID_ROUTE = f"{BASE_ROUTE}/<string:beer_company_id>"

ROUTES = {
    CREATE_BEER_COMPANY: BASE_ROUTE,
    "GetBeerCompany": BEER_COMPANY_ID_ROUTE,
    "UpdateBeerCompany": BEER_COMPANY_ID_ROUTE,
    "DeleteBeerCompany": BEER_COMPANY_ID_ROUTE,
    "ListBeerCompanies": "/beer-companies"
}

METHODS= {
    CREATE_BEER_COMPANY: "POST",
    "GetBeerCompany": "GET",
    "UpdateBeerCompany": "PUT",
    "DeleteBeerCompany": "DELETE",
    "ListBeerCompanies": "GET"
}

RESOURCES = {
    CREATE_BEER_COMPANY: CreateBeerCompany,
    "GetBeerCompany": GetBeerCompany,
    "UpdateBeerCompany": UpdateBeerCompany,
    "DeleteBeerCompany": DeleteBeerCompany,
    "ListBeerCompanies": ListBeerCompanies
}

def init_routes(api: Api) -> None:
    for [api_name, resource] in RESOURCES.items():
        api.add_resource(resource, ROUTES[api_name], methods=[METHODS[api_name]])