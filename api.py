'''This file sets up a set of API endpoints for managing 
beer companies using Flask-RESTful. It allows you to create,
 get, update, delete, and list beer companies.
   The data is stored in a simple companies dictionary
     in memory (not in a database), making it easy to
       experiment and learn.'''


#reqparse: A tool from Flask-RESTful to parse and validate incoming request data.
from flask_restful import reqparse,Resource
#uuid4: Generates a unique ID for each company, which is useful for uniquely identifying companies.
from uuid import uuid4 as generateId

#data storage
#companies: A dictionary that holds all the beer companies. Each company will be stored with a unique ID as the key.
companies={}

#creating a beer company

#Request Parser for Creating Companies
create_beer_company_parser = (reqparse.RequestParser()
    .add_argument("name", type=str, required=True)
    .add_argument("description", type=str, required=False))

class CreateBeerCompany(Resource):
    def post(self):
        name,description=create_beer_company_parser.parse_args().values()
        id=str(generateId)
        companies[id] = {
            "id":id,
            "name":name,
            "description": description,
            "numberofBeers":0
        }
        return companies[id], 200
    
class GetBeerCompany(Resource):
    def get(self, beer_company_id):
        beer_company = companies.get(beer_company_id)
        if beer_company is None:
            return { "message": "No company found" }, 404
        return beer_company, 200
    
update_beer_company_parser = (reqparse.RequestParser()
    .add_argument("name", type=str, required=False)
    .add_argument("description", type=str, required=False))

class UpdateBeerCompany(Resource):
    def put(self, beer_company_id):
        name, description = update_beer_company_parser.parse_args().values()
        beer_company = companies.get(beer_company_id)
        if beer_company is None:
            return { "message": "No company found" }, 404
        if name is not None:
            beer_company["name"] = name
        if description is not None:
            beer_company["description"] = description

        companies[beer_company_id] = beer_company
        return beer_company, 200
    
class DeleteBeerCompany(Resource):
    def delete(self, beer_company_id):
        if beer_company_id in companies:
            del companies[beer_company_id]
            return {}, 200
        return { "message": "No company found" }, 404
    
class ListBeerCompanies(Resource):
    def get(self):
        return [*companies.values()], 200