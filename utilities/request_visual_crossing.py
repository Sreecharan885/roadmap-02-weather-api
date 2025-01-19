import requests, os
import json
from .connect_to_redis import set_to_redis, get_from_redis

api_key = os.environ['API_KEY']

def get_weather_data(city_code):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_code}?unitGroup=us&key={api_key}&contentType=json"

    try:
        # Getting if it already exists
        cached_response = get_from_redis(city_code)

        # print(cached_response is None, cached_response)
        if not cached_response is None:
            return (cached_response, 200)
        
    except Exception as E:
        print("Request not in cache")

    try: 
        print("Debug_Log: Not found in Cache")
        response = requests.get(url)

        data = response.json()
        # Setting only after valid data is received
        try:
            set_to_redis(city_code,data)
        except Exception as e:
            return {"error": str("Internal Server Error - Redis connectivity issue at Server")}, 500 
        return (data,200)
    
    except Exception as e:
        # Using this for now as the site always returns a response but need to add functionality to what happens when time out occurs
        print(response.content, e)
        return {"error": str(response.content)},400