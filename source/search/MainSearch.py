import Node
import Greedy
import AStar

# Nodes where the search begins and finishes
INITIAL_NODE = 202
FINAL_NODE = 601

def main():
	"""Main function"""

	# Dictionary that stores all the nodes of the graph
	# in which the keys are the nodes' IDs
	dataNodes = {}

	# Readin data
	readInput(dataNodes)
	
	# Using Greedy algorithm
	Greedy.greedySearch(dataNodes, INITIAL_NODE, FINAL_NODE)

	# Using A* algorithm
	AStar.aStarSearch(dataNodes, INITIAL_NODE, FINAL_NODE)


def readInput(dataNodes):
	"""Read each line of file Uruguay.csv and add
	data to dictionary"""

	# Iterates for each line of input file and get data
	for line in open("../../inputs/Uruguay.csv", "r"):
		line = line.replace(";", " ").replace(",", ".")
		lines = line.split()

		# ID of the node
		indexNode = int(lines[0])
		# List of neighbors of the node
		neighbors = [int(x) for x in lines[3:]]		

		# Store information of the node
		currentNode = Node.Node(indexNode, float(lines[1]), float(lines[2]), neighbors)

		# Store node on the 'dataNodes' map
		dataNodes[indexNode] = currentNode



if __name__ == "__main__":
	main()