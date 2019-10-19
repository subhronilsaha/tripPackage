
from operatingAreas import *



def getData():
    k=1
    print('Where do you want to go for a trip?')
    print('Choose from the Menu below')
    for loc in Locs:
        print('{}. {}'.format(k,loc))
        k+=1
    print('Your response:',end="")
    location = int(input()) -1
    if location < 0 and location > 5:
        print('You did not select an option from the Menu')
        exit()


    print('Enter Maximum amount you would spend on your trip :',end="")
    maxPay = int(input())

    print('Enter Minimum amount you would spend on your trip :',end="")
    minPay = int(input())

    if maxPay < minPay:
        print('The minimum expense entered is more than the maximum desired expense')
        exit()

    print('How many days do you prefer your trip to last?',end="")
    days = int(input())



    return location, minPay, maxPay, days
