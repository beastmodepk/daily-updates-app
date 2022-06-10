"""
Content of the digest lives here
"""
import random
import datetime
import requests
from config import Config


def get_random_quote():
    """
    Function to get random quotes
    - requests for quotes from the url
    - picks a random quote
    - returns random quote, if exception send default quote
    """
    try:
        response = requests.get(Config.QUOTE_URL)
        response.raise_for_status()

        random_quote = random.choice(response.json())
    except TypeError:
        random_quote = [{'author': 'Parthey Khanderia',\
            'quote': 'Life is on fire but I am in a pool'}]
    return random_quote


def get_weather_forecast(coords=Config.WEATHER_APP['DEFAULT_COORDS']):
    """
    get_weather_forecast(default coordinates for Nashua)
    - create weather url with coordinates
    - get response
    - create list to store next 9 forcast periods
    - return forcast
    """
    # Create weather_url
    base_url = Config.WEATHER_APP['URL']
    api_key = Config.WEATHER_APP['API_KEY']
    weather_url = f"{base_url}?lat={coords['lat']}&lon={coords['lon']}&appid={api_key}&units=metric"

    # get response
    response = requests.get(weather_url)
    response.raise_for_status()

    data = response.json()

    forecast = {'city': data['city']['name'], # city name
                'country': data['city']['country'], # country name
                'periods': list()} # list for storing forcast_data

    # populate list with next 9 forecast periods
    for period in data['list'][0:9]:
        forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                    'temp': round(period['main']['temp']),
                                    'description': period['weather'][0]['description'].title()})

    return forecast

# def get_twitter_trends():
#     pass

# def get_wikipedia_article():
#     pass

if __name__ == '__main__':
#----------------------------------------------
    # test get_random_quote()
    quote = get_random_quote()
    print("Testing get_random_quote")
    print(f"Quote for the day is:\n{quote['text']}")
    print(f"Auther: {quote['author']}")
    print('*'*20)
    san_fran = {"lat": "37.773972","lon": "-122.431297"}
    url = get_weather_forecast()
    print(url)
#----------------------------------------------
