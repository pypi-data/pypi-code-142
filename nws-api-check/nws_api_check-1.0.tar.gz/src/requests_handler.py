import requests
import json
from requests.exceptions import ConnectionError 
import urllib.request

# ---------------------------------------------------------------------
# This module is used in api.py to handle the error exceptions from 
# the request.get module.
# ---------------------------------------------------------------------

# Resolves UnboundedLocalError
response = 0
data = 0

# define module
def responseHandler(url):
    global response, data, contentType
    try:
        # If using API-v1, verification is needed to bypass InsecureRequestWarning
        if "api-v1-cp" in url:
             # Make a request to the API
             response = requests.get(url, timeout=5, verify=False) 
             # Content Type
             contentType = response.headers['content-type']
             # Define status code
             status = response.status_code
             # Convert data dictionary to JSON
             data = response.json()
        # If using prod or dev
        else:
             response = requests.get(url, timeout=30)
             status = response.status_code
             data = response.json()
             contentType = response.headers['content-type']
             #if "geo+json" not in str(contentType): #come back to this, need conditional if content type isn't json
             #print("Content type is: " + contentType)
    # Exclude the following errors
    except requests.exceptions.Timeout: # 5 seconds
        print("Timeout ERROR.")
    except requests.exceptions.ConnectionError:
       print("Connection ERROR.")
    except ValueError:
        if response.status_code == 500:
            print("Status: " + str(status) + " ERROR.")
        elif response.status_code != 200:
            print("ValueError: Not JSON. Content Type is: " + contentType)
        else:
#            print("ValueError: No JSON object could be decoded.")
            with urllib.request.urlopen(url) as response:
                info = response.info()
                info_type = info.get_content_subtype()
                print("Is not JSON. Content type is: " + info_type)
#                print(info.get_content_type())      # -> application/type
    except IndexError:
        print("Index ERROR: list index out of range")
        print("Alerts likely missing. Check the URL for alerts.")
#        quit()
    else:
        if response.status_code == 200:
            pass
            #print "Status: 200 OK"
        if response.status_code == 400: 
            #print "Content Type is: " + contentType
            print("Status: " + str(status) + " error. Bad request.")
            print("Correlation ID: " + str(data['correlationId']))
        elif response.status_code == 404:
            print("Status: 404 Page not found")
        elif response.status_code == 503:
            print("Status: 503 Service unavailable")
        elif response.status_code != 200 and response.status_code != 400 and response.status_code != 404 and response.status_code != 503:
        #else:
            print("Status: " + str(status) + " ERROR.")
    # Return values to be used in the main script
    return response, data

