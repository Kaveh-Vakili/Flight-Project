import requests
import config
import flight_data as fd



KIWI_API_URL = "http://tequila-api.kiwi.com"
LOCALE = "en-US"
NIGHTS_FROM = 7
NIGHTS_TO = 28
CURRENCY = "USD"
MAX_STOPOVERS = 0



class FlightSearch:    
    def __init__(self):
        self.api_url = KIWI_API_URL
        self.locale = LOCALE
        self.headers = {
            "apikey": config.KIWI_API_KEY
        }
    def find_city_code(self,name):
        URL= f"{self.api_url}/locations/query"
        params={
            "term":name,
            "locale":self.locale,
            "location_types":"city",
            "active_only":True
        }   
        response = requests.get(url=URL, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()["locations"]

    def find_flights(self, origin, destination, date_from, date_to):
        search_url = f"{self.api_url}/v2/search"
        params = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": NIGHTS_FROM,
            "nights_in_dst_to": NIGHTS_TO,
            "flight_type": "round",
            "curr": CURRENCY,
            "one_for_city": 1,
            "max_stopovers": MAX_STOPOVERS
        }