from gui.ChessboardPainter import ChessboardPainter
from gui.PositionCalculator import PositionCalculator
from chess.Chessman import Chessman

class Chessboard:

	def __init__(self, canvas):
		canvas.bind('<Configure>', self.__onResize)
		canvas.bind('<Button-1>', self.__onLButtonClick)

		self.__painter = ChessboardPainter(canvas)
		self.__painter.setBoardColor('grey')
		self.__painter.setChessBaseColor('#888811')

		self.__posCalculator = PositionCalculator()
		self.__posCalculator.setChessmanSpacing(5)
		self.__posCalculator.setBoundarySpacing(3)

		self.__chessmenOnBoard = []

		self.__selection = []
		self.__onClickListener = None

	def __positionAtScreen(self, x, y):
		# 棋盘坐标左下角为原点，屏幕坐标左上角为原点，需要转换
		y = 9-y
		return self.__posCalculator.positionAtScreen(x, y)

	def __positionAtBoard(self, x, y):
		pos = self.__posCalculator.positionAtBoard(x, y)
		if pos:
			return (pos[0], 9-pos[1])

	def __onResize(self, event):
		self.__posCalculator.setChessboardSize(event.width, event.height)
		self.__posCalculator.setMargin(self.__posCalculator.chessmanSize()//2+5)
		self.__posCalculator.setPadding(self.__posCalculator.chessmanSize()//8)

		self.__painter.setChessSize(self.__posCalculator.chessmanSize())
		self.refresh()

	def __onLButtonClick(self, event):
		pos = self.__positionAtBoard(event.x, event.y)
		if self.__onClickListener:
			self.__onClickListener(pos)

	def __drawBackground(self):
		width, height = self.__posCalculator.boardSize()
		self.__painter.clearBoard(width, height)

	def __drawOutline(self):
		x, y = self.__posCalculator.outlinePos()
		width, height = self.__posCalculator.outlineSize()
		self.__painter.drawRectangle(x, y, width, height, 3)

	def __drawBorder(self):
		x, y = self.__posCalculator.borderPos()
		width, height = self.__posCalculator.borderSize()
		self.__painter.drawRectangle(x, y, width, height, 2)

	def __drawGrid(self):
		for row in range(1, 4):
			x1,y1 = self.__positionAtScreen(0, row)
			x2,y2 = self.__positionAtScreen(8, row)
			self.__painter.drawLine(x1,y1,x2,y2,1)
		for row in range(6, 9):
			x1,y1 = self.__positionAtScreen(0, row)
			x2,y2 = self.__positionAtScreen(8, row)
			self.__painter.drawLine(x1,y1,x2,y2,1)
		for col in range(1, 8):
			x1, y1 = self.__positionAtScreen(col, 0)
			x2, y2 = self.__positionAtScreen(col, 4)
			self.__painter.drawLine(x1, y1, x2, y2, 1)
			x1, y1 = self.__positionAtScreen(col, 5)
			x2, y2 = self.__positionAtScreen(col, 9)
			self.__painter.drawLine(x1, y1, x2, y2, 1)

	def __drawCross(self):
		x1,y1 = self.__positionAtScreen(3, 0)
		x2,y2 = self.__positionAtScreen(5, 2)
		self.__painter.drawLine(x1,y1,x2,y2,1)
		x1,y1 = self.__positionAtScreen(5, 0)
		x2,y2 = self.__positionAtScreen(3, 2)
		self.__painter.drawLine(x1,y1,x2,y2,1)
		x1,y1 = self.__positionAtScreen(3, 7)
		x2,y2 = self.__positionAtScreen(5, 9)
		self.__painter.drawLine(x1,y1,x2,y2,1)
		x1,y1 = self.__positionAtScreen(5, 7)
		x2,y2 = self.__positionAtScreen(3, 9)
		self.__painter.drawLine(x1,y1,x2,y2,1)

	# 楚河汉界
	def __drawBoundary(self):
		x1,y1 = self.__positionAtScreen(0, 4)
		x2,y2 = self.__positionAtScreen(8, 4)
		self.__painter.drawLine(x1,y1,x2,y2,2)
		x1,y1 = self.__positionAtScreen(0, 5)
		x2,y2 = self.__positionAtScreen(8, 5)
		self.__painter.drawLine(x1,y1,x2,y2,2)

		x1,y1 = self.__positionAtScreen(1, 4)
		x2,y2 = self.__positionAtScreen(2, 5)
		self.__painter.drawText((x1+x2)//2, (y1+y2)//2, '楚')
		x1,y1 = self.__positionAtScreen(2, 4)
		x2,y2 = self.__positionAtScreen(3, 5)
		self.__painter.drawText((x1+x2)//2, (y1+y2)//2, '河')
		x1,y1 = self.__positionAtScreen(5, 4)
		x2,y2 = self.__positionAtScreen(6, 5)
		self.__painter.drawText((x1+x2)//2, (y1+y2)//2, '漢')
		x1,y1 = self.__positionAtScreen(6, 4)
		x2,y2 = self.__positionAtScreen(7, 5)
		self.__painter.drawText((x1+x2)//2, (y1+y2)//2, '界')

	def __drawFoldLine(self):
		space = self.__posCalculator.chessmanSize()//12
		length = self.__posCalculator.chessmanSize()//4
		foldLinePos = [
			(1, 2), (7, 2), (0, 3), (2, 3), (4, 3), (6, 3), (8, 3),
			(1, 7), (7, 7), (0, 6), (2, 6), (4, 6), (6, 6), (8, 6)
		]
		for pos in foldLinePos:
			x, y = self.__positionAtScreen(pos[0], pos[1])
			if (pos[0] > 0):
				self.__painter.drawLine(x-space, y+space, x-space, y+space+length, 1)
				self.__painter.drawLine(x-space, y+space, x-space-length, y+space, 1)
				self.__painter.drawLine(x-space, y-space, x-space, y-space-length, 1)
				self.__painter.drawLine(x-space, y-space, x-space-length, y-space, 1)
			if (pos[0] < 8):
				self.__painter.drawLine(x+space, y+space, x+space, y+space+length, 1)
				self.__painter.drawLine(x+space, y+space, x+space+length, y+space, 1)
				self.__painter.drawLine(x+space, y-space, x+space, y-space-length, 1)
				self.__painter.drawLine(x+space, y-space, x+space+length, y-space, 1)

	def __drawChessman(self, chess):
		color = '#880000' if chess.color == Chessman.red else '#111111'
		self.__painter.setChessColor(color)
		x, y = self.__positionAtScreen(chess.x, chess.y)
		self.__painter.drawChess(x, y, Chessman.text(chess.identifier))

	def __drawChessmen(self):
		for chess in self.__chessmenOnBoard:
			self.__drawChessman(chess)

	def __drawSelection(self):
		radius = self.__posCalculator.chessmanSize()//2
		lineLen = radius//3
		color = '#3333aa'
		for pos in self.__selection:
			x, y = self.__positionAtScreen(pos[0], pos[1])
			self.__painter.drawLine(x-radius,y-radius,x-radius+lineLen,y-radius,2,color)
			self.__painter.drawLine(x-radius,y-radius,x-radius,y-radius+lineLen,2,color)
			self.__painter.drawLine(x+radius,y-radius,x+radius-lineLen,y-radius,2,color)
			self.__painter.drawLine(x+radius,y-radius,x+radius,y-radius+lineLen,2,color)
			self.__painter.drawLine(x-radius,y+radius,x-radius+lineLen,y+radius,2,color)
			self.__painter.drawLine(x-radius,y+radius,x-radius,y+radius-lineLen,2,color)
			self.__painter.drawLine(x+radius,y+radius,x+radius-lineLen,y+radius,2,color)
			self.__painter.drawLine(x+radius,y+radius,x+radius,y+radius-lineLen,2,color)

	def minimumSize(self):
		return self.__posCalculator.boardSizeForFixedChessmanSize(50)

	def setChessmenOnBoard(self, chessmenOnBoard):
		self.__chessmenOnBoard = chessmenOnBoard

	def refresh(self):
		self.__drawBackground()
		self.__drawOutline()
		self.__drawBorder()
		self.__drawGrid()
		self.__drawCross()
		self.__drawBoundary()
		self.__drawFoldLine()
		self.__drawChessmen()
		self.__drawSelection()

	def setMoveEventListener(self, listener):
		self.__onClickListener = listener

	def selectionSize(self):
		return len(self.__selection)

	def addToSelection(self, pos):
		self.__selection.append(pos)

	def selectedPos(self, index):
		return self.__selection[index]
