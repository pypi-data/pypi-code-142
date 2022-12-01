import requests
import json
from requests.exceptions import ConnectionError 
import datetime
from datetime import date, timedelta
import pytz
from pytz import timezone
from requests_handler import responseHandler

# -----Test ------------------------------------------------------------------------------
#url_hardcoded = "https://preview-api.weather.gov/stations/KIAD/tafs/2022-11-17/1121"
#url_tafs = "https://preview-api.weather.gov/stations/KIAD/tafs"
#print("Requesting: " + url_hardcoded)
##response, data = responseHandler(url_hardcoded)
##x = requests.get(url_hardcoded)
#response, data = responseHandler(url_hardcoded)
##print(x.status_code)

# -------------------------------------------------------------------------------
# -------------------------------- API CALL -------------------------------------
# ----------------------- Endpoint: /alerts/active endpoint ---------------------
# -------------------------------------------------------------------------------

# Ask for user input     #n1. Origin
userInput = input("Select URL to use (enter 1, 2, or 3):\n1. Development\n2. QA/Preview \n3. Production\n\n")

# Define url options, 0 acts a placeholder so array can start at 1     #https://api-v1-cp.weather.gov/
url = [0, "http://nids-int-wapiweb-dev.bldr.ncep.noaa.gov/", "http://preview-api.weather.gov/", "https://api.weather.gov/"]

if int(userInput) <= 4:
    print("You selected option " + userInput + ": " + url[int(userInput)])
else:
    print(userInput)
    print("Invalid option. Exiting...")
    quit ()

url = url[int(userInput)]

print("_________________________________________________________\n")
print(" Requesting /alerts/active/ endpoints")
print("_________________________________________________________")

print("\nRequesting: " + url + "alerts/active")
response, data = responseHandler(url+"alerts/active")

