from chess.ChessRule import ChessRule
from chess.ChessData import Move

class MoveGenerator:

	def __init__(self, game):
		self.game = game

	def generateLegalMoves(self):
		moves = []
		rule = ChessRule()
		rule.setChessmenOnBoard(self.game.chessmenOnBoard())
		rule.setActiveColor(self.game.activeColor())
		for x1 in range(9):
			for y1 in range(10):
				for x2 in range(9):
					for y2 in range(10):
						move = Move(
							(x1, y1), (x2, y2),
							self.game.chessmanAt((x1, y1)),
							self.game.chessmanAt((x2, y2))
						)
						if rule.isMoveLegal(move):
							moves.append(move)
		return moves
