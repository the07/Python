import itertools
from math import *

def distance_between(point1, point2):
    """Returns the distance between 2 locations"""

    EARTH_RADIUS = 6371
    lat_point1 = radians(float(places[point1][0]))
    lat_point2 = radians(float(places[point2][0]))
    lon_point1 = radians(float(places[point1][1]))
    lon_point2 = radians(float(places[point2][1]))

    return acos(sin(lat_point1) * sin(lat_point2) + cos(lat_point1) * cos(lat_point2) * cos(lon_point2 - lon_point1)) * EARTH_RADIUS

n = int(input())
interests = []
while n > 0:
    n = n - 1
    _, *interest = map(str, input().split())
    for x in interest:
        interests.append(x)

m = int(input())
global places
places = {}
while m > 0:
    m = m - 1
    location, latitute, longitude, count, *passions = map(str, input().split())
    places[location] = [float(latitute), float(longitude), count, passions]

possible_places = list(itertools.combinations(places.keys(), 2))

group_interest = set(interests)
current = 0
distance = 0

for i in range(0, len(possible_places)):
    location1 = possible_places[i][0]
    location2 = possible_places[i][1]
    a = set(places[location1][3])
    b = set(places[location2][3])
    c = a.intersection(b)
    matches = len(c.intersection(group_interest))
    if matches > current:
        current = matches
        answer = i
        distance = distance_between(location1, location2)
    elif matches == current and matches != 0:
        curr_distance = distance_between(location1, location2)
        if curr_distance < distance:
            answer = i
            distance = curr_distance
        else:
            continue
    else:
        continue


print(*(sorted(possible_places[answer])))
