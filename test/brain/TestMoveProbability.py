from brain.MoveProbability import MoveProbability
from chess.Chessman import Chessman
import unittest

class TestMoveProbability(unittest.TestCase):

	def redKingPositions(self):
		ret = []
		for x in range(3, 6):
			for y in range(0, 3):
				ret.append((x, y))
		return ret

	def blackKingPositions(self):
		ret = []
		for x in range(3, 6):
			for y in range(7, 10):
				ret.append((x, y))
		return ret

	def redMandarinPositions(self):
		return [(3, 0), (5, 0), (4, 1), (3, 2), (5, 2)]

	def blackMandarinPositions(self):
		return [(3, 7), (5, 7), (4, 8), (3, 9), (5, 9)]

	def redElephantPositions(self):
		return [(2, 0), (6, 0), (0, 2), (4, 2), (8, 2), (2, 4), (6, 4)]

	def blackElephantPositions(self):
		return [(2, 5), (6, 5), (0, 7), (4, 7), (8, 7), (2, 9), (6, 9)]

	def redPawnPositions(self):
		ret = [(0, 3), (2, 3), (4, 3), (6, 3), (8, 3), (0, 4), (2, 4), (4, 4), (6, 4), (8, 4)]
		for x in range(0, 9):
			for y in range(5, 10):
				ret.append((x, y))
		return ret

	def blackPawnPositions(self):
		ret = [(0, 5), (2, 5), (4, 5), (6, 5), (8, 5), (0, 6), (2, 6), (4, 6), (6, 6), (8, 6)]
		for x in range(0, 9):
			for y in range(0, 5):
				ret.append((x, y))
		return ret

	def allPositions(self):
		ret = []
		for x in range(0, 9):
			for y in range(0, 10):
				ret.append((x, y))
		return ret

	def testKingFeatureIdRedActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.redKingPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.king, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(0, 9))
			idSet.add(id)
		self.assertEqual(len(idSet), 9)

		positions = self.blackKingPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.king, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(346, 355))
			idSet.add(id)
		self.assertEqual(len(idSet), 18)

	def testKingFeatureIdBlackActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.redKingPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.king, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(346, 355))
			idSet.add(id)
		self.assertEqual(len(idSet), 9)

		positions = self.blackKingPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.king, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(0, 9))
			idSet.add(id)
		self.assertEqual(len(idSet), 18)

	def testMandarinFeatureIdRedActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.redMandarinPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.mandarin, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(9, 14))
			idSet.add(id)
		self.assertEqual(len(idSet), 5)

		positions = self.blackMandarinPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.mandarin, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(355, 360))
			idSet.add(id)
		self.assertEqual(len(idSet), 10)

	def testMandarinFeatureIdBlackActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.redMandarinPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.mandarin, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(355, 360))
			idSet.add(id)
		self.assertEqual(len(idSet), 5)

		positions = self.blackMandarinPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.mandarin, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(9, 14))
			idSet.add(id)
		self.assertEqual(len(idSet), 10)

	def testElephantFeatureIdRedActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.redElephantPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.elephant, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(14, 21))
			idSet.add(id)
		self.assertEqual(len(idSet), 7)

		positions = self.blackElephantPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.elephant, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(360, 367))
			idSet.add(id)
		self.assertEqual(len(idSet), 14)

	def testElephantFeatureIdBlackActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.redElephantPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.elephant, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(360, 367))
			idSet.add(id)
		self.assertEqual(len(idSet), 7)

		positions = self.blackElephantPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.elephant, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(14, 21))
			idSet.add(id)
		self.assertEqual(len(idSet), 14)

	def testKnightFeatureIdRedActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.allPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.knight, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(21, 111))
			idSet.add(id)
		self.assertEqual(len(idSet), 90)

		positions = self.allPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.knight, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(367, 457))
			idSet.add(id)
		self.assertEqual(len(idSet), 180)

	def testKnightFeatureIdBlackActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.allPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.knight, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(367, 457))
			idSet.add(id)
		self.assertEqual(len(idSet), 90)

		positions = self.allPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.knight, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(21, 111))
			idSet.add(id)
		self.assertEqual(len(idSet), 180)

	def testRookFeatureIdRedActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.allPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.rook, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(111, 201))
			idSet.add(id)
		self.assertEqual(len(idSet), 90)

		positions = self.allPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.rook, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(457, 547))
			idSet.add(id)
		self.assertEqual(len(idSet), 180)

	def testRookFeatureIdBlackActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.allPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.rook, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(457, 547))
			idSet.add(id)
		self.assertEqual(len(idSet), 90)

		positions = self.allPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.rook, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(111, 201))
			idSet.add(id)
		self.assertEqual(len(idSet), 180)

	def testCannonFeatureIdRedActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.allPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.cannon, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(201, 291))
			idSet.add(id)
		self.assertEqual(len(idSet), 90)

		positions = self.allPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.cannon, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(547, 637))
			idSet.add(id)
		self.assertEqual(len(idSet), 180)

	def testCannonFeatureIdBlackActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.allPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.cannon, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(547, 637))
			idSet.add(id)
		self.assertEqual(len(idSet), 90)

		positions = self.allPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.cannon, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(201, 291))
			idSet.add(id)
		self.assertEqual(len(idSet), 180)

	def testPawnFeatureIdRedActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.redPawnPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.pawn, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(291, 346))
			idSet.add(id)
		self.assertEqual(len(idSet), 55)

		positions = self.blackPawnPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.pawn, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(637, 692))
			idSet.add(id)
		self.assertEqual(len(idSet), 110)

	def testPawnFeatureIdBlackActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.redPawnPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.pawn, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(637, 692))
			idSet.add(id)
		self.assertEqual(len(idSet), 55)

		positions = self.blackPawnPositions()
		for pos in positions:
			id = idGen.chessmanFeatureId(Chessman.pawn, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(291, 346))
			idSet.add(id)
		self.assertEqual(len(idSet), 110)

	def testKingMoveFeatureIdRedActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.redKingPositions()
		directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = idGen.moveFeatureId(Chessman.king, Chessman.red, pos, toPos, Chessman.red)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(0, 36))
				idSet.add(id)

	def testKingMoveFeatureIdBlackActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.blackKingPositions()
		directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = idGen.moveFeatureId(Chessman.king, Chessman.black, pos, toPos, Chessman.black)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(0, 36))
				idSet.add(id)

	def testMandarinMoveFeatureIdRedActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.redMandarinPositions()
		directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = idGen.moveFeatureId(Chessman.mandarin, Chessman.red, pos, toPos, Chessman.red)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(36, 56))
				idSet.add(id)

	def testMandarinMoveFeatureIdBlackActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.blackMandarinPositions()
		directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = idGen.moveFeatureId(Chessman.mandarin, Chessman.black, pos, toPos, Chessman.black)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(36, 56))
				idSet.add(id)

	def testElephantMoveFeatureIdRedActive(self):
		idGen = MoveProbability()
		idSet = set()
		positions = self.redElephantPositions()
		directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = idGen.moveFeatureId(Chessman.elephant, Chessman.red, pos, toPos, Chessman.red)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(56, 84))
				idSet.add(id)

	def testElephantMoveFeatureIdBlackActive(self):
		pass

	def testMoveFeatureIdRedActive(self):
		pass

	def testMoveFeatureIdBlackActive(self):
		pass


if __name__ == '__main__':
	unittest.main()
