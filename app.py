import tkinter
from gui.Chessboard import Chessboard
from chess.Chessgame import Chessgame
from chess.ChessData import Move
from chess.ChessRule import ChessRule
from chess.Chessman import Chessman
from brain.MoveProbability import MoveProbability
from chess.MoveGenerator import MoveGenerator
from brain.Network import Network
import time

def setWindowSize(window, width, height):
	geometry = '%dx%d' % (width, height)
	window.geometry(geometry)

def reset():
	global training
	global noEatCnt
	global game
	training = False
	noEatCnt = 0
	game = Chessgame()

def endGame(result):
	print('train started', result)
	start = time.time()
	i = 0
	trainGame = Chessgame()
	while i < game.moveSize():
		move = game.moveAt(i)
		moveGen = MoveGenerator(trainGame)
		moves = moveGen.generateLegalMoves()
		moveIndex = moves.index(move)
		brains[Chessman.red].train(trainGame.chessmenOnBoard(), moves, moveIndex, result)

		trainGame.makeMove(move.fromPos, move.toPos)
		if i+1 < game.moveSize():
			move = game.moveAt(i+1)
			trainGame.makeMove(move.fromPos, move.toPos)
		i += 2
	end = time.time()
	print('train finished, cost time ', end-start)
	network.save()

def train():
	moveGen = MoveGenerator(game)
	brains[game.activeColor()].generateProbability(game.chessmenOnBoard(), moveGen.generateLegalMoves())
	move = brains[game.activeColor()].chooseByProbability()
	global training
	global noEatCnt
	if not move or noEatCnt > 100:
		training = False
		if not move:
			if game.activeColor() == Chessman.red:
				result = -1
			else:
				result = 1
			endGame(result)
		return
	if move.ateChessman:
		noEatCnt = 0
	else:
		noEatCnt += 1
	game.makeMove(move.fromPos, move.toPos)
	board.setChessmenOnBoard(game.chessmenOnBoard())
	board.refresh()
	if training:
		cv.after(1, train)

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

def onKey(event):
	code = event.keycode
	global training
	global noEatCnt
	if code == 27: # Esc
		if board.selectionSize() > 0:
			board.clearSelection()
			board.refresh()
		elif training:
			training = False
		else:
			rootWindow.quit()
	elif code == 37 or code == 38: # Left, Up
		game.undoMove()
		board.setChessmenOnBoard(game.chessmenOnBoard())
		board.refresh()
	elif code == 39 or code == 40: # Right, Down
		game.redoMove()
		board.setChessmenOnBoard(game.chessmenOnBoard())
		board.refresh()
	elif code == 13 and not training: # Enter
		training = True
		noEatCnt = 0
		cv.after(1, train)
	elif code == 82 and not training: # r
		reset()
		board.setChessmenOnBoard(game.chessmenOnBoard())
		board.refresh()
	elif code == 83 and not training: # s
		network.save()

rootWindow = tkinter.Tk()

cv = tkinter.Canvas(rootWindow)

reset()
board = Chessboard(cv)
board.setChessmenOnBoard(game.chessmenOnBoard())
rule = ChessRule()
network = Network()
brains = {
	Chessman.red: MoveProbability(network),
	Chessman.black: MoveProbability()
}

board.setMoveEventListener(onClick)
rootWindow.bind('<Key>', onKey)

miniW, miniH = board.minimumSize()
rootWindow.minsize(miniW, miniH)

rootWindow.title('中国象棋 - 妖刀')
setWindowSize(rootWindow, miniW, miniH+5)

cv.pack(fill=tkinter.BOTH, expand=1)
rootWindow.mainloop()
