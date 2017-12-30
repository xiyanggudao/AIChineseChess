from chess.Chessman import Chessman
from chess.ChessData import ChessmanOnBoard
from chess.ChessData import Move
import numpy as np

initChessboard = (
	(Chessman.redRook(), Chessman.redKnight(), Chessman.redElephant(), Chessman.redMandarin(), Chessman.redKing(), Chessman.redMandarin(), Chessman.redElephant(), Chessman.redKnight(), Chessman.redRook()),
	(Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid()),
	(Chessman.invalid(), Chessman.redCannon(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.redCannon(), Chessman.invalid()),
	(Chessman.redPawn(), Chessman.invalid(), Chessman.redPawn(), Chessman.invalid(), Chessman.redPawn(), Chessman.invalid(), Chessman.redPawn(), Chessman.invalid(), Chessman.redPawn()),
	(Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid()),
	(Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid()),
	(Chessman.blackPawn(), Chessman.invalid(), Chessman.blackPawn(), Chessman.invalid(), Chessman.blackPawn(), Chessman.invalid(), Chessman.blackPawn(), Chessman.invalid(), Chessman.blackPawn()),
	(Chessman.invalid(), Chessman.blackCannon(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.blackCannon(), Chessman.invalid()),
	(Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid(), Chessman.invalid()),
	(Chessman.blackRook(), Chessman.blackKnight(), Chessman.blackElephant(), Chessman.blackMandarin(), Chessman.blackKing(), Chessman.blackMandarin(), Chessman.blackElephant(), Chessman.blackKnight(), Chessman.blackRook())
)

class Chessgame:

	def __init__(self):

		self.__board = np.array(initChessboard, np.int32).transpose()
		self.__activeColor = Chessman.red
		self.__moves = []
		self.__movesBackup = []

	def moveSize(self):
		return len(self.__moves)

	def moveAt(self, index):
		return self.__moves[index]

	def makeMove(self, fromPos, toPos):
		self.__moves.append(Move(fromPos, toPos, self.chessmanAt(fromPos), self.chessmanAt(toPos)))
		self.__activeColor = Chessman.oppositeColor(self.__activeColor)
		if fromPos != toPos:
			self.__board[toPos] = self.__board[fromPos]
			self.__board[fromPos] = Chessman.invalid()
		if len(self.__movesBackup) > 0:
			self.__movesBackup.clear()

	def undoMove(self):
		if len(self.__moves) > 0:
			move = self.__moves.pop()
			self.__activeColor = Chessman.oppositeColor(self.__activeColor)
			self.__board[move.fromPos] = move.moveChessman
			self.__board[move.toPos] = move.ateChessman
			self.__movesBackup.append(move)

	def redoMove(self):
		if len(self.__movesBackup) > 0:
			move = self.__movesBackup.pop()
			self.__activeColor = Chessman.oppositeColor(self.__activeColor)
			self.__board[move.fromPos] = Chessman.invalid()
			self.__board[move.toPos] = move.moveChessman
			self.__moves.append(move)

	def chessmenOnBoard(self):
		ret = list()
		for y in range(10):
			for x in range(9):
				if self.__board[x, y]:
					chess = ChessmanOnBoard((x, y), self.__board[x, y])
					ret.append(chess)
		return ret

	def board(self):
		return self.__board.copy()

	def chessmanAt(self, pos):
		return self.__board[pos]

	def activeColor(self):
		return self.__activeColor

	def lastMove(self):
		if len(self.__moves) > 0:
			return self.__moves[len(self.__moves) - 1]

	def ucciFen(self):
		ret = ''
		for y in range(9, -1, -1):
			blank = 0
			for x in range(9):
				piece = self.__board[x, y]
				if piece == Chessman.invalid():
					blank += 1
				else:
					if blank != 0:
						ret += str(blank)
						blank = 0
					ret += Chessman.ucciFenOfChessman(piece)
			if blank != 0:
				ret += str(blank)
			if y != 0:
				ret += '/'
		ret += ' '
		ret += Chessman.ucciFenOfColor(self.activeColor())
		ret += ' - - 0 1'
		return ret

	def setWithUcciFen(self, ucciFen):
		self.__board.fill(Chessman.invalid())
		index = 0
		y = 9
		while y >= 0:
			x = 0
			while x < 9:
				if '0' <= ucciFen[index] <= '9':
					x += ord(ucciFen[index]) - ord('0')
				else:
					self.__board[x, y] = Chessman.chessmanOfUcciFen(ucciFen[index])
					x += 1
				index += 1
			index += 1
			y -= 1
		self.__activeColor = Chessman.colorOfUcciFen(ucciFen[index])
