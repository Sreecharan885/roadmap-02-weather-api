import requests, os
import json
from .connect_to_redis import set_to_redis, get_from_redis, conn_to_redis
from werkzeug.exceptions import HTTPException

api_key = os.environ['API_KEY']

def get_weather_data(city_code):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_code}?unitGroup=us&key={api_key}&contentType=json"

    if conn_to_redis()[1] == False:
        return {"error":"Connectivity to Redis is not properly established"},500
    
    # Getting if it already exists
    cached_response = get_from_redis(city_code)

    # print(cached_response is None, cached_response)
    if not cached_response is None:
        return (cached_response, 200)

    try: 
        print("Debug_Log: Not found in Cache")
        response = requests.get(url)
        data = response.json()
    except Exception as H:
        return {"error":f"Invalid API call, {str(response.content)}"}, 400
    
    # try:
        # Setting only after valid data is received
    if set_to_redis(city_code,data) == True:
        return (data,200)
    else:
        return {"error": "Unable to set the value"}, 500
    
    # except Exception as e:
    #     # Using this for now as the site always returns a response but need to add functionality to what happens when time out occurs
    #     print(response.content, e)
    #     return {"error": str(response.content)},400