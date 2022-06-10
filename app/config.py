"""
App's config
"""
import os
from dotenv import load_dotenv

class Config():
    """  Class storing apps's config   """

    # secrets are stored in .env
    load_dotenv()
    openweathermap_api = os.environ.get("openweathermap_api")

    QUOTE_URL = "https://type.fit/api/quotes"
    WEATHER_FORCAST = {
        "API_KEY": openweathermap_api,
        "URL": "https://api.openweathermap.org/data/2.5/forecast",
        "DEFAULT_COORDS": {"lat": "42.7653662","lon": "-71.467566" } # Nashua, NH
        #SAN_FRAN_COORDS: {"lat": "37.773972" ,"lon": "-122.431297"}
    }
    WIKI_URL =  "https://en.wikipedia.org/api/rest_v1/page/random/summary"

Config = Config()
