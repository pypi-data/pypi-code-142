import math

class LocationHandler:
    # calculation algorithm: https://www.geeksforgeeks.org/program-distance-two-points-earth/#:~:text=For%20this%20divide%20the%20values,is%20the%20radius%20of%20Earth.
    # Calculate the distance in KM between two latitude-longitude pairs
    def calculateDistanceInKM(self, lat1, lon1, lat2, lon2):
        lon1 = math.radians(lon1)
        lon2 = math.radians(lon2)
        lat1 = math.radians(lat1)
        lat2 = math.radians(lat2)
        
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        
        c = 2 * math.asin(math.sqrt(a))
        
        r = 6371
        
        return(round((c * r),3))
        
    # Decide if a coordinate is close enough to a given coordinate
    def isCoordinateFeasible(self, lat1, lon1, lat2, lon2, radius):
        return True if (self.calculateDistanceInKM(lat1, lon1, lat2, lon2) <= radius) else False
