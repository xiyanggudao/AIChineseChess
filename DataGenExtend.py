from chess.Chessgame import Chessgame
from brain.MoveProbability import MoveProbability
from chess.MoveGenerator import MoveGenerator
from brain.UcciBrain import UcciBrain
import time
import traceback

brains = [
	'./ucci/bhws/Binghewusi.exe',
	'./ucci/hice/HICE.EXE',
	'./ucci/swallow/swallow.exe',
	'./ucci/xqcyclone/cyclone.exe',
	'./ucci/xqspirit/XQSPIRIT.EXE',
	'./ucci/xqwizard/ELEEYE.EXE',
	'./ucci/yssy/YSSY.EXE',
]

def appendFile(path, data):
	file = open(path, 'a')
	for str in data:
		file.write(str)
	file.close()

def play(fen):
	global brain
	game = Chessgame()
	moveGen = MoveGenerator(game)
	playingBrain = MoveProbability(brain)
	game.setWithUcciFen(fen)

	brain.setStartpos('fen '+fen)
	playingBrain.generateProbability(game, moveGen.generateLegalMoves())
	move = playingBrain.chooseByProbability()

	saveLine = fen+':'+move.ucciStr()+'\n'
	appendFile('data/train.txt', saveLine)

brain = None
def reset():
	global brain
	if brain != None:
		del brain
		brain = None
	brain = UcciBrain(brains[6])
	brain.setDepth(12)

file = open('data/merged.txt', 'r')
index = 0
reset()
while True:
	if index % 200 == 0:
		reset()
	line = file.readline()
	if not line:
		break
	end = line.index(':')
	fen = line[0: end]
	playStart = time.time()
	while True:
		try:
			play(fen)
		except:
			f = open("log.txt", 'a')
			traceback.print_exc(file=f)
			f.close()
			reset()
		else:
			break
	playEnd = time.time()
	print(index, 'time', round(playEnd - playStart, 2))
	index += 1
file.close()
