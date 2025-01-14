import requests, os
import json

def get_weather_data(city_code):
    api_key = os.environ['API_KEY']
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_code}?unitGroup=us&key={api_key}&contentType=json"
    try:
        response = requests.get(url)
        data = response.json()
        return (data,200)
    except Exception:
        # Using this for now as the site always returns a response but need to add functionality to what happens when time out occurs
        return (json.dumps({"error": str(response.content)}),400)