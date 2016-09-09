import sys

class Node:
	"""Class that especifies a node of the graph"""


	def __init__(self, index, axisX, axisY, listNeighbors):
		"""Constructor"""

		self.index = index						# Index (ID) of the node
		self.axisX = axisX						# X coordinate of the node
		self.axisY = axisY						# Y coordinate of the node
		self.listNeighbors = listNeighbors		# Neighbors of the node
		self.marked = False						# Mark a node that cannot be visited (used only on Greedy algorithm)
		self.cost = sys.float_info.max			# Current cost of the node (used only on A* algorithm)

