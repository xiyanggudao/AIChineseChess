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
		pass

	def getMoveSize(self):
		return 0