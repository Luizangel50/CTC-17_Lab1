import NodeTree
from Helper import winner

class Tree:
	"""Class that implements the Tree used on the Tic Tac Toe problem"""

	def __init__(self, currentState):
		"""Constructor"""

		self.currentNode = NodeTree.NodeTree(None, None, None, None)
		state = list(currentState)

		self.buildTree(self.currentNode, state, "O")


	def buildTree(self, node, state, player):

		node.boardState = list(state)
		node.player = player

		node.children = []
		situation = winner(node.boardState)

		if situation is "X":
			node.leaf = True			
			node.winner = "X"
			node.points = -1

		elif situation is "O":
			node.leaf = True
			node.winner = "O"
			node.points = 1

		elif situation is "draw":
			node.leaf = True
			node.winner = "draw"
			node.points = 0

		else:
			for i in range (0, 9):
				if node.boardState[i] is None:
					newState = list(node.boardState)
					newNode = NodeTree.NodeTree(node, None, None, None)
					node.children.append(newNode)
					
					if player == "X":
						newState[i] = "X"
						self.buildTree(newNode, newState, "O")
					elif player == "O":
						newState[i] = "O"
						self.buildTree(newNode, newState, "X")