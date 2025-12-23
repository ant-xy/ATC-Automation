import math

def distance(startLat, endLat, startLong, endLong):
    startLat = float(startLat)
    endLat = float(endLat)
    startLong = float(startLong)
    endLong = float(endLong)

    earthRad = 6371

    dLatitude = math.radians(endLat - startLat)
    dLongitude = math.radians(endLong - startLong)

    startLat = math.radians(startLat)
    endLat = math.radians(endLat)

    a = haversine(dLatitude) + math.cos(startLat) * math.cos(endLat) * haversine(dLongitude)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return earthRad * c


def haversine(other):
    return math.pow(math.sin(other/2), 2)
