import tkinter
from gui.Chessboard import Chessboard
from chess.Chessgame import Chessgame
from chess.ChessData import Move
from chess.ChessRule import ChessRule
from chess.Chessman import Chessman

def setWindowSize(window, width, height):
	geometry = '%dx%d' % (width, height)
	window.geometry(geometry)

def onClick(pos):
	if pos == None:
		return
	selectionSize = board.selectionSize()
	if selectionSize == 0:
		chessmanId = game.chessmanAt(pos)
		if chessmanId and Chessman.color(chessmanId) == game.activeColor():
			board.addToSelection(pos)
			board.refresh()
	elif selectionSize == 1:
		board.addToSelection(pos)
		move = Move(board.selectedPos(0), board.selectedPos(1),
			game.chessmanAt(board.selectedPos(0)), game.chessmanAt(board.selectedPos(1)))
		rule.setChessmenOnBoard(game.chessmenOnBoard())
		rule.setActiveColor(game.activeColor())
		if rule.isMoveLegal(move):
			game.makeMove(board.selectedPos(0), board.selectedPos(1))
			board.setChessmenOnBoard(game.chessmenOnBoard())
		else:
			board.clearSelection()
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
rule = ChessRule()

board.setMoveEventListener(onClick)

miniW, miniH = board.minimumSize()
rootWindow.minsize(miniW, miniH)

rootWindow.title('中国象棋---妖刀')
setWindowSize(rootWindow, miniW, miniH+5)

cv.pack(fill=tkinter.BOTH, expand=1)
rootWindow.mainloop()
