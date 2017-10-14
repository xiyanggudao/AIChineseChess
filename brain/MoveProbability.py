import random
from chess.Chessman import Chessman

class MoveProbability:

	def __init__(self, brain=None):
		self.__brain = brain

	def __randomGenerate(self, moves):
		probability = []
		total = 0
		for i in range(len(moves)):
			probability.append(random.randint(1, 100))
			total += probability[i]
		for i in range(len(probability)):
			probability[i] /= total
		self.__probability = probability

	def __generate(self, chessmenOnBoard, moves):
		# 14种棋子
		boardFeature = [None for i in range(14)]

		boardFeature[0] = [0 for i in range(9)]
		boardFeature[1] = [0 for i in range(5)]
		boardFeature[2] = [0 for i in range(7)]
		boardFeature[3] = [0 for i in range(90)]
		boardFeature[4] = [0 for i in range(90)]
		boardFeature[5] = [0 for i in range(90)]
		boardFeature[6] = [0 for i in range(55)]

		boardFeature[7] = [0 for i in range(9)]
		boardFeature[8] = [0 for i in range(5)]
		boardFeature[9] = [0 for i in range(7)]
		boardFeature[10] = [0 for i in range(90)]
		boardFeature[11] = [0 for i in range(90)]
		boardFeature[12] = [0 for i in range(90)]
		boardFeature[13] = [0 for i in range(55)]

		active = Chessman.color(moves[0].moveChessman)
		for piece in chessmenOnBoard:
			if piece.color == active:
				offset = 0
			else:
				offset = 7
			if piece.color == Chessman.red:
				x, y = piece.position
			elif piece.color == Chessman.black:
				x, y = 9-piece.x, 10-piece.y
			if piece.type == Chessman.king:
				i = 0
			elif piece.type == Chessman.mandarin:
				i = 1
			elif piece.type == Chessman.elephant:
				i = 2
			elif piece.type == Chessman.knight:
				i = 3
			elif piece.type == Chessman.rook:
				i = 4
			elif piece.type == Chessman.cannon:
				i = 5
			elif piece.type == Chessman.pawn:
				i = 6

	def generateProbability(self, chessmenOnBoard, moves):
		if len(moves) < 1:
			self.__probability = []
		elif len(moves) == 1:
			self.__probability = [1.]
		elif self.__brain:
			self.__generate(chessmenOnBoard, moves)
		else:
			self.__randomGenerate(moves)
		self.__moves = moves

	def probability(self):
		return self.__probability

	def chooseByProbability(self):
		if len(self.__moves) == 0:
			return None
		rand = random.uniform(0, 1)
		for i in range(len(self.__probability)):
			if rand < self.__probability[i]:
				return self.__moves[i]
			rand -= self.__probability[i]
		return self.__moves[0]

	def chooseBest(self):
		pass

	def chooseAcceptable(self):
		pass
