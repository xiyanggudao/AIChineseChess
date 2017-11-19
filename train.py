from chess.Chessgame import Chessgame
from brain.MoveProbability import MoveProbability
from chess.MoveGenerator import MoveGenerator
from brain.Network import Network
from brain.ResidualNetwork2 import ResidualNetwork
from brain.UcciBrain import UcciBrain
import time

class Trainer:
	def __init__(self, startTrainCnt, endTrainCnt, saveTurn):
		self.startTrainCnt = startTrainCnt
		self.endTrainCnt = endTrainCnt
		self.saveTurn = saveTurn
		self.noEatCnt = 0
		self.loseCnt = 0
		self.drawCnt = 0
		self.winCnt = 0
		self.maxNoEatSteps = 50

	def networkSavePath(self, trainTurn):
		basePath = './model/'
		date = '20171029-'
		suffix = '%05d' % trainTurn
		name = '/model.ckpt'
		return basePath + date + suffix + name

	def play(self, brains, currentMan):
		self.noEatCnt = 0
		game = Chessgame()
		moveGen = MoveGenerator(game)
		while True:
			brains[currentMan].generateProbability(game, moveGen.generateLegalMoves())
			move = brains[currentMan].chooseByProbability()
			if not move or self.noEatCnt >= self.maxNoEatSteps:
				return game
			if move.ateChessman:
				self.noEatCnt = 0
			else:
				self.noEatCnt += 1
			game.makeMove(move.fromPos, move.toPos)
			currentMan ^= 1

	def update(self, network, game, winColor):
		print('train started')
		trainStart = time.time()
		trainGame = Chessgame()
		moveGenTrain = MoveGenerator(trainGame)
		i = 0
		while i < game.moveSize():
			move = game.moveAt(i)
			moves = moveGenTrain.generateLegalMoves()
			moveIndex = moves.index(move)
			if trainGame.activeColor() == winColor:
				trainResult = 1
			else:
				trainResult = -1
			if len(moves) > 1:
				network.addTrainData(trainGame.chessmenOnBoard(), moves, moveIndex, trainResult)
			trainGame.makeMove(move.fromPos, move.toPos)
			i += 1
		network.train()
		trainEnd = time.time()
		print('train finished, cost time', round(trainEnd - trainStart, 2))

	def logGame(self, winMan, time, steps):
		print('game result', winMan, ', time', round(time, 2), ', move step', steps)
		total = self.loseCnt + self.drawCnt + self.winCnt
		print('total', total, ', loseCnt', self.loseCnt, ', drawCnt', self.drawCnt, ', winCnt', self.winCnt)

	def train(self):
		network = ResidualNetwork(self.networkSavePath(self.startTrainCnt))
		ucci = UcciBrain('./ucci/xqwizard/ELEEYE.EXE')
		brains = [MoveProbability(network), MoveProbability(ucci)]
		for i in range(self.startTrainCnt, self.endTrainCnt):
			startMan = i & 1
			gameStart = time.time()
			game = self.play(brains, startMan)
			gameEnd = time.time()

			if self.noEatCnt < self.maxNoEatSteps:
				if (game.moveSize() & 1):
					winColor = 0
				else:
					winColor = 1
				if winColor == startMan:
					self.winCnt += 1
				else:
					self.loseCnt += 1
			else:
				winColor = None
				self.drawCnt += 1

			self.logGame(winColor, gameEnd-gameStart, game.moveSize())

			if winColor != None:
				self.update(network, game, winColor)

			if (i+1)%self.saveTurn == 0:
				network.save(self.networkSavePath(i+1))
				# 定期重启ucci进程，不然会挂
				brains[1] = MoveProbability(UcciBrain('./ucci/xqwizard/ELEEYE.EXE'))

trainer = Trainer(0, 30000, 1000)
trainer.train()
