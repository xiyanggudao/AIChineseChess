import random

class RandomBrain:

	def __init__(self):
		pass

	def generate(self, chessmenOnBoard, moves):
		probability = []
		total = 0
		for i in range(len(moves)):
			probability.append(random.randint(1, 100))
			total += probability[i]
		for i in range(len(probability)):
			probability[i] /= total

		return probability

	def train(self, chessmenOnBoard, moves, moveIndex, reward):
		pass


class RandomEatBrain:

	def __init__(self):
		pass

	def generate(self, chessmenOnBoard, moves):
		probability = []
		total = 0
		for i in range(len(moves)):
			if moves[i].ateChessman:
				min = 80
				max = 100
			else:
				min = 1
				max = 20
			probability.append(random.randint(min, max))
			total += probability[i]
		for i in range(len(probability)):
			probability[i] /= total

		return probability

	def train(self, chessmenOnBoard, moves, moveIndex, reward):
		pass
