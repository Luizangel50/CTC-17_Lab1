import heapq
from Helper import distanceBetweenCities

def aStarSearch(dataNodes, initialCity, finalCity):
	"""Function that implements A* Search Algorithm.
	Receives the graph, the initial and the final cities and prints
	the list of cities, ordered by the path that was followed, for the best estimative"""

	# List of already evaluated cities
	evaluatedNodes = []

	# Priority queue of algorithm
	priorityQueue = []

	# Map that associates a city to its neighbor by the most efficient path
	# according to this algorithm
	originMap = {}

	# Cost of initialCity to the initialCity
	dataNodes[initialCity].cost = 0

	# Pushing the initialCity to the heap
	distanceFromInitialToFinal = distanceBetweenCities(dataNodes, initialCity, finalCity)
	heapq.heappush(priorityQueue, [distanceFromInitialToFinal, dataNodes[initialCity]])

	# List of cities followed
	totalPath = []

	# While priority queue is not empty
	while len(priorityQueue) != 0:

		# Pop the element of priority queue that has the best estimative
		# for its cost
		currentNode = heapq.heappop(priorityQueue)

		# If currentNode is the destination
		if currentNode[1].index == finalCity:
			totalPath = bestPath(dataNodes, originMap, currentNode[1].index)
			break

		# Add currentNode to the list of already evaluated nodes
		evaluatedNodes.append(currentNode[1].index)

		# For each neighbor of the currentNode
		for neighbor in currentNode[1].listNeighbors:

			# If neighbor was evaluated yet, ignores begin the loop again
			if neighbor in evaluatedNodes:
				continue
			
			# New estimative for the currentNode
			newValue = currentNode[1].cost + distanceBetweenCities(dataNodes, currentNode[1].index, neighbor)
			
			# Variable that indicates if neighbor is already in the priority queue
			newNode = True
			for element in priorityQueue:
				if dataNodes[neighbor].index == element[1].index:
					# Set False if neighbor exists in the priority queue
					newNode = False
					break
				
			# If neighbor is not in priority queue or it is in priority queue,
			# but there is a new better estimative for its cost
			if (newNode == True) or (newNode == False and newValue < dataNodes[neighbor].cost):
				originMap[neighbor] = currentNode[1].index
				dataNodes[neighbor].cost = newValue
				sumValues = newValue + distanceBetweenCities(dataNodes, neighbor, finalCity)
				heapq.heappush(priorityQueue, [sumValues, dataNodes[neighbor]])

	print "\n"
	print "*****************A Star Algorithm*****************"
	print "Total cost of the path: " + str(dataNodes[finalCity].cost)
	print "Path followed:"
	for node in reversed(totalPath):
		print node,


def bestPath(dataNodes, originMap, node):
	"""Function that finds the best path after applying A* algorithm
	according to a map relating the cities"""

	totalPath = []
	totalPath.append(node)
	
	while node in originMap.keys():
		node = originMap[node]
		totalPath.append(node)

	return totalPath