import random
from chess.Chessman import Chessman

class MoveProbability:

	def __init__(self, brain):
		self.__brain = brain

	def __generate(self, game, moves):
		self.__probability = self.__brain.generate(game, moves)

		totalProbability = sum(self.__probability)
		assert abs(totalProbability - 1) < 0.000001
		#print('totalProbability ', totalProbability)

	def generateProbability(self, game, moves):
		if len(moves) < 1:
			self.__probability = []
		elif len(moves) == 1:
			self.__probability = [1.]
		else:
			assert self.__brain
			self.__generate(game, moves)
		self.__moves = moves

	def probability(self):
		return self.__probability

	def moves(self):
		return self.__moves

	def chooseByProbability(self):
		if len(self.__moves) == 0:
			return None
		rand = random.uniform(0, 1)
		for i in range(len(self.__probability)):
			if rand < self.__probability[i]:
				return self.__moves[i]
			rand -= self.__probability[i]
		print('rand choose failed ', rand)
		return self.__moves[0]

	def chooseBest(self):
		pass

	def chooseAcceptable(self):
		pass
