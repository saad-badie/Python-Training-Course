places= [
	{"place": "Eiffel Tower", "city": "Paris", "Country": "France"},
	{"place": "Taj Mahal", "city": "Agra", "Country": "India"},
	{"place": "Central Park", "city": "New York", "Country": "United States"},
]


# add item
places.append({"place": "Ishtar Gate", "city": "Babylon", "Country": "Iraq"})

for place in places:
	print(place["place"], place["city"], place["Country"], sep=", ")