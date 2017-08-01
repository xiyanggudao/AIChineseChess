
class PositionCalculator:

	def __init__(self):
		self.__width = 0
		self.__height = 0
		self.__margin = 0
		self.__padding = 0
		self.__chessmanSpacing = 0
		self.__opposingSpacing = 0

	def outlinePos(self):
		outlineSize = self.outlineSize()
		extraWidth = self.__width - outlineSize[0]
		extraHeight = self.__height - outlineSize[1]
		return (extraWidth // 2 , extraHeight // 2)

	def borderPos(self):
		retX, retY = self.outlinePos()
		retX += self.__padding
		retY += self.__padding
		return (retX, retY)

	def positionAtCoordinate(self, x, y):
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


