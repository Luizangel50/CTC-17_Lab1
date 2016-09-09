import math

def distanceBetweenCities(dataNodes, cityA, cityB):
	"""Auxiliar function that return the distance in straight line
	of a city A to a city B"""

	deltaX = dataNodes[cityA].axisX - dataNodes[cityB].axisX
	deltaY = dataNodes[cityA].axisY - dataNodes[cityB].axisY
	distance = math.sqrt(math.pow(deltaX, 2) + math.pow(deltaY, 2))

	return distance