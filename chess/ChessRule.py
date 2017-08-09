from chess.Chessman import Chessman

class ChessRule:

	def __init__(self):
		self.__activeColor = None

	def setChessmenOnBoard(self, chessmenOnBoard):
		pass

	def setActiveColor(self, activeColor):
		self.__activeColor = activeColor

	def isMoveRightColor(self, move):
		if self.__activeColor != None and Chessman.color(move.moveChessman) == self.__activeColor:
			return True
		return False

	def isMoveConformToChessboard(self, move):
		return True
