from chess.Chessgame import Chessgame
from chess.MoveGenerator import MoveGenerator
from chess.Chessman import Chessman
from chess.ChessData import Move
import brain.NetworkFeature as nf
import random
import gzip
import os
import numpy as np

def writeInt(file, val):
	s = str(val)
	file.write(s + '\n')

def readint(file):
	s = file.readline()
	if not s:
		return None
	return int(s)

class DataId:

	def __init__(self):
		pass

	def __moveId(self, move):
		active = Chessman.color(move.moveChessman)
		type = Chessman.type(move.moveChessman)
		color = Chessman.color(move.moveChessman)
		id = nf.moveFeatureId(type, color, move.fromPos, move.toPos, active)
		return id

	def setBoard(self, chessmenOnBoard, moves):
		self.boardIds = []
		self.moveIds = []
		self.predicIds = []
		active = Chessman.color(moves[0].moveChessman)
		for piece in chessmenOnBoard:
			id = nf.chessmanFeatureId(piece.type, piece.color, piece.position, active)
			self.boardIds.append(id)
		for move in moves:
			id = self.__moveId(move)
			self.moveIds.append(id)

	def addPredicMove(self, move):
		id = self.__moveId(move)
		self.predicIds.append(id)

	def inputFeature(self, boardFeature, moveFeature, predic):
		for id in self.boardIds:
			assert boardFeature[id] == 0
			boardFeature[id] = 1

		for id in self.moveIds:
			assert moveFeature[id] == 0
			moveFeature[id] = 1

		for id in self.predicIds:
			assert moveFeature[id] == 1
			assert predic[id] == 0
			predic[id] = 1. / len(self.predicIds)

		return (boardFeature, moveFeature, predic)

	def serialize(self, file):
		writeInt(file, len(self.boardIds))
		for val in self.boardIds:
			writeInt(file, val)
		writeInt(file, len(self.moveIds))
		for val in self.moveIds:
			writeInt(file, val)
		writeInt(file, len(self.predicIds))
		for val in self.predicIds:
			writeInt(file, val)

	@staticmethod
	def unserialize(file):
		size = readint(file)
		if size == None:
			return None
		ret = DataId()
		ret.boardIds = []
		for i in range(size):
			val = readint(file)
			ret.boardIds.append(val)
		size = readint(file)
		ret.moveIds = []
		for i in range(size):
			val = readint(file)
			ret.moveIds.append(val)
		size = readint(file)
		ret.predicIds = []
		for i in range(size):
			val = readint(file)
			ret.predicIds.append(val)
		return ret

class DataSet:

	def __init__(self, filePath):
		self.dataIds = []
		tmpPath = filePath+'.tmp'
		if os.path.exists(tmpPath):
			self.__loadFromTmp(tmpPath)
		else:
			self.__loadFromGz(filePath)
			self.__saveTmp(tmpPath)

	def __loadFromTmp(self, filePath):
		file = open(filePath, 'r')
		while True:
			dataId = DataId.unserialize(file)
			if dataId == None:
				break
			self.dataIds.append(dataId)
		file.close()

	def __saveTmp(self, filePath):
		file = open(filePath, 'w')
		for dataId in self.dataIds:
			dataId.serialize(file)
		file.close()

	def __loadFromGz(self, filePath):
		file = gzip.open(filePath, 'r')
		lastFen = ''
		while True:
			line = file.readline().decode()
			if not line:
				break
			sep = line.index(':')
			fen = line[0: sep]
			moveStr = line[sep+1: sep+5]
			if len(self.dataIds) > 0 and lastFen == fen:
				game, moves, predicMove = self.__getGameAndMove(fen, moveStr)
				self.dataIds[-1].addPredicMove(predicMove)
			else:
				lastFen = fen
				game, moves, predicMove = self.__getGameAndMove(fen, moveStr)
				self.dataIds.append(DataId())
				self.dataIds[-1].setBoard(game.chessmenOnBoard(), moves)
				self.dataIds[-1].addPredicMove(predicMove)
		file.close()

	def __getGameAndMove(self, fen, moveStr):
		game = Chessgame()
		game.setWithUcciFen(fen)
		moveGen = MoveGenerator(game)

		fx = ord(moveStr[0]) - ord('a')
		fy = ord(moveStr[1]) - ord('0')
		tx = ord(moveStr[2]) - ord('a')
		ty = ord(moveStr[3]) - ord('0')

		predicMove = Move(
			(fx, fy), (tx, ty),
			game.chessmanAt((fx, fy)), game.chessmanAt((tx, ty))
		)

		moves = moveGen.generateLegalMoves()
		assert predicMove in moves

		return (game, moves, predicMove)

	def nextBatch(self, size):
		boards = np.zeros((size, 692), dtype=np.float32)
		moves = np.zeros((size, 4209), dtype=np.float32)
		predictions = np.zeros((size, 4209), dtype=np.float32)

		indexes = random.sample(range(len(self.dataIds)), size)
		for i in range(len(indexes)):
			self.dataIds[indexes[i]].inputFeature(boards[i], moves[i], predictions[i])

		return (boards, moves, predictions)