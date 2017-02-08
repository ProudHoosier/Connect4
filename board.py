##Implementation of Board for a connect 4 game.

class Board:
	# Using move history to keep track of progress of the game.
	move_history = []
	
	# Initialize Board with required parameters of a new board game.
	def __init__(self):
		self.empty = '_'
		self.board_width = 7
		self.board_height = 6
		self.player1 = 'green'
		self.player2 = 'blue'
		self.player = self.player1
		self.board = []
		self.emptyBoard = True
		self.count = 0
		self.winning = ''
		
		# enumerate the board
		for i in range(self.board_width):
			self.board.append([self.empty] * self.board_height)
	
	# determine if the move by a player is valid
	def isValidMove(self, move):
		if self.board[move][0] != '_':
		    return False

		return True
	# generate list of valid moves for the player
	def generate_moves(self):
		moves = []
		for move in range(self.board_width):
			if self.isValidMove(move):
				moves.append(move)
		return moves
			
	# change the state of the board based on the move taken by the player and switch the player.
	def make_move(self, move):		
		for i in range(self.board_height - 1, -1, -1):
			if self.board[move][i] == self.empty:
				self.board[move][i] = self.player

				Board.move_history.append((move,i,self.player))
				if(self.player == self.player1):
					self.player = self.player2
				else:
					self.player = self.player1
				self.emptyBoard = False
				return self
	
	# change the state of the board if the player unmakes the last move.
	def unmake_last_move(self):
		x = Board.move_history[len(Board.move_history)-1][0]
		y = Board.move_history[len(Board.move_history)-1][1]
		value = Board.move_history[len(Board.move_history)-1][2]
		self.player = value
		self.board[x][y] = self.empty
		Board.move_history.remove(Board.move_history[len(Board.move_history)-1])
		#str(self.board)
	
	#determine if the last move resulted in a win by checking the 4 tiles of same colour in horizontal, vertical and two diagonals.
	def last_move_won(self):
		color = ''		
		if len(Board.move_history) <= 6:
			return False

		if(self.player == 'green'):
			color = 'blue'
		else:
			color ='green'		

		# check horizontal winning
		for y in range(self.board_height):
			for x in range(self.board_width - 3):
				if self.board[x][y] == color and self.board[x+1][y] == color and self.board[x+2][y] == color and self.board[x+3][y] == color:
					self.winning = 'h'
					return True

		# check vertical winning
		for x in range(self.board_width):
			for y in range(self.board_height - 3):
				if self.board[x][y] == color and self.board[x][y+1] == color and self.board[x][y+2] == color and self.board[x][y+3] == color:
					self.winning = 'v'
					return True

		# check diagonal winning
		for x in range(self.board_width - 3):
			for y in range(3, self.board_height):
				if self.board[x][y] == color and self.board[x+1][y-1] == color and self.board[x+2][y-2] == color and self.board[x+3][y-3] == color:
					self.winning = 'd'
					return True

		# check other diagonal winning
		for x in range(self.board_width - 3):
			for y in range(self.board_height - 3):
				if self.board[x][y] == color and self.board[x+1][y+1] == color and self.board[x+2][y+2] == color and self.board[x+3][y+3] == color:
					self.winning = 'od'
					return True

		return False
	# This method determines if the board has any vacant tiles by comparing the content of a tile with empty marker.
	def isBoardFull(self):
	    for x in range(self.board_width):
	        for y in range(self.board_height):
	            if self.board[x][y] == self.empty:
	                return False
	    return True
	
	# String representation of the board for debugging purposes
	def __str__(self):
		state = ''
		for i in range(self.board_height):
			for j in range(self.board_width):
				state += ' ' + self.board[j][i]
			state += '\n'
		#print(state)
		return state;
	
	
