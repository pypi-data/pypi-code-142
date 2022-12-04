def result(loc_1: tuple, loc_2: tuple):

    import openrouteservice
    from polyline import decode
    
    
    client = openrouteservice.Client('5b3ce3597851110001cf6248773a45002391497692c5c864b13673d7')
    
    coords = (loc_1, loc_2)
    
    res = client.directions(coords)
    geometry = client.directions(coords)['routes'][0]['geometry']
    
    path = decode(geometry)
    
    return path


def duration(loc_1: tuple, loc_2: tuple):

    import openrouteservice
    from polyline import decode


    client = openrouteservice.Client('5b3ce3597851110001cf6248773a45002391497692c5c864b13673d7')

    coords = (loc_1, loc_2)

    res = client.directions(coords)
    geometry = client.directions(coords)['routes'][0]['summary']['duration']
    
    return geometry