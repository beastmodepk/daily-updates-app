"""
App's config
"""
import os
from dotenv import load_dotenv


class Config:
    """Class storing apps's config"""

    # secrets are stored in .env
    load_dotenv()
    openweathermap_api = os.environ.get("openweathermap_api")

    QUOTE_URL = "https://type.fit/api/quotes"
    WEATHER_FORCAST = {
        "API_KEY": openweathermap_api,
        "URL": "https://api.openweathermap.org/data/2.5/forecast",
        # Nashua, NH
        "DEFAULT_COORDS": {"lat": "42.7653662", "lon": "-71.467566"}
        # SAN_FRAN_COORDS: {"lat": "37.773972" ,"lon": "-122.431297"}
    }
    WIKI_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

    recipients_list = ['digest-recipient1@email.com',
                       'digest-recipient2@email.com']

    sender_credentials = {"email": "fake_email",
                          "credentials": "fake_credentails"}

    sender_credentials = {"email": "fake_email",
                          "credentials": "password"}

    # self.sender_credentials = {'email': 'YOUR SENDER EMAIL ADDRESS GOES HERE',  # your sender email address
    #                               'password': 'YOUR SENDER EMAIL PASSWORD GOES HERE'}  # your sender password


Config = Config()
