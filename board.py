
class Board:
	
	move_history = []

	def __init__(self):

		self.empty = '_'
		self.board_width = 7
		self.board_height = 6
		self.player1 = 'g'
		self.player2 = 'b'
		self.player = self.player1
		self.board = []
		self.emptyBoard = True
		self.count = 0
		self.winning = ''

		for i in range(self.board_width):
			self.board.append([self.empty] * self.board_height)
	

	def isValidMove(self, move):
		if self.board[move][0] != '_':
		    return False

		return True

	def generate_moves(self):
		moves = []
		for move in range(self.board_width):
			if self.isValidMove(move):
				moves.append(move)
		return moves
			

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

	def unmake_last_move(self):
		x = Board.move_history[len(Board.move_history)-1][0]
		y = Board.move_history[len(Board.move_history)-1][1]
		value = Board.move_history[len(Board.move_history)-1][2]
		self.player = value
		self.board[x][y] = self.empty
		Board.move_history.remove(Board.move_history[len(Board.move_history)-1])
		#str(self.board)

	def last_move_won(self):
		color = ''		
		if len(Board.move_history) <= 6:
			return False

		if(self.player == 'g'):
			color = 'b'
		else:
			color ='g'		

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

	def isBoardFull(self):
	    for x in range(self.board_width):
	        for y in range(self.board_height):
	            if self.board[x][y] == self.empty:
	                return False
	    return True

	def __str__(self):
		state = ''
		for i in range(self.board_height):
			for j in range(self.board_width):
				state += ' ' + self.board[j][i]
			state += '\n'
		#print(state)
		return state;
	
	
