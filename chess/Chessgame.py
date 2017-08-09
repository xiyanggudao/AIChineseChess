from chess.Chessman import Chessman
from chess.ChessData import ChessmanOnBoard
from chess.ChessData import Move

class Chessgame:

	def __init__(self):
		rKing = Chessman.identifier(Chessman.king, Chessman.red)
		rMandarin = Chessman.identifier(Chessman.mandarin, Chessman.red)
		rElephant = Chessman.identifier(Chessman.elephant, Chessman.red)
		rKnight = Chessman.identifier(Chessman.knight, Chessman.red)
		rRook = Chessman.identifier(Chessman.rook, Chessman.red)
		rCannon = Chessman.identifier(Chessman.cannon, Chessman.red)
		rPawn = Chessman.identifier(Chessman.pawn, Chessman.red)
		bKing = Chessman.identifier(Chessman.king, Chessman.black)
		bMandarin = Chessman.identifier(Chessman.mandarin, Chessman.black)
		bElephant = Chessman.identifier(Chessman.elephant, Chessman.black)
		bKnight = Chessman.identifier(Chessman.knight, Chessman.black)
		bRook = Chessman.identifier(Chessman.rook, Chessman.black)
		bCannon = Chessman.identifier(Chessman.cannon, Chessman.black)
		bPawn = Chessman.identifier(Chessman.pawn, Chessman.black)

		self.__chessmen = [
			rKing,rMandarin,rMandarin,rElephant,rElephant,rKnight,rKnight,rRook,rRook,
			rCannon,rCannon,rPawn,rPawn,rPawn,rPawn,rPawn,
			bKing,bMandarin,bMandarin,bElephant,bElephant,bKnight,bKnight,bRook,bRook,
			bCannon,bCannon,bPawn,bPawn,bPawn,bPawn,bPawn
		]
		self.__position = [
			(4, 0), (3, 0), (5, 0), (2, 0), (6, 0), (1, 0), (7, 0), (0, 0), (8, 0),
			(1, 2), (7, 2), (0, 3), (2, 3), (4, 3), (6, 3), (8, 3),
			(4, 9), (3, 9), (5, 9), (2, 9), (6, 9), (1, 9), (7, 9), (0, 9), (8, 9),
			(1, 7), (7, 7), (0, 6), (2, 6), (4, 6), (6, 6), (8, 6)
		]

		self.__activeColor = Chessman.red
		self.__moves = []

	def moveSize(self):
		return len(self.__moves)

	def moveAt(self):
		pass

	def makeMove(self, fromPos, toPos):
		self.__moves.append(Move(fromPos, toPos, self.chessmanAt(fromPos), self.chessmanAt(toPos)))
		self.__activeColor = Chessman.oppositeColor(self.__activeColor)
		for i in range(0, 32):
			if self.__position[i] == toPos:
				self.__position[i] = None
		for i in range(0, 32):
			if self.__position[i] == fromPos:
				self.__position[i] = toPos

	def undoMove(self):
		pass

	def chessmenOnBoard(self):
		ret = list()
		for i in range(0, 32):
			if self.__position[i] != None:
				chess = ChessmanOnBoard(self.__position[i], self.__chessmen[i])
				ret.append(chess)
		return ret

	def chessmanAt(self, pos):
		for i in range(0, 32):
			if self.__position[i] == pos:
				return self.__chessmen[i]

	def activeColor(self):
		return self.__activeColor

	def lastMove(self):
		if len(self.__moves) > 0:
			return self.__moves[len(self.__moves) - 1]
