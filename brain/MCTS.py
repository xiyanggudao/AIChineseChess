import numpy as np
from chess.MoveGenerator import MoveGenerator
from chess.Chessgame import Chessgame
from chess.ChessData import Move
from chess.Chessman import Chessman

class MCTS:

	def __init__(self, brain, maxNodes):
		self.brain = brain
		maxEdges = maxNodes*128
		self.maxNodes = maxNodes
		self.maxEdges = maxEdges

		self.W = np.empty(maxEdges, np.float32)
		self.N = np.empty(maxEdges, np.int32)
		self.Q = np.empty(maxEdges, np.float32)
		self.P = np.empty(maxEdges, np.float32)
		self.linkTo = np.empty(maxEdges, np.int32)
		self.move = np.empty((maxEdges, 4), np.float32)
		self.IsEdgeUsed = np.empty(maxEdges, np.bool_)
		self.edgeUseCnt = 0
		self.edgeCurrent = 0

		self.nodesToEdge = np.empty((maxNodes, 128), np.int32)
		self.nodesToEdgeCnt = np.empty(maxNodes, np.int32)
		self.IsNodeUsed = np.empty(maxNodes, np.bool_)
		self.nodeBoard = [None for i in range(maxNodes)]
		self.nodeUseCnt = 0
		self.root = None
		self.nodeCurrent = 0

	def newEdge(self):
		assert self.edgeUseCnt < self.maxEdges
		while self.IsEdgeUsed[self.edgeCurrent]:
			self.edgeCurrent = (self.edgeCurrent + 1)%self.maxEdges
		self.edgeUseCnt += 1
		self.IsEdgeUsed[self.edgeCurrent] = True
		return self.edgeCurrent

	def newNode(self):
		assert self.nodeUseCnt < self.maxNodes
		while self.IsNodeUsed[self.nodeCurrent]:
			self.nodeCurrent = (self.nodeCurrent + 1)%self.maxNodes
		self.nodeUseCnt += 1
		self.IsNodeUsed[self.nodeCurrent] = True
		return self.nodeCurrent

	def releaseNode(self, node):
		assert self.IsNodeUsed[node]
		for i in range(self.nodesToEdgeCnt[node]):
			edge = self.nodesToEdge[self.root, i]
			self.releaseEdge(edge)
		self.nodeUseCnt -= 1
		self.IsNodeUsed[node] = False

	def releaseEdge(self, edge):
		assert self.IsEdgeUsed[edge]
		if self.linkTo[edge] != -1:
			self.releaseNode(self.linkTo[edge])
		self.edgeUseCnt -= 1
		self.IsEdgeUsed[edge] = False

	def createNode(self, game):
		moves = MoveGenerator(game).generateLegalMoves()
		newNode = self.newNode()
		self.nodeBoard[newNode] = game.ucciFen()
		self.nodesToEdgeCnt[newNode] = len(moves)
		if len(moves) < 1:
			return (-1, -1)
		p, v = self.brain.generate(game, moves)
		for i in range(len(moves)):
			newEdge = self.newEdge()
			self.nodesToEdge[newNode, i] = newEdge
			self.linkTo[newEdge] = -1
			self.move[newEdge, 0] = moves[i].fromPos[0]
			self.move[newEdge, 1] = moves[i].fromPos[1]
			self.move[newEdge, 2] = moves[i].toPos[0]
			self.move[newEdge, 3] = moves[i].toPos[1]

			self.W[newEdge] = 0
			self.N[newEdge] = 0
			self.Q[newEdge] = 0
			self.P[newEdge] = p[i]
		return (newNode, v)

	def clear(self):
		self.IsEdgeUsed.fill(False)
		self.edgeUseCnt = 0

		self.IsNodeUsed.fill(False)
		self.nodeUseCnt = 0

	def setRoot(self, game):
		self.clear()
		self.root, v = self.createNode(game)

	def moveRoot(self, edge):
		newRoot = None
		assert self.root != None
		for i in range(self.nodesToEdgeCnt[self.root]):
			e = self.nodesToEdge[self.root, i]
			if e == edge:
				assert newRoot == None
				assert self.linkTo[edge] != -1
				newRoot = self.linkTo[edge]
				self.linkTo[edge] = -1
		assert newRoot != None
		self.releaseNode(self.root)
		self.root = newRoot

	def PUCT(self, q, p, sqrtSumN, n):
		return q + p*sqrtSumN/(1+n)

	def select(self, node):
		if self.nodesToEdgeCnt[node] < 1:
			return -1
		sumN = 0
		for i in range(self.nodesToEdgeCnt[node]):
			edge = self.nodesToEdge[node, i]
			sumN += self.N[edge]
		sqrtSumN = sumN ** 0.5
		selected = self.nodesToEdge[node, 0]
		max = self.PUCT(self.Q[selected], self.P[selected], sqrtSumN, self.N[selected])
		for i in range(1, self.nodesToEdgeCnt[node]):
			edge = self.nodesToEdge[node, i]
			puct = self.PUCT(self.Q[edge], self.P[edge], sqrtSumN, self.N[edge])
			if puct > max:
				selected = edge
				max = puct
		return selected

	def backup(self, edge, value):
		self.N[edge] += 1
		self.W[edge] += value
		self.Q[edge] = self.W[edge]/self.N[edge]

	def expandNode(self, node):
		edge = self.select(node)
		if edge == -1:
			return -1
		if self.linkTo[edge] == -1:
			game = Chessgame()
			game.setWithUcciFen(self.nodeBoard[node])
			fx = self.move[edge, 0]
			fy = self.move[edge, 1]
			tx = self.move[edge, 2]
			ty = self.move[edge, 3]
			game.makeMove((fx, fy), (tx, ty))
			self.linkTo[edge], v = self.createNode(game)
			ret = -v
		else:
			ret = -self.expandNode(self.linkTo[edge])
		self.backup(edge, ret)
		return ret

	def expand(self):
		self.expandNode(self.root)

	def pi(self, n, sumN):
		return n/sumN

	def selectToMove(self, node):
		if self.nodesToEdgeCnt[node] < 1:
			return -1
		sumN = 0
		for i in range(self.nodesToEdgeCnt[node]):
			edge = self.nodesToEdge[node, i]
			sumN += self.N[edge]
		selected = self.nodesToEdge[node, 0]
		max = self.pi(self.N[selected], sumN)
		for i in range(1, self.nodesToEdgeCnt[node]):
			edge = self.nodesToEdge[node, i]
			pi = self.pi(self.N[edge], sumN)
			if pi > max:
				selected = edge
				max = pi
		return selected

	def play(self):
		edge = self.selectToMove(self.root)
		move = None
		if edge != -1:
			self.moveRoot(edge)
			fx = self.move[edge, 0]
			fy = self.move[edge, 1]
			tx = self.move[edge, 2]
			ty = self.move[edge, 3]
			move = Move((fx, fy), (tx, ty), Chessman.invalid(), Chessman.invalid())
		return move
