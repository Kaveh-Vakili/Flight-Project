#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import datetime as dt
import data_manager as dm
import flight_search as fs
import notification_manager as nm


ORIGIN_CODE = "IAD"

# initialization
data_manager = dm.DataManager()
flight_search = fs.FlightSearch()
notification_manager = nm.NotificationManager()

sheet=data_manager.get_sheet()


#checking for missing airport codes
for city in sheet:
    if city["iataCode"]=="":
        

