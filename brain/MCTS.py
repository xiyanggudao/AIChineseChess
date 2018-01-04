import numpy as np
from chess.MoveGenerator import MoveGenerator

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

	def createNode(self, game, moves):
		P, v = self.brain.generate(game, moves)
		newNode = self.newNode()
		self.nodesToEdgeCnt[newNode] = len(moves)
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
			self.P[newEdge] = P[i]
		return newNode

	def clear(self):
		self.IsEdgeUsed.fill(False)
		self.edgeUseCnt = 0

		self.IsNodeUsed.fill(False)
		self.nodeUseCnt = 0

	def setRoot(self, game):
		self.clear()
		moves = MoveGenerator(game).generateLegalMoves()
		self.root = self.createNode(game, moves)

	def moveRoot(self, move):
		newRoot = None
		assert self.root != None
		for i in range(self.nodesToEdgeCnt[self.root]):
			edge = self.nodesToEdge[self.root, i]
			if self.move[edge, 0] == move.fromPos[0] \
				and self.move[edge, 1] == move.fromPos[1] \
				and self.move[edge, 2] == move.toPos[0] \
				and self.move[edge, 3] == move.toPos[1]:
				assert newRoot == None
				newRoot = self.linkTo[edge]
				self.linkTo[edge] = -1
		assert newRoot != None
		self.releaseNode(self.root)
		self.root = newRoot

	def expandNode(self, node):
		pass

	def expand(self):
		self.expandNode(self.root)
