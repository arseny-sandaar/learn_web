from flask import current_app
import requests

def weather_by_city(city_name):
    weather_url = current_app.config["WEATHER_URL"]
    params = {
        "key": current_app.config["WEATHER_API_KEY"],
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params)# it will return string (result)
        result.raise_for_status()#it generates exception if the server responds with a specific code that start from 4xx or 5xx
        # we need to convert it to the format we need
        weather = result.json()# we have converted to a pyhton dictionary
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError,TypeError):
                    return False      
    except(requests.RequestException, ValueError):
        print('Network error')
        return False
    return False

if __name__ == "__main__":
    W = weather_by_city("Moscow,Russia")
    print(W)
