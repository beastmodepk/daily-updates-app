"""
Content of the digest lives here
"""
import random
import requests
import config
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

# def get_weather_forecast():
#     pass

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
#----------------------------------------------
    pass