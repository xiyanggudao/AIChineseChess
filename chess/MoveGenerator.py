from chess.ChessRule import ChessRule
from chess.ChessData import Move
from chess.Chessman import Chessman

class MoveGenerator:

	def __init__(self, game):
		self.game = game
		self.rule = ChessRule()

	def generateLegalMoves(self):
		moves = []
		rule = self.rule
		rule.setBoard(self.game.board())
		rule.setActiveColor(self.game.activeColor())
		for x1 in range(9):
			for y1 in range(10):
				moveMan = self.game.chessmanAt((x1, y1))
				if moveMan == Chessman.invalid() or Chessman.color(moveMan) != self.game.activeColor():
					continue
				type = Chessman.type(moveMan)
				if type == Chessman.rook or type == Chessman.cannon or type == Chessman.king:
					for x2 in range(9):
						move = Move(
							(x1, y1), (x2, y1),
							moveMan,
							self.game.chessmanAt((x2, y1))
						)
						if rule.isMoveLegal(move):
							moves.append(move)
					for y2 in range(10):
						move = Move(
							(x1, y1), (x1, y2),
							moveMan,
							self.game.chessmanAt((x1, y2))
						)
						if rule.isMoveLegal(move):
							moves.append(move)
				elif type == Chessman.knight:
					kightPath = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
					for path in kightPath:
						x2, y2 = x1+path[0],y1+path[1]
						if not (0 <= x2 < 9 and 0 <= y2 < 10):
							continue
						move = Move(
							(x1, y1), (x2, y2),
							self.game.chessmanAt((x1, y1)),
							self.game.chessmanAt((x2, y2))
						)
						if rule.isMoveLegal(move):
							moves.append(move)
				elif type == Chessman.pawn:
					pawnPath = ((-1, 0), (0, -1), (0, 1), (1, 0))
					for path in pawnPath:
						x2, y2 = x1+path[0],y1+path[1]
						if not (0 <= x2 < 9 and 0 <= y2 < 10):
							continue
						move = Move(
							(x1, y1), (x2, y2),
							self.game.chessmanAt((x1, y1)),
							self.game.chessmanAt((x2, y2))
						)
						if rule.isMoveLegal(move):
							moves.append(move)
				elif type == Chessman.mandarin:
					mandarinPath = ((-1, -1), (-1, 1), (1, -1), (1, 1))
					for path in mandarinPath:
						x2, y2 = x1+path[0],y1+path[1]
						if not (0 <= x2 < 9 and 0 <= y2 < 10):
							continue
						move = Move(
							(x1, y1), (x2, y2),
							self.game.chessmanAt((x1, y1)),
							self.game.chessmanAt((x2, y2))
						)
						if rule.isMoveLegal(move):
							moves.append(move)
				elif type == Chessman.elephant:
					elephantPath = ((-2, -2), (-2, 2), (2, -2), (2, 2))
					for path in elephantPath:
						x2, y2 = x1+path[0],y1+path[1]
						if not (0 <= x2 < 9 and 0 <= y2 < 10):
							continue
						move = Move(
							(x1, y1), (x2, y2),
							self.game.chessmanAt((x1, y1)),
							self.game.chessmanAt((x2, y2))
						)
						if rule.isMoveLegal(move):
							moves.append(move)
				else:
					assert False
		return moves
