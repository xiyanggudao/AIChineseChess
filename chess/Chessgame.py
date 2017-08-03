from chess.Chessman import Chessman

class ChessmanOnBoard:

	def __init__(self, position, identifier):
		self.__position = position
		self.__identifier = identifier

	@property
	def position(self):
		return self.__position

	@property
	def x(self):
		return self.__position[0]

	@property
	def y(self):
		return self.__position[1]

	@property
	def identifier(self):
		return self.__identifier

	@property
	def type(self):
		return Chessman.getType(self.__identifier)

	@property
	def color(self):
		return Chessman.getColor(self.__identifier)

# 走棋数据，提供外面访问走棋历史的接口
class Move:

	def __init__(self, moveChessman, fromPos, toPos, ateChessman):
		self.__fromPos = fromPos
		self.__toPos = toPos
		self.__moveChessman = moveChessman
		self.__ateChessman = ateChessman

	@property
	def fromPos(self):
		return self.__fromPos

	@property
	def toPos(self):
		return self.__toPos

	@property
	def moveChessman(self):
		return self.__moveChessman

	@property
	def ateChessman(self):
		return self.__ateChessman

class Chessgame:

	def __init__(self):
		rKing = Chessman.getIdentifier(Chessman.king, Chessman.red)
		rMandarin = Chessman.getIdentifier(Chessman.mandarin, Chessman.red)
		rElephant = Chessman.getIdentifier(Chessman.elephant, Chessman.red)
		rKnight = Chessman.getIdentifier(Chessman.knight, Chessman.red)
		rRook = Chessman.getIdentifier(Chessman.rook, Chessman.red)
		rCannon = Chessman.getIdentifier(Chessman.cannon, Chessman.red)
		rPawn = Chessman.getIdentifier(Chessman.pawn, Chessman.red)
		bKing = Chessman.getIdentifier(Chessman.king, Chessman.black)
		bMandarin = Chessman.getIdentifier(Chessman.mandarin, Chessman.black)
		bElephant = Chessman.getIdentifier(Chessman.elephant, Chessman.black)
		bKnight = Chessman.getIdentifier(Chessman.knight, Chessman.black)
		bRook = Chessman.getIdentifier(Chessman.rook, Chessman.black)
		bCannon = Chessman.getIdentifier(Chessman.cannon, Chessman.black)
		bPawn = Chessman.getIdentifier(Chessman.pawn, Chessman.black)

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

	def moveSize(self):
		return 0

	def moveAt(self):
		pass

	def makeMove(self, fromPos, toPos):
		pass

	def undoMove(self):
		pass

	def redoMove(self):
		pass

	def aliveChessmen(self):
		ret = list()
		for i in range(0, 32):
			if self.__position[i] != None:
				chess = ChessmanOnBoard(self.__position[i], self.__chessmen[i])
				ret.append(chess)
		return ret
