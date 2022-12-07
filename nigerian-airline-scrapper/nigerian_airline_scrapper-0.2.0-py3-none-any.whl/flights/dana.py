from bs4 import BeautifulSoup
import requests


def dana_air(data):
    if not data:
        return dict()

    trip_info = {}

    locations = {
        "LOS": "Lagos",
        "ABV": "Abuja",
        "ENU": "Enugu",
        "QOW": "Owerri",
        "PHC": "Port Harcourt"
    }

    # if data["depature"] not in locatons[:][0]:
    #     return {}

    # if data["destination"] not in locatons[:][0]:
    #     return {}

    trip_types = ["OW", "RT", "MC"]
    trip_type = trip_types[int(data["type"]) - 1]
    if trip_type != "OW" and "date_arrival" not in data:
        return trip_info

    am = None
    ad = None

    year, month, day = data["date_departure"].split("-")

    am = f"{year}-{month}"
    ad = f"{day}"
    response = requests.get(
        "https://secure.flydanaair.com/bookings/flight_selection.aspx",

        params={
            "TT_RT": trip_type,
            "AM": am,
            "AD": ad,
            "PA": data["adults"],
            "PC": data["infants"],
            "PI": data["children"],
            "DC": data["departure"].upper(),
            "AC": data["destination"].upper()
        }
    )
    bs = BeautifulSoup(response.text, features="lxml")
    count = 1
    for leaving in bs.find_all("td", {"class": "time leaving"}):
        trip_info[count] = {}
        trip_info[count]["Departure Time"] = leaving.text
        arrival = leaving.find_next("td", {"class": "time landing"})
        trip_info[count]["Arrival Time"] = arrival.text

        prices = leaving.parent.find_next("label")
        trip_info[count]["url"] = response.url
        trip_info[count]["destination"] = data["destination"].upper()
        trip_info[count]["dest"] = locations[data["destination"].upper()]
        trip_info[count]["departure"] = data["departure"].upper()
        trip_info[count]["depart"] = locations[data["departure"].upper()]
        trip_info[count]["Prices"] = []

        for _ in range(3):

            try:
                _, price = prices.get_attribute_list(
                    "data-title")[0].split("\n")
                trip_info[count]["Prices"].append(price)
            except:
                pass
            prices = prices.find_next("label")

        count += 1
    return trip_info
