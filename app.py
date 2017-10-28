import tkinter
from gui.Chessboard import Chessboard
from chess.Chessgame import Chessgame
from chess.ChessData import Move
from chess.ChessRule import ChessRule
from chess.Chessman import Chessman
from brain.MoveProbability import MoveProbability
from chess.MoveGenerator import MoveGenerator
from brain.Network import Network
import brain.RandomBrain as rb
import time

def setWindowSize(window, width, height):
	geometry = '%dx%d' % (width, height)
	window.geometry(geometry)

def reset():
	global training
	global noEatCnt
	global game
	global moveGen
	global trainCnt
	global loseCnt
	global drawCnt
	global winCnt
	training = False
	noEatCnt = 0
	game = Chessgame()
	moveGen = MoveGenerator(game)

	trainCnt = 800
	loseCnt = 0
	drawCnt = 0
	winCnt = 0

def endGame(result):
	global game
	print('train started')
	trainStart = time.time()
	i = 0
	trainGame = Chessgame()
	moveGenTrain = MoveGenerator(trainGame)
	while i < game.moveSize():
		move = game.moveAt(i)
		moves = moveGenTrain.generateLegalMoves()
		moveIndex = moves.index(move)
		if trainGame.activeColor() == trainColor:
			trainResult = result
		else:
			trainResult = -result
		brains[trainColor].addTrainData(trainGame.chessmenOnBoard(), moves, moveIndex, trainResult)

		trainGame.makeMove(move.fromPos, move.toPos)
		i += 1
	brains[trainColor].train()
	trainEnd = time.time()
	print('train finished, cost time', round(trainEnd-trainStart, 2))
	network.save()

def swapTrainColor():
	global trainColor
	nextColor = Chessman.oppositeColor(trainColor)
	brainTmp = brains[nextColor]
	brains[nextColor] = brains[trainColor]
	brains[trainColor] = brainTmp
	trainColor = nextColor

def train():
	global trainCnt
	global loseCnt
	global drawCnt
	global winCnt
	global game
	global moveGen
	global gameStart
	global gameEnd
	brains[game.activeColor()].generateProbability(game.chessmenOnBoard(), moveGen.generateLegalMoves())
	move = brains[game.activeColor()].chooseByProbability()
	global training
	global noEatCnt
	if not move or noEatCnt > 100:
		training = False
		trainCnt -= 1
		if not move:
			if game.activeColor() == trainColor:
				result = -1
				loseCnt += 1
			else:
				result = 1
				winCnt += 1
		else:
			result = 0
			drawCnt += 1

		gameEnd = time.time()
		print('game result', result, ', time', round(gameEnd-gameStart, 2), ', move step', game.moveSize())
		print('total', loseCnt+drawCnt+winCnt, ', loseCnt', loseCnt, ', drawCnt', drawCnt, ', winCnt', winCnt)

		if result != 0:
			endGame(result)
		if trainCnt > 0:
			game = Chessgame()
			moveGen = MoveGenerator(game)
			#board.setChessmenOnBoard(game.chessmenOnBoard())
			#board.refresh()

			training = True
			noEatCnt = 0

			swapTrainColor()

			gameStart = time.time()
			cv.after(1000, train)
		return
	if move.ateChessman:
		noEatCnt = 0
	else:
		noEatCnt += 1
	game.makeMove(move.fromPos, move.toPos)
	#board.setChessmenOnBoard(game.chessmenOnBoard())
	#board.refresh()
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
	global gameStart
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
		gameStart = time.time()
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
	Chessman.black: MoveProbability(rb.RandomEatBrain())
}
trainColor = Chessman.red

board.setMoveEventListener(onClick)
rootWindow.bind('<Key>', onKey)

miniW, miniH = board.minimumSize()
rootWindow.minsize(miniW, miniH)

rootWindow.title('中国象棋 - 妖刀')
setWindowSize(rootWindow, miniW, miniH+5)

cv.pack(fill=tkinter.BOTH, expand=1)
rootWindow.mainloop()
