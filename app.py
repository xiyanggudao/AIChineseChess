import tkinter
from gui.Chessboard import Chessboard
from chess.Chessgame import Chessgame

def setWindowSize(window, width, height):
	geometry = '%dx%d' % (width, height)
	window.geometry(geometry)

def onClick(pos):
	if pos == None:
		return
	selectionSize = board.selectionSize()
	if selectionSize == 0:
		chessmanId = game.chessmanAt(pos)
		if chessmanId:
			board.addToSelection(pos)
			board.refresh()
	elif selectionSize == 1:
		board.addToSelection(pos)
		game.makeMove(board.selectedPos(0), board.selectedPos(1))
		board.setChessmenOnBoard(game.chessmenOnBoard())
		board.refresh()
	elif selectionSize == 2:
		board.clearSelection()
		chessmanId = game.chessmanAt(pos)
		if chessmanId:
			board.addToSelection(pos)
		board.refresh()

rootWindow = tkinter.Tk()

cv = tkinter.Canvas(rootWindow)

game = Chessgame()
board = Chessboard(cv)
board.setChessmenOnBoard(game.chessmenOnBoard())

board.setMoveEventListener(onClick)

miniW, miniH = board.minimumSize()
rootWindow.minsize(miniW, miniH)

rootWindow.title('中国象棋---妖刀')
setWindowSize(rootWindow, miniW, miniH+5)

cv.pack(fill=tkinter.BOTH, expand=1)
rootWindow.mainloop()
