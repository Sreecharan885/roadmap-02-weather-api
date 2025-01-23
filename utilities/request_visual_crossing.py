import requests, os
from .connect_to_redis import set_to_redis, get_from_redis, conn_to_redis

api_key = os.environ['API_KEY']

def get_weather_data(city_code):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_code}?unitGroup=us&key={api_key}&contentType=json"

    if conn_to_redis()[1] == False:
        return {"error":"Connectivity to Redis is not properly established"},500
    
    # Getting if it already exists
    cached_response = get_from_redis(city_code)

    if not cached_response is None:
        return (cached_response, 200)

    try: 
        print("Debug_Log: Not found in Cache")
        response = requests.get(url)
        data = response.json()
    except requests.exceptions.ConnectionError or requests.exceptions.Timeout:
        # When the site is down
        return {"error":"Invalid API call, Unable to connect to Web API/ It returned no response"}, 502
    except Exception as H:
        print(str(response.content))
        return {"error":f"Invalid API call, check Error logs for more details"}, 400
    
    if set_to_redis(city_code,data) == True:
        return (data,200)
    else:
        return {"error": "Unable to set the value"}, 500