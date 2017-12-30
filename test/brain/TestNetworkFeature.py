import brain.NetworkFeature as nf
from chess.Chessman import Chessman
import unittest
from chess.Chessgame import Chessgame
from chess.MoveGenerator import MoveGenerator

class TestNetworkFeature(unittest.TestCase):

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
		idSet = set()
		positions = self.redKingPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.king, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(0, 9))
			idSet.add(id)
		self.assertEqual(len(idSet), 9)

		positions = self.blackKingPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.king, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(346, 355))
			idSet.add(id)
		self.assertEqual(len(idSet), 18)

	def testKingFeatureIdBlackActive(self):
		idSet = set()
		positions = self.redKingPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.king, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(346, 355))
			idSet.add(id)
		self.assertEqual(len(idSet), 9)

		positions = self.blackKingPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.king, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(0, 9))
			idSet.add(id)
		self.assertEqual(len(idSet), 18)

	def testMandarinFeatureIdRedActive(self):
		idSet = set()
		positions = self.redMandarinPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.mandarin, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(9, 14))
			idSet.add(id)
		self.assertEqual(len(idSet), 5)

		positions = self.blackMandarinPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.mandarin, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(355, 360))
			idSet.add(id)
		self.assertEqual(len(idSet), 10)

	def testMandarinFeatureIdBlackActive(self):
		idSet = set()
		positions = self.redMandarinPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.mandarin, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(355, 360))
			idSet.add(id)
		self.assertEqual(len(idSet), 5)

		positions = self.blackMandarinPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.mandarin, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(9, 14))
			idSet.add(id)
		self.assertEqual(len(idSet), 10)

	def testElephantFeatureIdRedActive(self):
		idSet = set()
		positions = self.redElephantPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.elephant, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(14, 21))
			idSet.add(id)
		self.assertEqual(len(idSet), 7)

		positions = self.blackElephantPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.elephant, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(360, 367))
			idSet.add(id)
		self.assertEqual(len(idSet), 14)

	def testElephantFeatureIdBlackActive(self):
		idSet = set()
		positions = self.redElephantPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.elephant, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(360, 367))
			idSet.add(id)
		self.assertEqual(len(idSet), 7)

		positions = self.blackElephantPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.elephant, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(14, 21))
			idSet.add(id)
		self.assertEqual(len(idSet), 14)

	def testKnightFeatureIdRedActive(self):
		idSet = set()
		positions = self.allPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.knight, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(21, 111))
			idSet.add(id)
		self.assertEqual(len(idSet), 90)

		positions = self.allPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.knight, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(367, 457))
			idSet.add(id)
		self.assertEqual(len(idSet), 180)

	def testKnightFeatureIdBlackActive(self):
		idSet = set()
		positions = self.allPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.knight, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(367, 457))
			idSet.add(id)
		self.assertEqual(len(idSet), 90)

		positions = self.allPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.knight, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(21, 111))
			idSet.add(id)
		self.assertEqual(len(idSet), 180)

	def testRookFeatureIdRedActive(self):
		idSet = set()
		positions = self.allPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.rook, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(111, 201))
			idSet.add(id)
		self.assertEqual(len(idSet), 90)

		positions = self.allPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.rook, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(457, 547))
			idSet.add(id)
		self.assertEqual(len(idSet), 180)

	def testRookFeatureIdBlackActive(self):
		idSet = set()
		positions = self.allPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.rook, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(457, 547))
			idSet.add(id)
		self.assertEqual(len(idSet), 90)

		positions = self.allPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.rook, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(111, 201))
			idSet.add(id)
		self.assertEqual(len(idSet), 180)

	def testCannonFeatureIdRedActive(self):
		idSet = set()
		positions = self.allPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.cannon, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(201, 291))
			idSet.add(id)
		self.assertEqual(len(idSet), 90)

		positions = self.allPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.cannon, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(547, 637))
			idSet.add(id)
		self.assertEqual(len(idSet), 180)

	def testCannonFeatureIdBlackActive(self):
		idSet = set()
		positions = self.allPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.cannon, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(547, 637))
			idSet.add(id)
		self.assertEqual(len(idSet), 90)

		positions = self.allPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.cannon, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(201, 291))
			idSet.add(id)
		self.assertEqual(len(idSet), 180)

	def testPawnFeatureIdRedActive(self):
		idSet = set()
		positions = self.redPawnPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.pawn, Chessman.red, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(291, 346))
			idSet.add(id)
		self.assertEqual(len(idSet), 55)

		positions = self.blackPawnPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.pawn, Chessman.black, pos, Chessman.red)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(637, 692))
			idSet.add(id)
		self.assertEqual(len(idSet), 110)

	def testPawnFeatureIdBlackActive(self):
		idSet = set()
		positions = self.redPawnPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.pawn, Chessman.red, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(637, 692))
			idSet.add(id)
		self.assertEqual(len(idSet), 55)

		positions = self.blackPawnPositions()
		for pos in positions:
			id = nf.chessmanFeatureId(Chessman.pawn, Chessman.black, pos, Chessman.black)
			self.assertFalse(id in idSet)
			self.assertTrue(id in range(291, 346))
			idSet.add(id)
		self.assertEqual(len(idSet), 110)

	def testKingMoveFeatureIdRedActive(self):
		idSet = set()
		positions = self.redKingPositions()
		directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = nf.moveFeatureId(Chessman.king, Chessman.red, pos, toPos, Chessman.red)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(0, 36))
				idSet.add(id)
		self.assertEqual(len(idSet), 36)

	def testKingMoveFeatureIdBlackActive(self):
		idSet = set()
		positions = self.blackKingPositions()
		directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = nf.moveFeatureId(Chessman.king, Chessman.black, pos, toPos, Chessman.black)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(0, 36))
				idSet.add(id)
		self.assertEqual(len(idSet), 36)

	def testMandarinMoveFeatureIdRedActive(self):
		idSet = set()
		positions = self.redMandarinPositions()
		directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = nf.moveFeatureId(Chessman.mandarin, Chessman.red, pos, toPos, Chessman.red)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(36, 56))
				idSet.add(id)
		self.assertEqual(len(idSet), 20)

	def testMandarinMoveFeatureIdBlackActive(self):
		idSet = set()
		positions = self.blackMandarinPositions()
		directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = nf.moveFeatureId(Chessman.mandarin, Chessman.black, pos, toPos, Chessman.black)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(36, 56))
				idSet.add(id)
		self.assertEqual(len(idSet), 20)

	def testElephantMoveFeatureIdRedActive(self):
		idSet = set()
		positions = self.redElephantPositions()
		directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = nf.moveFeatureId(Chessman.elephant, Chessman.red, pos, toPos, Chessman.red)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(56, 84))
				idSet.add(id)
		self.assertEqual(len(idSet), 28)

	def testElephantMoveFeatureIdBlackActive(self):
		idSet = set()
		positions = self.blackElephantPositions()
		directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = nf.moveFeatureId(Chessman.elephant, Chessman.black, pos, toPos, Chessman.black)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(56, 84))
				idSet.add(id)
		self.assertEqual(len(idSet), 28)

	def testKnightMoveFeatureIdRedActive(self):
		idSet = set()
		positions = self.allPositions()
		directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = nf.moveFeatureId(Chessman.knight, Chessman.red, pos, toPos, Chessman.red)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(84, 804))
				idSet.add(id)
		self.assertEqual(len(idSet), 720)

	def testKnightMoveFeatureIdBlackActive(self):
		idSet = set()
		positions = self.allPositions()
		directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = nf.moveFeatureId(Chessman.knight, Chessman.black, pos, toPos, Chessman.black)
				self.assertFalse(id in idSet)
				self.assertTrue(id in range(84, 804))
				idSet.add(id)
		self.assertEqual(len(idSet), 720)

	def testRookMoveFeatureIdRedActive(self):
		idSet = set()
		positions = self.allPositions()
		directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
		for pos in positions:
			for dir in directions:
				tx, ty = (pos[0]+dir[0], pos[1]+dir[1])
				while 0 <= tx < 9 and 0 <= ty < 10:
					id = nf.moveFeatureId(Chessman.rook, Chessman.red, pos, (tx, ty), Chessman.red)
					self.assertFalse(id in idSet, 'id '+str(id)+' pos '+str(pos)+' toPos '+str((tx, ty)))
					self.assertTrue(id in range(804, 2424))
					idSet.add(id)
					tx, ty = (tx+dir[0], ty+dir[1])
		self.assertEqual(len(idSet), 1530)

	def testRookMoveFeatureIdBlackActive(self):
		idSet = set()
		positions = self.allPositions()
		directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
		for pos in positions:
			for dir in directions:
				tx, ty = (pos[0]+dir[0], pos[1]+dir[1])
				while 0 <= tx < 9 and 0 <= ty < 10:
					id = nf.moveFeatureId(Chessman.rook, Chessman.black, pos, (tx, ty), Chessman.black)
					self.assertFalse(id in idSet, 'id '+str(id)+' pos '+str(pos)+' toPos '+str((tx, ty)))
					self.assertTrue(id in range(804, 2424))
					idSet.add(id)
					tx, ty = (tx+dir[0], ty+dir[1])
		self.assertEqual(len(idSet), 1530)

	def testCannonMoveFeatureIdRedActive(self):
		idSet = set()
		positions = self.allPositions()
		directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
		for pos in positions:
			for dir in directions:
				tx, ty = (pos[0]+dir[0], pos[1]+dir[1])
				while 0 <= tx < 9 and 0 <= ty < 10:
					id = nf.moveFeatureId(Chessman.cannon, Chessman.red, pos, (tx, ty), Chessman.red)
					self.assertFalse(id in idSet, 'id '+str(id)+' pos '+str(pos)+' toPos '+str((tx, ty)))
					self.assertTrue(id in range(2424, 4044))
					idSet.add(id)
					tx, ty = (tx+dir[0], ty+dir[1])
		self.assertEqual(len(idSet), 1530)

	def testCannonMoveFeatureIdBlackActive(self):
		idSet = set()
		positions = self.allPositions()
		directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
		for pos in positions:
			for dir in directions:
				tx, ty = (pos[0]+dir[0], pos[1]+dir[1])
				while 0 <= tx < 9 and 0 <= ty < 10:
					id = nf.moveFeatureId(Chessman.cannon, Chessman.black, pos, (tx, ty), Chessman.black)
					self.assertFalse(id in idSet, 'id '+str(id)+' pos '+str(pos)+' toPos '+str((tx, ty)))
					self.assertTrue(id in range(2424, 4044))
					idSet.add(id)
					tx, ty = (tx+dir[0], ty+dir[1])
		self.assertEqual(len(idSet), 1530)

	def testPawnMoveFeatureIdRedActive(self):
		idSet = set()
		positions = self.redPawnPositions()
		directions = [(-1, 0), (0, 1), (1, 0)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = nf.moveFeatureId(Chessman.pawn, Chessman.red, pos, toPos, Chessman.red)
				self.assertFalse(id in idSet, 'id '+str(id)+' pos '+str(pos)+' toPos '+str(toPos))
				self.assertTrue(id in range(4044, 4209))
				idSet.add(id)
		self.assertEqual(len(idSet), 165)

	def testPawnMoveFeatureIdBlackActive(self):
		idSet = set()
		positions = self.blackPawnPositions()
		directions = [(-1, 0), (0, -1), (1, 0)]
		for pos in positions:
			for dir in directions:
				toPos = (pos[0]+dir[0], pos[1]+dir[1])
				id = nf.moveFeatureId(Chessman.pawn, Chessman.black, pos, toPos, Chessman.black)
				self.assertFalse(id in idSet, 'id '+str(id)+' pos '+str(pos)+' toPos '+str(toPos))
				self.assertTrue(id in range(4044, 4209))
				idSet.add(id)
		self.assertEqual(len(idSet), 165)

	def testBoardImage(self):
		expect = [[[0 for k in range(14)] for j in range(10)] for i in range(9)]
		expect[4][0][0] = 1
		expect[3][0][1] = 1
		expect[5][0][1] = 1
		expect[2][0][2] = 1
		expect[6][0][2] = 1
		expect[1][0][3] = 1
		expect[7][0][3] = 1
		expect[0][0][4] = 1
		expect[8][0][4] = 1
		expect[4][2][5] = 1
		expect[7][2][5] = 1
		expect[0][3][6] = 1
		expect[2][3][6] = 1
		expect[4][3][6] = 1
		expect[6][3][6] = 1
		expect[8][3][6] = 1
		expect[0][6][13] = 1
		expect[2][6][13] = 1
		expect[4][6][13] = 1
		expect[6][6][13] = 1
		expect[8][6][13] = 1
		expect[1][7][12] = 1
		expect[7][7][12] = 1
		expect[0][9][11] = 1
		expect[8][9][11] = 1
		expect[2][7][10] = 1
		expect[7][9][10] = 1
		expect[2][9][9] = 1
		expect[6][9][9] = 1
		expect[3][9][8] = 1
		expect[5][9][8] = 1
		expect[4][9][7] = 1

		game = Chessgame()
		game.makeMove((1, 2), (4, 2))
		game.makeMove((1, 9), (2, 7))
		imageIds = nf.boardImageIds(game.chessmenOnBoard(), game.activeColor())

		self.assertEqual(len(imageIds), 32)
		for id in imageIds:
			x, y, h = nf.imageIdToIndex(id)
			self.assertEqual(expect[x][y][h], 1)

	def testMoveFeatureId2(self):
		game = Chessgame()
		moveGen = MoveGenerator(game)
		idSet = set()
		moves = moveGen.generateLegalMoves()
		for move in moves:
			id = nf.moveFeatureId2(move.fromPos, move.toPos)
			self.assertNotEqual(id, -1)
			self.assertFalse(id in idSet)
			idSet.add(id)

		game.makeMove((1, 2), (4, 2))
		idSet.clear()
		moves = moveGen.generateLegalMoves()
		for move in moves:
			id = nf.moveFeatureId2(move.fromPos, move.toPos)
			self.assertNotEqual(id, -1)
			self.assertFalse(id in idSet)
			idSet.add(id)


if __name__ == '__main__':
	unittest.main()
