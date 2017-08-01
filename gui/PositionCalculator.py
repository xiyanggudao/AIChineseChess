
class PositionCalculator:

	def __init__(self):
		self.__width = 0
		self.__height = 0
		self.__margin = 0
		self.__padding = 0
		self.__chessmanSpacing = 0
		self.__opposingSpacing = 0

	def outlinePos(self):
		retX, retY = self.__margin, self.__margin
		return (retX, retY)

	def borderPos(self):
		indent = self.__margin + self.__padding
		retX, retY = indent, indent
		return (retX, retY)

	def coordinatePos(self, x, y):
		retX, retY = self.borderPos()
		cellSize = self.chessmanSize() + self.__chessmanSpacing
		retX += cellSize * x
		retY += cellSize * y
		if y > 4:
			retY += self.__opposingSpacing
		return (retX, retY)

	def chessmanSize(self):
		maxWidth = self.__width
		maxWidth -= 2*self.__margin
		maxWidth -= 2*self.__padding
		maxWidth -= 8*self.__chessmanSpacing
		maxWidth //= 8
		maxHeight  = self.__height
		maxHeight -= 2*self.__margin
		maxHeight -= 2*self.__padding
		maxHeight -= 9*self.__chessmanSpacing
		maxHeight -= self.__opposingSpacing
		maxHeight //= 9
		return min(maxWidth, maxHeight)

	def outlineSize(self):
		return self.__outlineSize(self.chessmanSize())

	def borderSize(self):
		return self.__borderSize(self.chessmanSize())

	def __borderSize(self, chessmanSize):
		retWidth, retHeight = (8*chessmanSize, 9*chessmanSize)
		retWidth += 8*self.__chessmanSpacing
		retHeight += 9*self.__chessmanSpacing
		retHeight += self.__opposingSpacing
		return (retWidth, retHeight)

	def __outlineSize(self, chessmanSize):
		retWidth, retHeight = self.__borderSize(chessmanSize)
		retWidth += 2*self.__padding
		retHeight += 2*self.__padding
		return (retWidth, retHeight)

	def boardSizeForFixedChessmanSize(self, chessmanSize):
		retWidth, retHeight = self.__outlineSize(chessmanSize)
		retWidth += 2*self.__margin
		retHeight += 2*self.__margin
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


