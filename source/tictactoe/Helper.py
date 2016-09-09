def winner(state):

		# Diagonal win
		if state[0] == state[4] == state[8] == "X":
			return "X"
		elif state[2] == state[4] == state[6] == "X":
			return "X"
		elif state[0] == state[4] == state[8] == "O":
			return "O"
		elif state[2] == state[4] == state[6] == "O":
			return "O"

		# Line win
		for i in range(0, 3):
			if state[0 + i*3] == state[1 + i*3] == state[2 + i*3] == "X":
				return "X"
			elif state[0 + i*3] == state[1 + i*3] == state[2 + i*3] == "O":
				return "O"

		# Column win
		for j in range(0, 3):
			if state[j + 0] == state[j + 3] == state[j + 6] == "X":
				return "X"
			elif state[j + 0] == state[j + 3] == state[j + 6] == "O":
				return "O"

		draw = True
		if state.count(None) != 0:
			draw = False

		if draw == True:
			return "draw"
		else:
			return None

def checkEnd(state):

	if winner(state) is "X":
		print "Congrats!!! You won! :)"
		return True
	elif winner(state) is "O":
		print "Sorry, You lost! :("
		return True
	elif winner(state) is "draw":
		print "No one won. :|"
		return True
	else:
		return False

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