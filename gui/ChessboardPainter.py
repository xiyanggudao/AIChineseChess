
# 对canvas的封装
class ChessboardPainter:

	def __init__(self, canvas):
		self.__canvas = canvas
		self.__boardColor = None
		self.__chessColor = None
		self.__chessBaseColor = None
		self.__chessSize = 0

	def setBoardColor(self, boardColor):
		self.__boardColor = boardColor

	def setChessColor(self, chessColor):
		self.__chessColor = chessColor

	def setChessBaseColor(self, chessBaseColor):
		self.__chessBaseColor = chessBaseColor

	def setChessSize(self, chessSize):
		self.__chessSize = chessSize

	def clearBoard(self, width, height):
		self.__canvas.create_rectangle(0, 0, width, height, fill=self.__boardColor)

	# (x, y) 是左上角的坐标
	def drawRectangle(self, x, y, width, height, boardWidth):
		self.__canvas.create_rectangle(x, y, x+width, y+height, width=boardWidth)

	# (x, y) 是棋子中心的坐标
	def drawChess(self, x, y, name):
		left = x-self.__chessSize//2
		right = left+self.__chessSize
		top = y-self.__chessSize//2
		bottom = top+self.__chessSize
		textSize = int(0.7*self.__chessSize)
		font = '-family 楷体 -size %d'%textSize

		self.__canvas.create_oval(left, top, right, bottom, fill=self.__chessBaseColor)
		self.__canvas.create_text((x, y), text=name, fill=self.__chessColor, font=font)


