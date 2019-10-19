def printPayload(hotels, pois, lasts):
	print('Here are the places you might visit in {} day(s)'.format(lasts))

	k=1
	for i in pois:
	    print("{}  {}".format(k,i))
	    k+=1

	print()
	print('-----------------------------------------------------------------------')

	print('These are the Hotel(s) as per your budget')
	for hotel in hotels:
	    print(hotel['name'])
	    for i in range(hotel['star']):
	        print('*',end="")
	    print(' Hotel')
	    print('Location:', hotel['location'])
	    print('Per night cost:', hotel['price'])
	    print()
	    print('-----------------------------------------------------------------------')



	print('Here are some hotel suggestions')
	print('* Food expenses are not included in this trip')
	print('** Only breakfasts are included')