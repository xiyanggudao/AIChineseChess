from chess.Chessgame import Chessgame
from chess.MoveGenerator import MoveGenerator
from chess.Chessman import Chessman
import brain.NetworkFeature as nf
import random

class DataSet:

	def __init__(self, filePath):
		self.fens = []
		self.moves = []
		file = open(filePath, 'r')
		while True:
			line = file.readline()
			if not line:
				break
			sep = line.index(':')
			fen = line[0: sep]
			move = line[sep+1: sep+5]
			size = len(self.fens)
			if size > 0 and self.fens[size-1] == fen:
				self.moves[size-1].append(move)
			else:
				self.fens.append(fen)
				self.moves.append([move])
		file.close()

	def nextBatch(self, size):
		game = Chessgame()
		moveGen = MoveGenerator(game)
		boards = []
		moves = []
		predictions = []

		for i in range(size):
			j = random.randint(0, len(self.fens)-1)
			game.setWithUcciFen(self.fens[j])
			bf, mf = nf.inputFeature(game.chessmenOnBoard(), moveGen.generateLegalMoves())
			predic = [0 for i in range(len(mf))]
			for moveStr in self.moves[j]:
				fx = ord(moveStr[0]) - ord('a')
				fy = ord(moveStr[1]) - ord('0')
				tx = ord(moveStr[2]) - ord('a')
				ty = ord(moveStr[3]) - ord('0')
				chessman = game.chessmanAt((fx, fy))
				type = Chessman.type(chessman)
				color = Chessman.color(chessman)
				id = nf.moveFeatureId(type, color, (fx, fy), (tx, ty), game.activeColor())
				assert mf[id] == 1
				predic[id] = 1./len(self.moves[j])
			boards.append(bf)
			moves.append(mf)
			predictions.append(predic)

		return (boards, moves, predictions)