# tripPackage
college project

#__main__.py
-runtime Index
+functioanlities served
>calls getData() // input function
>calls getTrip() // computing call
>calls printPayload() // to print the result

#getData.py ~ getData()
-input stream handler
+functionalities served
>gets the user budget max, min
> place to visit and day limit of tour
> returns the recieved payload to main

#packageFilter.py ~ getTrip()
-data computing call
+functionalities served
> gets data from hardcoded db in Hotels.py and Pois.py
> calls getHotel() // to get appropriate hotel for budget constrains
> return payload to main

#printPayload.py ~ printPayload()
-prints result
+functionalities served
> print result with basic formating
