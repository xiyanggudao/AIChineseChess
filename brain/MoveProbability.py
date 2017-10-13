import random

class MoveProbability:

	def __init__(self):
		pass

	def setChessmenOnBoard(self, chessmenOnBoard):
		pass

	def generateProbability(self, moves):
		probability = []
		if len(moves) == 1:
			probability.append(1.)
		elif len(moves) > 1:
			total = 0
			for i in range(len(moves)):
				probability.append(random.randint(1, 100))
				total += probability[i]
			for i in range(len(probability)):
				probability[i] /= total
		self.moves = moves
		self.probability = probability

	def probability(self):
		return self.probability

	def chooseByProbability(self):
		if len(self.moves) == 0:
			return None
		rand = random.uniform(0, 1)
		for i in range(len(self.probability)):
			if rand < self.probability[i]:
				return self.moves[i]
			rand -= self.probability[i]
		return self.moves[0]
