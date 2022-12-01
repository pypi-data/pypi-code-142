import requests
import json
from requests.exceptions import ConnectionError 
import datetime
from datetime import date, timedelta
import pytz
from pytz import timezone
from requests_handler import responseHandler


# Ask for user input
userInput = raw_input("Select URL to use (enter 1, 2, or 3):\n1. Origin\n2. Development\n3. Production\n\n")

# Define url options, 0 acts a placeholder so array can start at 1
url = [0, "https://api-v1-cp.weather.gov/", "http://nids-int-wapiweb-dev.bldr.ncep.noaa.gov/", "https://api.weather.gov/"]

if userInput == "1":
    print("You selected option 1: " + url[1])
elif userInput == "2":
    print("You selected option 2: " + url[2])
elif userInput == "3":
    print("You selected option 3: " + url[3])
else:
    print(userInput)
    print("Invalid option. Exiting...")
    quit ()

url = url[int(userInput)]

# -------------------------------------------------------------------------------
# -------------------------- Verify Pagination ----------------------------------
# -------------------------------------------------------------------------------
print("_________________________________________________________\n")
print(" VERIFYING PAGINATION")
print("_________________________________________________________")

# Define limit for the /alerts?limit parameter endpoint, max 500
limit = "500"

# Request the endpoint using the limit defined above 
print("Requesting: " + url + "alerts?limit=" + limit)
print("Limit is " + limit + ".")
response, data = responseHandler(url + "alerts?limit=" + limit)

# Define 1st pagination object to check for KeyError
try:
    pag_object1 = (data['pagination']['next'])
except KeyError:
    print("KeyError. Pagination object not found. Exiting...\n")
    quit()

# Convert the data to a string and count the number of alerts using a phrase found in each alert
data_str = str(data)
count_limit = data_str.count("areaDesc")

# Verify that the number of alerts match the defined limit
if str(count_limit) == limit:
    print(limit + " alerts found.\n")
else:
    print("Number of alerts found not equal to limit.\n")
    print(limit + " alerts found.\n")

# Loop through all pagination links as long as the text string is found in the data
# Use data defined outside the loop to define variables
# Make a new request to the API using the next pagination link
while "pagination" in data:
    pag_object1 = (data['pagination']['next']) 
    print "Requesting next pagination link..." + str(pag_object1)
    description = data['features'][0]['properties']['description'] 
    description_last = data['features'][-1]['properties']['description']
    response, data = responseHandler(pag_object1) 
    # Continue loop if pagination is found in next link
    # Define description from current pagination page
    if "pagination" in data:
        description2 = data['features'][0]['properties']['description']
        description_last2 = data['features'][-1]['properties']['description']
        # Verify that the first and last alerts from the current page don't match those from the first
        if description != description_last and description != description2:
            print("First and last alert are different.")
        else:
            print("Alerts are the same.")
    else:
        print("Pagination link not found. End of pagination.\n")


