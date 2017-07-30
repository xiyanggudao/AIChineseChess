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

class Chessgame:

	def __init__(self):
		pass

	def getMoveSize(self):
		return 0