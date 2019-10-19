from math import ceil


from operatingAreas import *
from Pois import *
from Hotels import *



def getTrip(loc, min, max, days):
    place = Locs[loc]
    pois = Pois[place]
    maxDay = days*2
    placesYouWillVisit = []
    if maxDay > len(pois):
        maxDay = len(pois)
    for i in range(maxDay):
        placesYouWillVisit.append(pois[i])


    max -= maxDay * 200
    min -= maxDay * 200
    hotel = getHotel(max, min, place, days)
    if len(hotel) == -1:
        print('Your maximum desired expense is lower than any packages we can provide.')
        exit()


    return hotel, placesYouWillVisit, ceil(maxDay/2)


def getHotel(max, min, place, days):
    hotel = Hotels[place]
    stayPriceLimit = max/days
    stayPriceMin = min/days
    stay = []
    for i in hotel:
        if i['price'] < stayPriceLimit and i['price'] > stayPriceMin:
            stay.append(i)
    return stay




