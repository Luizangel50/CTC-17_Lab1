from Helper import distanceBetweenCities

def greedySearch(dataNodes, initialCity, finalCity):
	"""Function that implements Greedy Search Algorithm.
	Receives the graph, the initial and the final cities and prints
	the list of cities, ordered by the path that was followed, for the best estimative"""

	# List of the cities followed
	cities = []
	cities.append(initialCity)

	if(initialCity != finalCity):
		searchPath(dataNodes, initialCity, finalCity, cities)


	print "*****************Greedy Algorithm (basic)*****************"
	print "Total cost of the path: " + str(costPath(dataNodes, cities, finalCity))
	print "Path followed:"
	for city in cities:
		print city,


def searchPath(dataNodes, currentCity, finalCity, listCities):
	"""Auxiliar function for the search of path with best estimative
	according to Greedy Search Algorithm"""

	# If it's not the final city
	if(currentCity != finalCity):

		# Get the map of neighbors of currentCity with theirs distances 
		# in straight line to the finalCity
		mapDistances = orderNeighbors(dataNodes, currentCity, finalCity)

		# Order the values (distances) of the map
		sortedDistances = sorted(mapDistances.values())

		# Variable that indicates if a city will be added to the
		# final list of cities followed
		cityAdded = False

		# For each distance in the list
		for distance in sortedDistances:
			chosenCity = mapDistances.keys()[mapDistances.values().index(distance)]

			# If this city is not in the list
			if chosenCity not in listCities:

				# Add the city to the list
				listCities.append(chosenCity)
				cityAdded = True
				break
		
		# If a neighbor city of currentCity was added
		if cityAdded is True:

			# Continue to follow the path after the chosenCity
			searchPath(dataNodes, chosenCity, finalCity, listCities)

		# If no neighbor city of currentCity was added
		else:
			# currentCity is the previous city
			currentCity = listCities[-2]		

			# remove the last city from the list and mark it
			dataNodes[listCities[-1]].marked = True
			del listCities[-1]

			# Continue to follow the path after the new currentCity
			searchPath(dataNodes, currentCity, finalCity, listCities)


def orderNeighbors(dataNodes, cityA, cityB):
	"""Auxiliar function that returns a map with neighbors (not yet marked)
	of a city A with the distance of them to the city B"""

	mapDistances = {}

	for neighborCity in dataNodes[cityA].listNeighbors:

		if dataNodes[neighborCity].marked == False:
			
			distance = distanceBetweenCities(dataNodes, neighborCity, cityB)
			mapDistances[neighborCity] = distance

	return mapDistances


def costPath(dataNodes, listCities, finalCity):
	"""Auxiliar function that return the cost of a path from
	the beginning of a list to its end"""

	cost = 0

	if finalCity in listCities:
		for city in listCities:
			indexCity = listCities.index(city)

			if indexCity != len(listCities) - 1:
				cost += distanceBetweenCities(dataNodes, city, listCities[indexCity + 1])
	else:
		cost = -1

	return cost