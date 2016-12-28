import board
import random
import copy


def perft(board, depth):
	if board.last_move_won() or depth == 0:
		return 1

	sum = 0

	moves = board.generate_moves()	
	
	for move in moves:

		#print('move:' + board.player)
		board.make_move(move)
		sum += perft(board, depth - 1)
		board.unmake_last_move()
	return sum	

def find_win(board, depth):
	maxplayer = board.player 
	#print('player is' + maxplayer)
	result = negamax(board, depth, maxplayer)
	#result = minimax(board, depth, maxplayer, True)
	print('result is' + str(result))

	if result == 0:
		return 'NO FORCED WIN IN ' + str(depth) + ' MOVES'

	elif result == 1:
		move = board.move_history[len(board.move_history)-1][2]
		return 'WIN BY PLAYING ' + str(move)

	elif result == -1:
		return 'ALL MOVES LOSE'
"""
def negamax_root(board, depth):
	minimax_value = -100
	if board.last_move_won():
		if board.player != maxplayer:
			print('fixed player is ' + maxplayer)
			print('maxim has won' + str(1))
			return (1, none)
		
		elif board.player == maxplayer:
			return -1

"""
def minimax(board, depth, maxplayer, maximizingPlayer):  
	if board.last_move_won():
		if board.player != maxplayer:
			print('fixed player is ' + maxplayer)
			print('maxim has won' + str(1))
			return -1

		else:
			return 1

	if depth == 0 or board.isBoardFull():
		return 0

	moves = board.generate_moves()
	values1 = []

	if maximizingPlayer:
		bestValue = -100
		for move in moves:
			board.make_move(move)
			value1 = minimax(board, depth -1, maxplayer, False)
			board.unmake_last_move()
			values1.append(value1)
			bestValue = max(values1)
		return bestValue

	else:
		bestValue = 100
		values2 = []
		for move in moves:
			board.make_move(move)
			value2 = minimax(board, depth -1,maxplayer, True)
			board.unmake_last_move()
			values2.append(value2)
			bestValue = min(values2)
		return bestValue


def negamax(board, depth, maxplayer):
	
	if board.last_move_won():
		if board.player != maxplayer:
			print('fixed player is ' + maxplayer)
			print('maxim has won' + str(1))
			return -1
		
		elif board.player == maxplayer:
			return 1

	if depth == 0 or board.isBoardFull():
		return 0

	
	moves = board.generate_moves()
	values =[]
	for move in moves:
		board.make_move(move)
		print(board)
		value = -negamax(board, depth -1, maxplayer)
		values.append(value)
		print(values)
		#print('outside if value' + str(value))
		board.unmake_last_move()
		#print(board)


	return max(values)


def AlphaBetaWithNegamax(board, alpha, beta, depth):
	if board.last_move_won():
		return 1

	if depth == 0:
		return 0

	moves = board.generate_moves()

	for move in moves:

		board.make_move(move)
		v = -1 * AlphaBetaWithNegamax(board, -1*beta, -1*alpha, depth -1)
		board.unmake_last_move()

		if v >= beta:
			return beta

		if v > alpha:
			alpha = v

	return alpha




