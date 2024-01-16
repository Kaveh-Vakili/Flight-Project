import requests
import config
SHEETY_API_URL = "https://api.sheety.co"

class DataManager:
    
    def __init__(self):
        self.sheet_url = SHEETY_API_URL + config.SHEET_URL
        # this is the same for all operations
        self.headers = {
            "Authorization": f"Bearer {config.SHEETY_TOKEN}"
        }
        
    def get_sheet(self):
        response=requests.get(url=self.sheet_url,headers=self.headers)
        # to know what that the response code is 
        response.raise_for_status()
     r