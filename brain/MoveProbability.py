import random
from chess.Chessman import Chessman

class MoveProbability:

	def __init__(self, brain=None):
		self.__brain = brain

	def __randomGenerate(self, moves):
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
		self.__probability = probability

	def chessmanFeatureId(self, type, color, position, active):
		if color == active:
			offset = 0
		else:
			offset = 9+5+7+90*3+55

		if color == Chessman.red:
			x, y = position
		else:
			assert color == Chessman.black
			x, y = 8 - position[0], 9 - position[1]

		if type == Chessman.king:
			id = y * 3 + x - 3
		elif type == Chessman.mandarin:
			offset += 9
			id = (x + y - 3) // 2 + y
		elif type == Chessman.elephant:
			offset += 9+5
			id = (x + y) // 4 + y
		elif type == Chessman.knight:
			offset += 9+5+7
			id = y * 9 + x
		elif type == Chessman.rook:
			offset += 9+5+7+90
			id = y * 9 + x
		elif type == Chessman.cannon:
			offset += 9+5+7+90*2
			id = y * 9 + x
		elif type == Chessman.pawn:
			offset += 9+5+7+90*3
			if y < 5:
				id = (y - 3) * 5 + x // 2
			else:
				id = (y - 5) * 9 + x + 10
		else:
			assert False

		return offset+id

	def moveFeatureId(self, type, color, fromPos, toPos, active):
		assert color == active
		if color == Chessman.red:
			fx, fy = fromPos
			tx, ty = toPos
		else:
			assert color == Chessman.black
			fx, fy = 8 - fromPos[0], 9 - fromPos[1]
			tx, ty = 8 - toPos[0], 9 - toPos[1]
		dx, dy = tx-fx, ty-fy

		if type == Chessman.king:
			offset = 0
			posId = fy*3 + fx-3
			ids = [0, 1, None, 2, 3]
			moveId = ids[2*dx + dy + 2]
			moveCnt = 4
		elif type == Chessman.mandarin:
			offset = 9*4
			posId = [0,None,1,2,3,None,4][2*(fx-3) + fy]
			moveId = dx + (dy+3)//2
			moveCnt = 4
		elif type == Chessman.elephant:
			offset = 9*4+5*4
			posId = [0,1,None,2,3,4,None,5,6][fx+fy//2-1]
			moveId = dx//2 + (dy//2 + 3) // 2
			moveCnt = 4
		elif type == Chessman.knight:
			offset = 9*4+5*4+7*4
			posId = fy*9+fx
			ids = [
				0, None, 1, 2, None, None, None, 3,
				None, None, None,
				4, None, None, None, 5, 6, None, 7
			]
			moveId = ids[4*dx+dy+9]
			moveCnt = 8
		elif type == Chessman.rook:
			offset = 9*4+5*4+7*4+90*8
			posId = fy*9 + fx
			if dy == 0:
				moveId = tx
			else:
				assert dx == 0
				moveId = ty+9
			moveCnt = 18
		elif type == Chessman.cannon:
			offset = 9*4+5*4+7*4+90*8+90*18
			posId = fy*9 + fx
			if dy == 0:
				moveId = tx
			else:
				assert dx == 0
				moveId = ty+9
			moveCnt = 18
		elif type == Chessman.pawn:
			offset = 9*4+5*4+7*4+90*8+90*18*2
			if fx < 5:
				posId = (fy-3)*5+fx//2
			else:
				posId = (fy-5)*9+fx+10
			moveId = dx + 1
			moveCnt = 3
		else:
			assert False

		assert posId >= 0
		assert moveId >= 0
		return offset + posId*moveCnt + moveId

	def __inputFeature(self, chessmenOnBoard, moves):
		active = Chessman.color(moves[0].moveChessman)

		boardFeature = [0 for i in range((9+5+7+90*3+55)*2)]
		for piece in chessmenOnBoard:
			id = self.chessmanFeatureId(piece.type, piece.color, piece.position, active)
			boardFeature[id] = 1

		moveFeature = [0 for i in range(9*4+5*4+7*4+90*8+90*18*2+55*3)]
		for move in moves:
			type = Chessman.type(move.moveChessman)
			color = Chessman.color(move.moveChessman)
			id = self.moveFeatureId(type, color, move.fromPos, move.toPos, active)
			assert moveFeature[id] == 0
			moveFeature[id] = 1

		return (boardFeature, moveFeature)

	def __generate(self, chessmenOnBoard, moves):
		boardFeature, moveFeature = self.__inputFeature(chessmenOnBoard, moves)

		moveProbability = self.__brain.generate(boardFeature, moveFeature)
		assert len(moveFeature) == len(moveProbability)

		self.__probability = []
		active = Chessman.color(moves[0].moveChessman)
		for move in moves:
			type = Chessman.type(move.moveChessman)
			color = Chessman.color(move.moveChessman)
			id = self.moveFeatureId(type, color, move.fromPos, move.toPos, active)
			self.__probability.append(moveProbability[id])
		totalProbability = sum(self.__probability)
		totalProbability2 = sum(moveProbability)
		assert abs(totalProbability - totalProbability2) < 0.000001
		assert abs(totalProbability - 1) < 0.000001
		print('totalProbability ', totalProbability)

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
		print('rand choose failed ', rand)
		return self.__moves[0]

	def chooseBest(self):
		pass

	def chooseAcceptable(self):
		pass

	def train(self, chessmenOnBoard, moves, moveIndex, result):
		# 结果：负、和、胜
		#assert result == -1 or result == 0 or result == 1
		if len(moves) > 1 and self.__brain and result != 0:
			boardFeature, moveFeature = self.__inputFeature(chessmenOnBoard, moves)
			move = moves[moveIndex]
			type = Chessman.type(move.moveChessman)
			color = Chessman.color(move.moveChessman)
			moveId = self.moveFeatureId(type, color, move.fromPos, move.toPos, color)
			self.__brain.train(boardFeature, moveFeature, moveId, result)