# DEFINE VARIABLES if active alerts are found
try:
    ugcString = str(data['features'][0]['properties']['geocode']['UGC'][0]) # access first item in geocode array [0]
    sameString = str(data['features'][0]['properties']['geocode']['SAME'][0])
    sameNumber = sameString[1:3]
    zoneId = sameString[3:6]
    nwsId = data['features'][0]['properties']['id']
    description_init = data['features'][0]['properties']['description']

    # Dictionary to hold State Codes and Marine Codes defined by the U.S. Census Bureau, https://www.census.gov/library/reference/code-lists/ansi/ansi-codes-for-states.html 
    area_codes = {'01': 'AL', '02': 'AK', '04': 'AZ', '05': 'AR', '06': 'CA', '08': 'CO', '09': 'CT', '10': 'DE', '11': 'DC', '12': 'FL', 
              '13': 'GA', '15': 'HI', '16': 'ID', '17': 'IL', '18': 'IN', '19': 'IA', '20': 'KS', '21': 'KY', '22': 'LA', '23': 'ME', 
              '24': 'MD', '25': 'MA', '26': 'MI', '27': 'MN', '28': 'MS', '29': 'MO', '30': 'MT', '31': 'NE', '32': 'NV', '33': 'NH', 
              '34': 'NJ', '35': 'NM', '36': 'NY', '37': 'NC', '38': 'ND', '39': 'OH', '40': 'OK', '41': 'OR', '42': 'PA', '44': 'RI', 
              '45': 'SC', '46': 'SD', '47': 'TN', '48': 'TX', '49': 'UT', '50': 'VT', '51': 'VA', '53': 'WA', '54': 'WV', '55': 'WI', 
              '56': 'WY', 
    # Coastal Waters and Outlying Areas of the US (like Guam and other islands)
              '57': 'PZ', '58': 'PK', '59': 'PH', '60': 'AS', '61': 'PS', '64': 'FM', '65': 'PM', '66': 'GU', '68': 'MH', 
              '69': 'MP', '70': 'PW', '72': 'PR', '73': 'AN', '74': 'UM', '75': 'AM', '77': 'GM', '78': 'VI', '91': 'LS', '92': 'LM', 
              '93': 'LH', '94': 'LC', '96': 'LE', '97': 'LO', '98': 'SL'}

    # Use SAME code to get corresponding state/marine zone 
    area = area_codes.get(sameNumber)

    # -------------------------------- API CALL -------------------------------------
    # ------------------ Endpoint: /alerts/active/zone/{zoneId} ---------------------
    # -------------------------------------------------------------------------------

    # If SAME is less than 57, use UGC (for the U.S.)
    if sameNumber < "57":
    #    print "UGC Code is: " + ugcString
        print("Requesting: " + url + "alerts/active/zone/" + ugcString)
        # Define zone here to use later
        zone = ugcString
        try: 
            response, data = responseHandler(url + "alerts/active/zone/" + ugcString)
            description2 = data['features'][0]['properties']['description']
        except KeyError:
            print("!!!!! ERROR !!!!!")
            print("KeyError. Result of bad request.\n")
    # If SAME is greater than 57, use SAME code (for marine zones) 
    else:
        #print "SAME Code is: " + sameString 
        print("Requesting: " + url + "alerts/active/zone/" + area + "Z" + zoneId)
        zone = area + "Z" + zoneId
        try: 
            response, data = responseHandler(url + "alerts/active/zone/" + area + "Z" + zoneId)
            description2 = data['features'][0]['properties']['description']
        except KeyError:
            print("!!!!! ERROR !!!!!")
            print("KeyError. Result of bad request.\n")
    
    # ------------------------- Endpoint: /alerts?zone= -----------------------------
    print("Requesting: " + url + "alerts?zone=" + zone)
    response, data = responseHandler(url + "alerts?zone=" + zone)

    # ---------------------------------- API CALL -----------------------------------
    # ------------------------- Endpoint: /alerts/{Id} ------------------------------
    # -------------------------------------------------------------------------------
    print("Requesting: " + url + "alerts/" + nwsId)
    response, data = responseHandler(url + "alerts/" + nwsId)
    description3 = data['properties']['description']
    
    # ------------------------------ API CALLS --------------------------------------
    # ------- Endpoints: /alerts/active/count, /alerts/active/area/{area}, ----------
    # ---------------------- /alerts/active/region/{region} -------------------------
    # -------------------------------------------------------------------------------
    
    endpoints = ["area/" + str(area), "count"]
    for e in endpoints:
        print("Requesting: " + url + "alerts/active/" + e)
        responseHandler(url + "alerts/active/" + e)

# Continuation of try block, accepting exceptions
except TypeError:
    print("IndexError. No active alerts found.\nSkipping /alerts/active endpoint.\n")
except KeyError:
    print("KeyError.\n")
except IndexError:
    print("IndexError. No active alerts found.\nSkipping /alerts/active endpoint.\n")

# Marine regions (can still be tested for response status if no active alerts)
regions = ["AL", "AT", "GL", "GM", "PA", "PI"]
for r in regions:
    print("Requesting: " + url + "alerts/active/region/" + r)
    responseHandler(url + "alerts/active/region/" + r)

# ----------------------------- API CALLS ---------------------------------------
# ---------------- Endpoint: /alerts?{parameters} -------------------------------
# -------------------------------------------------------------------------------
print("\n_________________________________________________________\n")
print(" Requesting /alerts?{parameters} endpoints.")
print("___________________________________________________________\n")

# Define dates to use for start and end times
today = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime('%Y-%m-%d')
yesterday = datetime.datetime.now(pytz.timezone('US/Eastern')) - timedelta(1)
yesterday_formatted = yesterday.strftime('%Y-%m-%d')
start_time =  yesterday.replace(microsecond=0).isoformat()
end_time = datetime.datetime.now(pytz.timezone('US/Eastern')).replace(microsecond=0).isoformat()

parameters = ["active=1", "active=0", "start="+start_time, "end="+end_time, "region_type=land", "region_type=marine", "point=38.84,-77.03", 
              "message_type=alert", "message_type=update", "message_type=cancel", "status=actual", "status=exercise", "status=system",
              "status=test", "status=draft", "area=VA", "severity=Unknown", "severity=Minor", "severity=Moderate", "severity=Severe", 
              "severity=Extreme", "certainty=Unknown", "certainty=Unlikely", "certainty=Possible", "certainty=Likely", 
              "certainty=Observed", "limit=5", "urgency=Unknown", "urgency=Past", "urgency=Future", "urgency=Expected", 
              "urgency=Immediate", "region=GL", "region=GM", "region=PA", "region=PI", "region=AT", "code=FLW",
              "event=Flood%20Warning"]
              
