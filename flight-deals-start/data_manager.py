import requests

import config

SHEETY_API_URL = "https://api.sheety.co"


class DataManager:

    def __init__(self, worksheet_name):
        self.worksheet_name = worksheet_name
        self.worksheet_url = SHEETY_API_URL + config.SHEET_URL + self.worksheet_name
        self.headers = {
            "Authorization": f"Bearer {config.SHEETY_TOKEN}"
        }

    def get_sheet(self):
        response = requests.get(url=self.worksheet_url, headers=self.headers)
        response.raise_for_status()
        print(f"Worksheet \"{self.worksheet_name}\" successfully loaded.")
        return response.json()[self.worksheet_name]

    def update_code(self, entry):
        """Takes a row number as STR and updates the corresponding row in the spreadsheet."""
        edit_url = f"{self.worksheet_url}/{entry['id']}"
        body = {
            "price": {
                "iataCode": entry["iataCode"]
            }
        }
        response = requests.put(url=edit_url, json=body, headers=self.headers)
        response.raise_for_status()
        print(f"Row {entry['id']} has been updated with code {entry['iataCode']}.")

    def add_user(self, first_name, last_name, email):
        """Takes the user's details as STRs and add them to the worksheet."""
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=self.worksheet_url, json=body, headers=self.headers)
      
        response.raise_for_status()
        print(f"User {first_name} {last_name} has been added to the \"{self.worksheet_name}\" worksheet.")