from flask import Flask, make_response
from flask_restful import Api, Resource
from utilities.request_visual_crossing import get_weather_data
import json

app = Flask(__name__)
api = Api(app)
    
class Get_Weather(Resource):
    def get(self, city_code):
        response_from_service = get_weather_data(city_code)
        if response_from_service[1] == 400:
            return "Invalid request", 400
        response = make_response(json.dumps(response_from_service[0]))
        response.headers['Content-Type'] = 'application/json'
        return response, 200
    
api.add_resource(Get_Weather,'/weather/<city_code>')