# Loop through each endpoint
for p in parameters:
    print("Requesting: " + url + "alerts?" + p)
    response, data = responseHandler(url + "alerts?" + p)

# --------------------------- Other Endpoints -----------------------------------
#   ------- /glossary, /gridpoints, /icons, /offices, /points, -------
#     ----- /products, /radar, /stations, /thumbnails, /zones -----

# define TAF ID for /stations endpoints
response, data = responseHandler(url+"stations/KIAD/tafs")

try:
    taf_id = str(data['@graph'][0]['id']) # access first element in graph array [0]
    taf_last_chars = taf_id[-15:] # access last 15 characters of taf_id URL
except TypeError:
    print("IndexError. No active TAFs found.\n")
except KeyError:
    print("KeyError.\n")
except IndexError:
    print("IndexError. No active TAFs found.\n")

otherEndpts = [
# /aviation
"aviation/cwsus/ZMA/cwas", "aviation/sigmets", "aviation/sigmets/MKCE", "aviation/sigmets/MKCE/"+today, #"aviation/sigmets/MKCE/"+today+"/0055", 
# /glossary
"glossary", 
# /gridpoints
"gridpoints/EAX/40,48","gridpoints/EAX/40,48/forecast?units=us","gridpoints/EAX/40,48/forecast/hourly?units=us","gridpoints/EAX/40,48/stations", 
# /health
"health", 
# /icons
"icons", 
# /offices 
"offices/EAX", "offices/EAX/headlines", "points/38.85,-77.03", # "offices/EAX/headlines/e43fd1ed97980cccfb1174d5f8d0f4c3",
# /points
"points/38.85,-77.03/stations",
# /products
"products","products?location=PHI","products?start="+start_time,"products?end="+end_time, "products?office=KLWX","products?type=NOW","products?limit=5",
"products?wmoid=SRUS51","products/locations","products/types","products/types/FLS","products/types/FLS/locations", #"products/58d21882-473e-41e6-b89f-adcef93135dd",
"products/locations/PHI/types","products/types/AFD/locations/PHI",
# /radar
"radar/servers","radar/servers/ldm1","radar/queues/tds","radar/stations",
"radar/stations/KLWX","radar/stations/KLWX/alarms","radar/profilers/ROCO2",
# /stations
"stations?id=LWX&state=VA&limit=5", "stations/KIAD","stations/KIAD/observations", "stations/KIAD/observations/latest", "stations/KIAD/tafs",# "stations/KIAD/tafs/"+taf_last_chars,
#/stations/{stationId}/observations/{time} #has to be a time from an observation under /stations/{stationId}/observations
# /thumbnails
"thumbnails/satellite/w",
# /zones
"zones","zones?id=ANZ530","zones?area=NY","zones?region=AR","zones?region=CR","zones?region=ER","zones?region=PR","zones?region=SR","zones?region=AL",
"zones?region=AT","zones?region=GL","zones?region=GM","zones?region=PA","zones?region=PI","zones?type=land","zones?type=marine","zones?type=forecast",
"zones?type=public","zones?type=coastal","zones?type=offshore","zones?type=fire","zones?type=county","zones?type=land","zones?point=38.85,-77.03", 
"zones?effective="+end_time,"zones/coastal","zones/coastal?id=AMZ152","zones/coastal?region=AT","zones/land?include_geometry=true",
"zones/forecast/DCZ001","zones/forecast/DCZ001/forecast","zones/forecast/DCZ001/observations","zones/forecast/DCZ001/stations"]

for x in otherEndpts:
    print("Requesting: " + url + x)
    responseHandler(url + x)

print("_________________________________________________________\n")
print("END OF SCRIPT ")
print("_________________________________________________________\n")

# END OF SCRIPT

