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
		return Chessman.type(self.__identifier)

	@property
	def color(self):
		return Chessman.color(self.__identifier)

	def __eq__(self, other):
		if self.__identifier != other.__identifier:
			return False
		if self.__position != other.__position:
			return False
		return True

# 走棋数据，提供外面访问走棋历史的接口
class Move:

	def __init__(self, fromPos, toPos, moveChessman, ateChessman):
		assert moveChessman is not None
		assert ateChessman is not None
		self.__fromPos = fromPos
		self.__toPos = toPos
		self.__moveChessman = moveChessman
		self.__ateChessman = ateChessman

	def __eq__(self, other):
		if self.__fromPos != other.__fromPos:
			return False
		if self.__toPos != other.__toPos:
			return False
		if self.__moveChessman != other.__moveChessman:
			return False
		if self.__ateChessman != other.__ateChessman:
			return False
		return True

	def __str__(self):
		return "<("+str(self.__fromPos[0])+", "+str(self.__fromPos[1])+", "\
			+Chessman.text(self.moveChessman)+")~("\
			+str(self.__toPos[0])+", "+str(self.__toPos[1])+", "\
			+Chessman.text(self.__ateChessman)+")>"

	def ucciStr(self):
		xs = 'abcdefghi'
		ys = '0123456789'
		fx, fy = self.__fromPos
		tx, ty = self.__toPos
		return xs[fx] + ys[fy] + xs[tx] + ys[ty]

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
