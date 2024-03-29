"""
Content of the digest lives here
"""

# TODO: List of things to add to the NEWSLETTER
# - funny gifs
# - book suggestions, ask for genre
#   - quotes from book suggestions, ask for book/genre
# - sports teams to watch for
#   - for sports teams
#   - for what kind of stats
# - news
# - link of daily games to play
#   - wordle

# OTHER THINGS
# - connect with other to see what they are watching
# - comment on peoples page about their things

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
        random_quote = [
            {
                "author": "Parthey Khanderia",
                "quote": "Life is on fire but I am in a pool",
            }
        ]
    return random_quote


def get_weather_forecast(coords=Config.WEATHER_FORCAST["DEFAULT_COORDS"]):
    """
    get_weather_forecast(default coordinates for Nashua)
    - create weather url with coordinates
    - get response
    - create list to store next 9 forcast periods
    - return forcast
    """
    # Create weather_url
    base_url = Config.WEATHER_FORCAST["URL"]
    api_key = Config.WEATHER_FORCAST["API_KEY"]
    weather_url = f"{base_url}?lat={coords['lat']}&lon={coords['lon']}&appid={api_key}&units=metric"

    # get response
    try:
        response = requests.get(weather_url)
        response.raise_for_status()

        data = response.json()

        forecast = {
            "city": data["city"]["name"],  # city name
            "country": data["city"]["country"],  # country name
            "periods": list(),
        }  # list for storing forcast_data

        # populate list with next 9 forecast periods
        for period in data["list"][0:9]:
            forecast["periods"].append(
                {
                    "timestamp": datetime.datetime.fromtimestamp(period["dt"]),
                    "temp": round(period["main"]["temp"]),
                    "description": period["weather"][0]["description"].title(),
                    "icon": f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png',
                }
            )

        return forecast
    except AttributeError as error:
        print(error)


def get_wikipedia_article():
    """
    Get a random wiki article
    """
    try:  # retrieve random Wikipedia article
        response = requests.get(Config.WIKI_URL)
        response.raise_for_status()

        data = response.json()
        wikipedia_article = {
            "title": data["title"],
            "extract": data["extract"],
            "url": data["content_urls"]["desktop"]["page"],
        }

        return wikipedia_article
    except AttributeError as error:
        print(f"error reaching URL: {error}")


if __name__ == "__main__":
    # ----------------------------------------------
    # test get_random_quote()
    STARS = "*" * 20
    quote = get_random_quote()
    print("Testing get_random_quote")
    print(f"Quote for the day is:\n{quote.get('text')}")
    print(f"Auther: {quote.get('author')}")
    print(STARS)
    # ----------------------------------------------
    # test get_weather_forecast()
    print("Testing get_weather_forecast")
    san_fran = {"lat": "37.773972", "lon": "-122.431297"}
    forcast = get_weather_forecast()
    print(forcast)
    print(STARS)
    # ----------------------------------------------
    # test get_wikipedia_article()
    print("Testing get_wikipedia_article")
    wiki_article = get_wikipedia_article()
    print(wiki_article)
    print(STARS)
# ----------------------------------------------
