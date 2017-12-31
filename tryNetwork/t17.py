import time
import sys
sys.path.append("..")
from chess.Chessgame import Chessgame
from chess.MoveGenerator import MoveGenerator
import gzip

timeStart = time.time()
file = gzip.open('../data/test.gz', 'r')
fens = []
while True:
	line = file.readline().decode()
	if not line:
		break
	sep = line.index(':')
	fens.append(line[0: sep])
file.close()
timeEnd = time.time()
print('read data time', round(timeEnd - timeStart, 2))

timeStart = time.time()
games = []
for fen in fens:
	game = Chessgame()
	games.append(game)
timeEnd = time.time()
print('Chessgame time', round(timeEnd - timeStart, 2))

timeStart = time.time()
for i in range(len(fens)):
	games[i].setWithUcciFen(fens[i])
timeEnd = time.time()
print('setWithUcciFen time', round(timeEnd - timeStart, 2))

timeStart = time.time()
gens = []
for game in games:
	gens.append(MoveGenerator(game))
timeEnd = time.time()
print('MoveGenerator time', round(timeEnd - timeStart, 2))

timeStart = time.time()
for gen in gens:
	gen.generateLegalMoves()
timeEnd = time.time()
print('generateLegalMoves time', round(timeEnd - timeStart, 2))
