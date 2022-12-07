from nigerian_airline_scrapper.custom.thread import CustomThread
from nigerian_airline_scrapper.flights.dana import dana_air


class LocalAirline:

    def __init__(self, data):
        self.data = data

    def get_flights(self):
        dana = CustomThread(target=dana_air, kwargs=self.data)
        dana.start()

        result = {
            "Dana Air": dana.join()
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
