from chess.Chessman import Chessman

class ChessRule:

	def __init__(self):
		self.__activeColor = None
		self.__board = (
			[None, None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None, None]
		)

	def __isPositionLegal(self, position):
		return 0 <= position[0] <= 8 and 0 <= position[1] <= 9

	def isPositionRangeLegal(self, move):
		return self.__isPositionLegal(move.fromPos) and self.__isPositionLegal(move.toPos)

	def setChessmenOnBoard(self, chessmenOnBoard):
		for chessman in chessmenOnBoard:
			self.__board[chessman.y][chessman.x] = chessman.identifier

	def setActiveColor(self, activeColor):
		self.__activeColor = activeColor

	def isMoveRightColor(self, move):
		if self.__activeColor != None and Chessman.color(move.moveChessman) == self.__activeColor:
			return True
		return False

	def isMoveConformToChessboard(self, move):
		fromX, fromY = move.fromPos
		toX, toY = move.toPos
		if self.__board[fromY][fromX] != move.moveChessman:
			return False
		if self.__board[toX][toY] != move.ateChessman:
			return False
		return True

	def isEatSelf(self, move):
		if move.moveChessman == None or move.ateChessman == None:
			return False
		return Chessman.color(move.moveChessman) == Chessman.color(move.ateChessman)

	def __isMoveOfKingLegal(self, move, minY, maxY):
		toX, toY = move.toPos
		if not (3 <= toX <= 5 and minY <= toY <= maxY):
			return False
		fromX, fromY = move.fromPos
		distance = abs(toX - fromX) + abs(toY - fromY)
		return distance == 1

	def isMoveOfRedKingLegal(self, move):
		return self.__isMoveOfKingLegal(move, 0, 2)

	def isMoveOfBlackKingLegal(self, move):
		return self.__isMoveOfKingLegal(move, 7, 9)

	def __isMoveOfMandarinLegal(self, move, minY, maxY):
		toX, toY = move.toPos
		if not (3 <= toX <= 5 and minY <= toY <= maxY):
			return False
		fromX, fromY = move.fromPos
		return abs(toX - fromX) == 1 and abs(toY - fromY) == 1

	def isMoveOfRedMandarinLegal(self, move):
		return  self.__isMoveOfMandarinLegal(move, 0, 2)

	def isMoveOfBlackMandarinLegal(self, move):
		return  self.__isMoveOfMandarinLegal(move, 7, 9)

	def __isMoveOfElephantLegal(self, move, minY, maxY):
		toX, toY = move.toPos
		if not (0 <= toX <= 8 and minY <= toY <= maxY):
			return False
		fromX, fromY = move.fromPos
		if not (abs(toX - fromX) == 2 and abs(toY - fromY) == 2):
			return False
		eyeX, eyeY = (fromX + toX)//2, (fromY + toY)//2
		return self.__board[eyeY][eyeX] == None

	def isMoveOfRedElephantLegal(self, move):
		return self.__isMoveOfElephantLegal(move, 0, 4)

	def isMoveOfBlackElephantLegal(self, move):
		return self.__isMoveOfElephantLegal(move, 5, 9)
