# Take note of the list of dicts that this code generates.There are three dicts in the list "places," one for each place. 
places= [
	{"place": "Eiffel Tower", "city": "Paris", "Country": "France"},
	{"place": "Taj Mahal", "city": "Agra", "Country": "India"},
	{"place": "Central Park", "city": "New York", "Country": "United States"},
]

for place in places:
	print(place["place"], place["city"], place["Country"], sep=", ")