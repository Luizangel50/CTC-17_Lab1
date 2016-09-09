import sys

class NodeTree:
	"""Class that implements the nodes of the tree used on the Tic Tac Toe problem"""

	def __init__(self, parent, children, state, player):
		"""Constructor"""

		self.parent = parent
		self.children = children
		self.boardState = state
		self.player = player
		self.leaf = False
		self.winner = None
		self.points = None