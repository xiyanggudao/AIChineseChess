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
		self.__posCalculator.setPadding(7)
		self.__posCalculator.setChessmanSpacing(5)
		self.__posCalculator.setBoundarySpacing(3)

		self.__chessmenOnBoard = []

	def __onResize(self, event):
		self.__posCalculator.setChessboardSize(event.width, event.height)
		self.__posCalculator.setMargin(self.__posCalculator.chessmanSize()//2+5)
		self.refresh()

	def __onLButtonClick(self, event):
		print(event.x, event.y)

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
			x1,y1 = self.__posCalculator.positionAtCoordinate(0,row)
			x2,y2 = self.__posCalculator.positionAtCoordinate(8,row)
			self.__painter.drawLine(x1,y1,x2,y2,1)
		for row in range(6, 9):
			x1,y1 = self.__posCalculator.positionAtCoordinate(0,row)
			x2,y2 = self.__posCalculator.positionAtCoordinate(8,row)
			self.__painter.drawLine(x1,y1,x2,y2,1)
		for col in range(1, 8):
			x1, y1 = self.__posCalculator.positionAtCoordinate(col, 0)
			x2, y2 = self.__posCalculator.positionAtCoordinate(col, 4)
			self.__painter.drawLine(x1, y1, x2, y2, 1)
			x1, y1 = self.__posCalculator.positionAtCoordinate(col, 5)
			x2, y2 = self.__posCalculator.positionAtCoordinate(col, 9)
			self.__painter.drawLine(x1, y1, x2, y2, 1)

	def __drawCross(self):
		x1,y1 = self.__posCalculator.positionAtCoordinate(3,0)
		x2,y2 = self.__posCalculator.positionAtCoordinate(5,2)
		self.__painter.drawLine(x1,y1,x2,y2,1)
		x1,y1 = self.__posCalculator.positionAtCoordinate(5,0)
		x2,y2 = self.__posCalculator.positionAtCoordinate(3,2)
		self.__painter.drawLine(x1,y1,x2,y2,1)
		x1,y1 = self.__posCalculator.positionAtCoordinate(3,7)
		x2,y2 = self.__posCalculator.positionAtCoordinate(5,9)
		self.__painter.drawLine(x1,y1,x2,y2,1)
		x1,y1 = self.__posCalculator.positionAtCoordinate(5,7)
		x2,y2 = self.__posCalculator.positionAtCoordinate(3,9)
		self.__painter.drawLine(x1,y1,x2,y2,1)

	# 楚河汉界
	def __drawBoundary(self):
		x1,y1 = self.__posCalculator.positionAtCoordinate(0,4)
		x2,y2 = self.__posCalculator.positionAtCoordinate(8,4)
		self.__painter.drawLine(x1,y1,x2,y2,2)
		x1,y1 = self.__posCalculator.positionAtCoordinate(0,5)
		x2,y2 = self.__posCalculator.positionAtCoordinate(8,5)
		self.__painter.drawLine(x1,y1,x2,y2,2)

	def __drawChessman(self, chess):
		color = '#880000' if chess.color == Chessman.red else '#111111'
		self.__painter.setChessColor(color)
		self.__painter.setChessSize(self.__posCalculator.chessmanSize())
		x, y = self.__posCalculator.positionAtCoordinate(chess.x, chess.y)
		self.__painter.drawChess(x, y, Chessman.text(chess.identifier))

	def __drawChessmen(self):
		for chess in self.__chessmenOnBoard:
			self.__drawChessman(chess)

	def __drawSelection(self):
		pass

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
		self.__drawChessmen()
		self.__drawSelection()

	def setOnMoveListener(self, listener):
		pass
