from nigerian_airline_scrapper.thread import CustomThread


class LocalAirline:

    def __init__(self, data):
        self.data = data

    def get_flights(self):
        dana_air = CustomThread(target=self.dana_air)
        dana_air.start()

        result = {
            "Dana Air": dana_air.join()
        }

        return result

    def airpiece(**data):
        trip_info = {}
        [("ABV", "Abuja"),
         ("ACC", "Accra"),
         ("AKR", "Akure"),
         ("ANA", "Anambra"),
         ("ABB", "Asaba"),
         ("BJL", "Banjul"),
         ("BNI", "Benin"),
         ("CBQ", "Calabar"),
         ("DSS", "Dakar"),
         ("DLA", "Douala"),
         ("ENU", "Enugu"),
         ("FNA", "Freetown"),
         ("GMO", "Gombe"),
         ("IBA", "Ibadan"),
         ("ILR", "Ilorin"),
         ("JNB", "Johannesburg"),
         ("KAN", "Kano"),
         ("LOS", "Lagos"),
         ("MDI", "Makurdi"),
         ("ROB", "Monrovia"),
         ("QOW", "Owerri"),
         ("PHC", "Port Harcourt"),
         ("QUO", "Uyo"),
         ("QRW", "Warri"),
         ("YOL", "Yola"),
         ]


data = {
    "type": 1,
    "depature": "LOS",
    "destination": "ABV",
    "infants": 0,
    "children": 0,
    "adults": 1,
    "date_depature": "2022-12-3"
}
localairline = LocalAirline(data)

print(localairline.get_flights())
