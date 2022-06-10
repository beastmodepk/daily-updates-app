"""
App's config
"""
class Config():
    """  Class storing apps's config   """
    QUOTE_URL = "https://type.fit/api/quotes"
    WEATHER_FORCAST = {
        "API_KEY": "fdfb08d6f28c8ca29b7880890bced87d",
        "URL": "https://api.openweathermap.org/data/2.5/forecast",
        "DEFAULT_COORDS": {"lat": "42.7653662","lon": "-71.467566" } # Nashua, NH
        #SAN_FRAN_COORDS: {"lat": "37.773972" ,"lon": "-122.431297"}
    }
Config = Config()
