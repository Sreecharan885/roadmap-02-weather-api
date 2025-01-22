from flask import Flask
from flask_restful import Api, Resource
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from utilities.request_visual_crossing import get_weather_data

app = Flask(__name__)
api = Api(app)

from errors.resource_not_found import *

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)
    
class Get_Weather(Resource):

    #You can adjust these limits as needed
    @limiter.limit('10 per hour')
    def get(self, city_code):
        response_from_service = get_weather_data(city_code)
        return response_from_service[0], response_from_service[1]
    
api.add_resource(Get_Weather,'/weather/<city_code>')

if __name__ == '__main__':
    try:
        app.run()
    except Exception as E:
        print("Unhandled exception raised: ",E)