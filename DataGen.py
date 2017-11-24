from chess.Chessgame import Chessgame
from brain.MoveProbability import MoveProbability
from chess.MoveGenerator import MoveGenerator
from brain.UcciBrain import UcciBrain
import random
import time
import traceback

brains = [
	'./ucci/bhws/Binghewusi.exe',
	'./ucci/blcx/BLCX056.EXE',
	'./ucci/eychessu/EYCHESSU.EXE',
	'./ucci/hice/HICE.EXE',
	'./ucci/jupiter/JUPITER.EXE',
	'./ucci/king/King.exe',
	'./ucci/nymphchess/EYE.EXE',
	'./ucci/qstar/qst.exe',
	'./ucci/sixteeners/sixteen.exe',
	'./ucci/swallow/swallow.exe',
	'./ucci/tht/THT.EXE',
	'./ucci/tlxj/TLXJ.EXE',
	'./ucci/xqcyclone/cyclone.exe',
	'./ucci/xqspirit/XQSPIRIT.EXE',
	'./ucci/xqwizard/ELEEYE.EXE',
	'./ucci/yssy/YSSY.EXE',
]

names = [
	'bhws',
	'blcx',
	'eychessu',
	'hice',
	'jupiter',
	'king',
	'nymphchess',
	'qstar',
	'sixteeners',
	'swallow',
	'tht',
	'tlxj',
	'xqcyclone',
	'xqspirit',
	'xqwizard',
	'yssy',
]

def play(red, black):
	noEatCnt = 0
	game = Chessgame()
	moveGen = MoveGenerator(game)
	playingBrains = [MoveProbability(red), MoveProbability(black)]
	currentMan = 0
	while True:
		playingBrains[currentMan].generateProbability(game, moveGen.generateLegalMoves())
		move = playingBrains[currentMan].chooseByProbability()
		if not move or noEatCnt >= 50:
			if move:
				game.isDraw = True
			return game
		if move.ateChessman:
			noEatCnt = 0
		else:
			noEatCnt += 1
		game.makeMove(move.fromPos, move.toPos)
		currentMan ^= 1

def appendFile(path, data):
	file = open(path, 'a')
	for str in data:
		file.write(str)
	file.close()

def save(game):
	trainGame = Chessgame()
	if (game.moveSize() & 1):
		index = 0
	else:
		move = game.moveAt(0)
		trainGame.makeMove(move.fromPos, move.toPos)
		index = 1
	saveLines = []
	while index < game.moveSize():
		move = game.moveAt(index)
		saveLines.append(trainGame.ucciFen())
		saveLines.append(':')
		saveLines.append(move.ucciStr())
		saveLines.append('\n')

		trainGame.makeMove(move.fromPos, move.toPos)
		index += 1
		if index < game.moveSize():
			move = game.moveAt(index)
			trainGame.makeMove(move.fromPos, move.toPos)
			index += 1

	appendFile('data/train.txt', saveLines)

assert len(brains) == len(names)
for i in range(10000):
	redIndex = random.randint(0, len(brains) - 1)
	blackIndex = random.randint(0, len(brains) - 1)

	redDepth = random.randint(5, 11)
	blackDepth = random.randint(5, 11)

	try:
		brainStart = time.time()
		red = UcciBrain(brains[redIndex])
		black = UcciBrain(brains[blackIndex])
		brainEnd = time.time()
		red.setDepth(redDepth)
		black.setDepth(blackDepth)
		print(names[redIndex], redDepth, 'vs', names[blackIndex], blackDepth)
		playStart = time.time()
		game = play(red, black)
		playEnd = time.time()
		if not hasattr(game, 'isDraw') and game.moveSize() > 0:
			print(
				'save', i, 'brain time', round(brainEnd - brainStart, 2),
				'play time', round(playEnd - playStart, 2)
			)
			save(game)
	except:
		f = open("log.txt", 'a')
		traceback.print_exc(file=f)
		f.close()
	finally:
		del red
		del black
