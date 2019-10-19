from operatingAreas import *
from packageFilter import *
from getData import *
from printPayload import *


location, minPay, maxPay, days = getData()

hotels, pois, lasts = getTrip(location, minPay, maxPay, days)

printPayload(hotels, pois, lasts)


