import tkinter
from gui.ChessboardPainter import ChessboardPainter

def setWindowSize(window, width, height):
	geometry = '%dx%d' % (width, height)
	window.geometry(geometry)

def drawChess(x, y, chessSize, text, textColor):
	painter.setChessColor(textColor)
	painter.setChessBaseColor('#666611')
	painter.setChessSize(chessSize)
	painter.drawChess(x, y, text)

def drawOutline(width, height):
	margin=20
	painter.drawRectangle(margin, margin, width-margin*2, height-margin*2, 3)

def drawBackground(width, height):
	painter.clearBoard(width, height)

def setWindowTitle(window, title):
	window.title(title)

def repaintCanvas(width, height):
	drawBackground(width, height)
	drawOutline(width, height)
	drawChess(120, 120, 50, '相', '#ff3333')

def onResize(event):
	'''
	print(type(event))
	print(event.width)
	print(event.height)
	print(event.type)
	print(type(event.widget))
	'''
	repaintCanvas(event.width, event.height)

def onLButtonClick(event):
	print(event.x, event.y)
	drawChess(event.x, event.y, 50, '相', '#ff3333')

rootWindow = tkinter.Tk()

cv = tkinter.Canvas(rootWindow)
painter = ChessboardPainter(cv)
painter.setBoardColor('grey')

setWindowSize(rootWindow, 440, 484)
rootWindow.minsize(100, 200)
setWindowTitle(rootWindow, '中国象棋')

cv.bind('<Configure>', onResize)
cv.bind('<Button-1>', onLButtonClick)

cv.pack(fill=tkinter.BOTH, expand=1)
rootWindow.mainloop()
