from chess.Chessman import Chessman
from chess.ChessData import ChessmanOnBoard
from chess.ChessData import Move

class Chessgame:

	def __init__(self):
		rKing = Chessman.redKing()
		rMandarin = Chessman.redMandarin()
		rElephant = Chessman.redElephant()
		rKnight = Chessman.redKnight()
		rRook = Chessman.redRook()
		rCannon = Chessman.redCannon()
		rPawn = Chessman.redPawn()
		bKing = Chessman.blackKing()
		bMandarin = Chessman.blackMandarin()
		bElephant = Chessman.blackElephant()
		bKnight = Chessman.blackKnight()
		bRook = Chessman.blackRook()
		bCannon = Chessman.blackCannon()
		bPawn = Chessman.blackPawn()

		self.__board = (
			[rRook, rKnight, rElephant, rMandarin, rKing, rMandarin, rElephant, rKnight, rRook],
			[None, None, None, None, None, None, None, None, None],
			[None, rCannon, None, None, None, None, None, rCannon, None],
			[rPawn, None, rPawn, None, rPawn, None, rPawn, None, rPawn],
			[None, None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None, None],
			[bPawn, None, bPawn, None, bPawn, None, bPawn, None, bPawn],
			[None, bCannon, None, None, None, None, None, bCannon, None],
			[None, None, None, None, None, None, None, None, None],
			[bRook, bKnight, bElephant, bMandarin, bKing, bMandarin, bElephant, bKnight, bRook]
		)

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
			self.__board[toPos[1]][toPos[0]] = self.__board[fromPos[1]][fromPos[0]]
			self.__board[fromPos[1]][fromPos[0]] = None
		if len(self.__movesBackup) > 0:
			self.__movesBackup.clear()

	def undoMove(self):
		if len(self.__moves) > 0:
			move = self.__moves.pop()
			self.__activeColor = Chessman.oppositeColor(self.__activeColor)
			self.__board[move.fromPos[1]][move.fromPos[0]] = move.moveChessman
			self.__board[move.toPos[1]][move.toPos[0]] = move.ateChessman
			self.__movesBackup.append(move)

	def redoMove(self):
		if len(self.__movesBackup) > 0:
			move = self.__movesBackup.pop()
			self.__activeColor = Chessman.oppositeColor(self.__activeColor)
			self.__board[move.fromPos[1]][move.fromPos[0]] = None
			self.__board[move.toPos[1]][move.toPos[0]] = move.moveChessman
			self.__moves.append(move)

	def chessmenOnBoard(self):
		ret = list()
		for y in range(len(self.__board)):
			for x in range(len(self.__board[y])):
				if self.__board[y][x]:
					chess = ChessmanOnBoard((x, y), self.__board[y][x])
					ret.append(chess)
		return ret

	def chessmanAt(self, pos):
		return self.__board[pos[1]][pos[0]]

	def activeColor(self):
		return self.__activeColor

	def lastMove(self):
		if len(self.__moves) > 0:
			return self.__moves[len(self.__moves) - 1]
