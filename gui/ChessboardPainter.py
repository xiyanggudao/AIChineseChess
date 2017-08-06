
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
		self.__canvas.delete('x') # 不清理会有内存泄漏
		self.__canvas.create_rectangle(0, 0, width, height, fill=self.__boardColor)

	# (x, y) 是左上角的坐标
	def drawRectangle(self, x, y, width, height, boardWidth):
		self.__canvas.create_rectangle(x, y, x+width, y+height, width=boardWidth,tag='x')

	def drawLine(self, x1, y1, x2, y2, width):
		self.__canvas.create_line(x1, y1, x2, y2, width=width,tag='x')

	# (x, y) 是棋子中心的坐标
	def drawChess(self, x, y, name):
		left = x-self.__chessSize//2
		right = left+self.__chessSize
		top = y-self.__chessSize//2
		bottom = top+self.__chessSize
		textSize = int(0.7*self.__chessSize)
		font = '-family 楷体 -size %d'%textSize

		self.__canvas.create_oval(left, top, right, bottom, fill=self.__chessBaseColor,tag='x')
		self.__canvas.create_text((x, y), text=name, fill=self.__chessColor, font=font,tag='x')

	def drawText(self, x, y, text):
		textSize = int(0.7 * self.__chessSize)
		font = '-family 隶书 -size %d' % textSize
		self.__canvas.create_text((x, y), text=text, fill='black', font=font,tag='x')


