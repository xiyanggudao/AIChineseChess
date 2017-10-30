import tkinter
from gui.Chessboard import Chessboard
from chess.Chessgame import Chessgame
from chess.ChessData import Move
from chess.ChessRule import ChessRule
from chess.Chessman import Chessman
from brain.MoveProbability import MoveProbability
from chess.MoveGenerator import MoveGenerator
from brain.Network import Network

def setWindowSize(window, width, height):
	geometry = '%dx%d' % (width, height)
	window.geometry(geometry)

def reset():
	global game
	global moveGen
	game = Chessgame()
	moveGen = MoveGenerator(game)

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

def think():
	brain.generateProbability(game, moveGen.generateLegalMoves())
	probability = brain.probability()
	moves = brain.moves()

	for i in range(len(moves)):
		moves[i].prob = probability[i] * 100
	moves.sort(key=lambda move: move.prob, reverse=True)

	moveList.delete(0, moveList.size())
	for move in moves:
		moveStr = move.ucciStr() + ('    ' + str(round(move.prob, 2)))
		moveList.insert(moveList.size(), moveStr)
	moveList.select_set(0)

def getSelectMove():
	selectIndexs = moveList.curselection()
	if len(selectIndexs) > 0:
		item = moveList.get(selectIndexs[0])

		fx = ord(item[0]) - ord('a')
		fy = ord(item[1]) - ord('0')
		tx = ord(item[2]) - ord('a')
		ty = ord(item[3]) - ord('0')

		return Move((fx, fy), (tx, ty), None, None)

def onKey(event):
	code = event.keycode
	if code == 27: # Esc
		if board.selectionSize() > 0:
			board.clearSelection()
			board.refresh()
		else:
			rootWindow.destroy()
	elif code == 37: # Left
		game.undoMove()
		board.setChessmenOnBoard(game.chessmenOnBoard())
		board.refresh()
		think()
	elif code == 39: # Right
		game.redoMove()
		board.setChessmenOnBoard(game.chessmenOnBoard())
		board.refresh()
		think()
	elif code == 38: # Up
		selectIndexs = moveList.curselection()
		if len(selectIndexs) > 0 and selectIndexs[0] > 0:
			moveList.select_clear(selectIndexs[0])
			moveList.select_set(selectIndexs[0]-1)
	elif code == 40: # Down
		selectIndexs = moveList.curselection()
		if len(selectIndexs) > 0 and selectIndexs[0] < moveList.size():
			moveList.select_clear(selectIndexs[0])
			moveList.select_set(selectIndexs[0]+1)
	elif code == 13: # Enter
		move = getSelectMove()
		if move:
			game.makeMove(move.fromPos, move.toPos)
			board.setChessmenOnBoard(game.chessmenOnBoard())
			board.refresh()
			think()
	elif code == 82: # r
		reset()
		board.setChessmenOnBoard(game.chessmenOnBoard())
		board.refresh()
	elif code ==84: # t
		think()

def onMoveItemClick(event):
	move = getSelectMove()
	if move:
		board.clearSelection()
		board.addToSelection(move.fromPos)
		board.addToSelection(move.toPos)
		board.refresh()

rootWindow = tkinter.Tk()

cv = tkinter.Canvas(rootWindow)

reset()
board = Chessboard(cv)
board.setChessmenOnBoard(game.chessmenOnBoard())
rule = ChessRule()
network = Network("./model/20171029-08400/model.ckpt")
brain = MoveProbability(network)

board.setMoveEventListener(onClick)
rootWindow.bind('<Key>', onKey)

miniW, miniH = board.minimumSize()
rootWindow.minsize(miniW, miniH)

rootWindow.title('中国象棋 - 妖刀')
setWindowSize(rootWindow, miniW, miniH+5)

toolWindow = tkinter.Toplevel(rootWindow)
toolWindow.title('走法')
toolWindow.geometry('300x900')
moveList  = tkinter.Listbox(toolWindow)
moveList.bind('<<ListboxSelect>>',onMoveItemClick)
think()
moveList.pack(fill=tkinter.BOTH, expand=1)

cv.pack(fill=tkinter.BOTH, expand=1)
rootWindow.mainloop()
