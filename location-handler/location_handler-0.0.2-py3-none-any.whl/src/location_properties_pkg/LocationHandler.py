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

def main():
    lh = LocationHandler()
    print(str(lh.calculateDistanceInKM(53.353628,-6.250163,53.349274,-6.242827)))
    coords = [
	{
		'product_id': 3,
		'latitude': 38.396578,
		'longitude': 27.071347
	},
	{
		'product_id': 5,
		'latitude': 53.349274,
		'longitude': -6.242827
	},
	{
		'product_id': 1,
		'latitude': 53.345037,
		'longitude': -6.267495
	},
	{
		'product_id': 4,
		'latitude': 53.344171,
		'longitude': -6.263622
	},
	{
		'product_id': 2,
		'latitude': 53.200963,
		'longitude': -6.111006
	},
]
    coords2 = {
        '5': {
            'latitude': 53.35357044,
            'longitude': -6.25010404
            
        }, 
        '1': {
            'latitude': 53.35357044, 
            'longitude': -6.25010404}
        
    }
    sorted_coords = lh.sortListOfCoordinates(53.353628, -6.250163, coords2)
    print(sorted_coords)
if __name__ == '__main__':
    main()