from chess.Chessman import Chessman
from chess.ChessData import Move
import numpy as np

class ChessRule:

	def __init__(self):
		self.__activeColor = None
		self.__board = np.empty((9, 10), np.int32)
		self.__board.fill(Chessman.invalid())

	def __clearChessboard(self):
		self.__board.fill(Chessman.invalid())

	def __isPositionLegal(self, position):
		return 0 <= position[0] <= 8 and 0 <= position[1] <= 9

	def isPositionRangeLegal(self, move):
		if move.fromPos == move.toPos:
			return False
		return self.__isPositionLegal(move.fromPos) and self.__isPositionLegal(move.toPos)

	def setChessmenOnBoard(self, chessmenOnBoard):
		self.__clearChessboard()
		for chessman in chessmenOnBoard:
			self.__board[chessman.position] = chessman.identifier

	def setBoard(self, board):
		self.__board = board

	def setActiveColor(self, activeColor):
		self.__activeColor = activeColor

	def isMoveRightColor(self, move):
		if move.moveChessman != Chessman.invalid() and Chessman.color(move.moveChessman) == self.__activeColor:
			return True
		return False

	def isMoveConformToChessboard(self, move):
		if self.__board[move.fromPos] != move.moveChessman:
			return False
		if self.__board[move.toPos] != move.ateChessman:
			return False
		return True

	def isEatSelf(self, move):
		if move.moveChessman == Chessman.invalid() or move.ateChessman == Chessman.invalid():
			return False
		return Chessman.color(move.moveChessman) == Chessman.color(move.ateChessman)

	def __isMoveOfKingLegal(self, move, minY, maxY):
		toX, toY = move.toPos
		if not (3 <= toX <= 5 and minY <= toY <= maxY):
			return False
		fromX, fromY = move.fromPos
		distance = abs(toX - fromX) + abs(toY - fromY)
		return distance == 1

	def __isKingsMeet(self, king1Pos, king2Pos):
		k1X, k1Y = king1Pos
		k2X, k2Y = king2Pos
		if k1X == k2X:
			for i in range(min(k1Y, k2Y)+1, max(k1Y, k2Y)):
				if self.__board[k1X, i]:
					return False
			return True
		return False

	def isMoveOfRedKingLegal(self, move):
		if move.ateChessman == Chessman.blackKing():
			return self.__isKingsMeet(move.fromPos, move.toPos)
		return self.__isMoveOfKingLegal(move, 0, 2)

	def isMoveOfBlackKingLegal(self, move):
		if move.ateChessman == Chessman.redKing():
			return self.__isKingsMeet(move.fromPos, move.toPos)
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
		return self.__board[eyeX, eyeY] == Chessman.invalid()

	def isMoveOfRedElephantLegal(self, move):
		return self.__isMoveOfElephantLegal(move, 0, 4)

	def isMoveOfBlackElephantLegal(self, move):
		return self.__isMoveOfElephantLegal(move, 5, 9)

	def isMoveOfKnightLegal(self, move):
		fromX, fromY = move.fromPos
		toX, toY = move.toPos
		if abs(toX - fromX) == 2:
				return abs(toY-fromY) == 1 and self.__board[(fromX+toX)//2, fromY] == Chessman.invalid()
		elif abs(toY-fromY) == 2:
				return abs(toX-fromX) == 1 and self.__board[fromX, (fromY+toY)//2] == Chessman.invalid()
		return False

	def isMoveOfRookLegal(self, move):
		fromX, fromY = move.fromPos
		toX, toY = move.toPos
		if fromX == toX:
			for i in range(min(fromY,toY)+1, max(fromY,toY)):
				if self.__board[fromX, i]:
					return False
			return True
		elif fromY == toY:
			for i in range(min(fromX,toX)+1, max(fromX,toX)):
				if self.__board[i, fromY]:
					return False
			return True
		return False

	def isMoveOfCannonLegal(self, move):
		fromX, fromY = move.fromPos
		toX, toY = move.toPos
		overCnt = 0
		if fromX == toX:
			for i in range(min(fromY,toY)+1, max(fromY,toY)):
				if self.__board[fromX, i]:
					overCnt += 1
		elif fromY == toY:
			for i in range(min(fromX,toX)+1, max(fromX,toX)):
				if self.__board[i, fromY] != Chessman.invalid():
					overCnt += 1
		else:
			return False
		return overCnt == 0 and self.__board[move.toPos] == Chessman.invalid() or overCnt == 1 and self.__board[move.toPos]

	def isMoveOfRedPawnLegal(self, move):
		fromX, fromY = move.fromPos
		toX, toY = move.toPos	
		if toY - fromY == 1:
			return fromX == toX
		elif abs(toX-fromX) == 1:
			return fromY == toY and fromY > 4
		return False

	def isMoveOfBlackPawnLegal(self, move):
		fromX, fromY = move.fromPos
		toX, toY = move.toPos
		if toY - fromY == -1:
			return fromX == toX
		elif abs(toX-fromX) == 1:
			return fromY == toY and fromY < 5
		return False

	def __isMoveOfChessmanLegal(self, move):
		if move.moveChessman in chessmanToFuncMap:
			return chessmanToFuncMap[move.moveChessman](self, move)
		return False

	def __isChecked(self, color):
		if color == Chessman.red:
			kingRangeY = range(0, 3)
		elif color == Chessman.black:
			kingRangeY = range(7, 10)
		else:
			return False

		kingPos = None
		king = Chessman.identifier(Chessman.king, color)
		for x in range(3, 6):
			for y in kingRangeY:
				if self.__board[x, y] == king:
					kingPos = (x, y)
					break
			if kingPos:
				break

		if kingPos == None:
			return False

		for x in range(0, 9):
			for y in range(0, 10):
				chessman = self.__board[x, y]
				if chessman and Chessman.color(chessman) != color:
					move = Move((x, y), kingPos, chessman, king)
					if self.__isMoveOfChessmanLegal(move):
						return True

		return False

	def isCheckedAfterMove(self, move):
		self.__board[move.fromPos] = Chessman.invalid()
		self.__board[move.toPos] = move.moveChessman
		ret = self.__isChecked(Chessman.color(move.moveChessman))
		self.__board[move.fromPos] = move.moveChessman
		self.__board[move.toPos] = move.ateChessman
		return ret

	def isMoveLegal(self, move):
		if not self.isPositionRangeLegal(move):
			return False
		if not self.isMoveRightColor(move):
			return False
		if not self.isMoveConformToChessboard(move):
			return False
		if self.isEatSelf(move):
			return False
		if not self.__isMoveOfChessmanLegal(move):
			return False
		if self.isCheckedAfterMove(move):
			return False
		return True

chessmanToFuncMap = {
	Chessman.redKing() :ChessRule.isMoveOfRedKingLegal,
	Chessman.redMandarin(): ChessRule.isMoveOfRedMandarinLegal,
	Chessman.redElephant(): ChessRule.isMoveOfRedElephantLegal,
	Chessman.redKnight(): ChessRule.isMoveOfKnightLegal,
	Chessman.redRook(): ChessRule.isMoveOfRookLegal,
	Chessman.redCannon(): ChessRule.isMoveOfCannonLegal,
	Chessman.redPawn(): ChessRule.isMoveOfRedPawnLegal,
	Chessman.blackKing() :ChessRule.isMoveOfBlackKingLegal,
	Chessman.blackMandarin(): ChessRule.isMoveOfBlackMandarinLegal,
	Chessman.blackElephant(): ChessRule.isMoveOfBlackElephantLegal,
	Chessman.blackKnight(): ChessRule.isMoveOfKnightLegal,
	Chessman.blackRook(): ChessRule.isMoveOfRookLegal,
	Chessman.blackCannon(): ChessRule.isMoveOfCannonLegal,
	Chessman.blackPawn(): ChessRule.isMoveOfBlackPawnLegal
}