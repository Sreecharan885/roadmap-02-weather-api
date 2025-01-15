from flask import Flask, make_response, jsonify
from flask_restful import Api, Resource
from utilities.request_visual_crossing import get_weather_data
import json

app = Flask(__name__)
api = Api(app)
    
class Get_Weather(Resource):
    def get(self, city_code):
        print('Debug_log: Just entered get')
        response_from_service = get_weather_data(city_code)
        if response_from_service[1] == 400:
            return "Invalid request", 400
        response = make_response(jsonify(response_from_service[0]),200)
        response.headers['Content-Type'] = 'application/json'
        return response
    
api.add_resource(Get_Weather,'/weather/<city_code>')

if __name__ == '__main__':
    app.run()