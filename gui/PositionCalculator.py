
class PositionCalculator:

	def __init__(self):
		self.__width = 0
		self.__height = 0
		self.__margin = 0
		self.__padding = 0
		self.__chessmanSpacing = 0
		self.__opposingSpacing = 0

	def getOutlinePos(self):
		retX, retY = self.__margin, self.__margin
		return (retX, retY)

	def getBorderPos(self):
		indent = self.__margin + self.__padding
		retX, retY = indent, indent
		return (retX, retY)

	def getCoordinatePos(self, x, y):
		retX, retY = self.getBorderPos()
		retX += self.__chessmanSpacing * x
		retY += self.__chessmanSpacing * y
		if y > 4:
			retY += self.__opposingSpacing
		return (retX, retY)

	def getChessmanSize(self):
		return (0, 0)

	def getOutlineSize(self):
		retWidth, retHeight = self.__width, self.__height
		retWidth -= self.__margin
		retHeight -= self.__margin
		return (retWidth, retHeight)

	def setMargin(self, margin):
		self.__margin = margin

	def setPadding(self, padding):
		self.__padding = padding

	def setChessboardSize(self, width, height):
		self.__width = width
		self.__height = height

	def setChessmanSpacing(self, spacing):
		self.__chessmanSpacing = spacing

	# 楚河汉界的宽度
	def setOpposingSpacing(self, opposingSpacing):
		self.__opposingSpacing = opposingSpacing


