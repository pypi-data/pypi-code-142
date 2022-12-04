from bs4 import BeautifulSoup
import requests


def dana_air(data):
    trip_info = {}

    locatons = [
        ("LOS", "Lagos"),
        ("ABV", "Abuja"),
        ("ENU", "Enugu"),
        ("QOW", "Owerri"),
        ("PHC", "Port Harcourt")
    ]

    # if data["depature"] not in locatons[:][0]:
    #     return {}

    # if data["destination"] not in locatons[:][0]:
    #     return {}

    trip_types = ["OW", "RT", "MC"]
    trip_type = trip_types[int(data["type"]) - 1]
    if trip_type != "OW":
        data["date_arrival"]

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
            "DC": data["departure"],
            "AC": data["destination"]
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
        trip_info[count]["Prices"] = []

        for _ in range(3):

            _, price = prices.get_attribute_list(
                "data-title")[0].split("\n")
            trip_info[count]["Prices"].append(price)
            prices = prices.find_next("label")

        count += 1
    return trip_info
