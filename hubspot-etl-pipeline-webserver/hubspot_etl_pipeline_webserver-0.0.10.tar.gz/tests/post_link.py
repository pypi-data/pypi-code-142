import requests
import json

URL = 'http://146.190.49.84/main/'

result = requests.post(URL, json={
    'download_link': 'https://api-na1.hubapi.com/notification-station/general/v1/notifications/cta/db8c2d02-cd9e-312a-b0ed-331832a3d734?notificationPortalId=3461273&deliveryMethod=EMAIL'
})

# print(json.dumps(result.json(), indent=2))
# print(result.json())
print(result.status_code)
print(result.text)
