
class PositionCalculator:

	def __init__(self):
		self.__width = 0
		self.__height = 0
		self.__margin = 0
		self.__padding = 0
		self.__spacing = 0

	def getOutlinePos(self):
		retX, retY = self.__margin, self.__margin
		return (retX, retY)

	def getBorderPos(self):
		indent = self.__margin + self.__padding
		retX, retY = indent, indent
		return (retX, retY)

	def getCoordinatePos(self, x, y):
		retX, retY = self.getBorderPos()
		return (retX, retY)

	def setMargin(self, margin):
		self.__margin = margin

	def setPadding(self, padding):
		self.__padding = padding

	def setBoardSize(self, width, height):
		self.__width = width
		self.__height = height

	def setChessSpacing(self, spacing):
		self.__spacing = spacing


