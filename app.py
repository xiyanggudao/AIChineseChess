import tkinter
from gui.Chessboard import Chessboard
from chess.Chessgame import Chessgame

def setWindowSize(window, width, height):
	geometry = '%dx%d' % (width, height)
	window.geometry(geometry)

rootWindow = tkinter.Tk()

cv = tkinter.Canvas(rootWindow)

game = Chessgame()
board = Chessboard(cv)
board.setChessmenOnBoard(game.aliveChessmen())

miniW, miniH = board.minimumSize()
rootWindow.minsize(miniW, miniH)

rootWindow.title('中国象棋')
setWindowSize(rootWindow, miniW, miniH+5)

cv.pack(fill=tkinter.BOTH, expand=1)
rootWindow.mainloop()
