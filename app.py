from flask import Flask
from flask_restful import Api
from routes import init_routes

app = Flask(__name__)
api = Api(app)

init_routes(api)

if __name__ == "__main__":
    app.run(debug=True)