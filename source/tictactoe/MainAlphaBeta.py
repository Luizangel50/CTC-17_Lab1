import Tree
from Helper import winner, checkEnd, printBoard
import time

def main():
	"""Main function"""

	# Flag that verifies if main loop is over
	end = False

	print "*****************Welcome to Alpha-Beta Tic Tac Toe*****************"

	# State of the board
	state = [None] * 9

	# A data estructure Tree
	treePossibilities = None

	# Timer
	pcTime = 0

	# While the game is not over
	while end is False:

		print "Human player's turn (type the x, space and the y, followed by enter): "
		humanInput = raw_input("---> ")

		# Pick up the human input
		humanInputX = int(humanInput.split()[0])
		humanInputY = int(humanInput.split()[1])

		try:
			index = humanInputX*3 + humanInputY

			# Error if invalid index
			if state[index] is not None:
				print "Invalid play. Try again, please."

			else:
				
				state[index] = "X"

				# If tree has not been built yet, build it (first human move)
				if state.count("X") == 1:
					treePossibilities = Tree.Tree(state)
			
				# Search for the node of the tree that has the current state
				for child in treePossibilities.currentNode.children:
					if child.boardState == state:
						treePossibilities.currentNode = child

				# Print human play
				printBoard(state)

				# Check if game is over
				end = checkEnd(state)

				if end == True:
					break

				print "Computer's turn:"				

				# Begin count time
				time1 = time.time()

				# Call alpha-beta pruning
				podaAlphaBeta(treePossibilities.currentNode, "MAX")

				# Search if the next play is victory or draw (never defeat)
				nextCurrentNode = None
				for child in treePossibilities.currentNode.children:
					if child.points == 1:
						nextCurrentNode = child
						break

				if nextCurrentNode is None:
					for child in treePossibilities.currentNode.children:
						if child.points == 0:
							nextCurrentNode = child
							break
				
				# Stop counting time
				pcTime += time.time() - time1

				# Set the currentNode and the state according to the
				# machine's play
				treePossibilities.currentNode = nextCurrentNode
				state = list(treePossibilities.currentNode.boardState)

				# Print computer's play
				printBoard(state)

				# Check if game is over
				end = checkEnd(state)

		# Error treatment
		except:
			if end is False:
				print "Invalid play. Try again."

	print "Total of processing time of machine:", pcTime


def podaAlphaBeta(node, max_or_min):
	"""Function that implements Alpha-Beta pruning algorithm"""

	if node.leaf is False:
		for childNode in node.children:
			if max_or_min == "MAX":
				if node.points is not None:
					if childNode.points is None:
						podaAlphaBeta(childNode, "MIN")
					
					if childNode.points > node.points:
							node.points = childNode.points
					

				elif node.points is None:
					if childNode.points is None:
						podaAlphaBeta(childNode, "MIN")					
					node.points = childNode.points
					

			elif max_or_min == "MIN":
				if node.points is not None:
					if childNode.points is None:
						podaAlphaBeta(childNode, "MAX")
					
					if childNode.points < node.points:
							node.points = childNode.points
					

				elif node.points is None:
					if childNode.points is None:
						podaAlphaBeta(childNode, "MAX")
					node.points = childNode.points


def printBoard(boardState):

	board = list(boardState)
	for i in range(0, 9):
		if board[i] is None:
			board[i] = " "

	print
	for i in range (0, 3):
		print " " + board[i*3 + 0] + " | " + board[i*3 + 1] + " | " + board[i*3 + 2]
		if i is not 2:
			print "-----------"
		else:
			print


if __name__ == "__main__":
	main()