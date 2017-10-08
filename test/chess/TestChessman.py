import unittest
from chess.Chessman import Chessman


class TestChessman(unittest.TestCase):

	def testColorUnique(self):
		self.assertNotEqual(Chessman.red, Chessman.black)

	def testTypeUnique(self):
		typeSet = set()
		typeSet.add(Chessman.king)
		typeSet.add(Chessman.mandarin)
		typeSet.add(Chessman.elephant)
		typeSet.add(Chessman.knight)
		typeSet.add(Chessman.rook)
		typeSet.add(Chessman.cannon)
		typeSet.add(Chessman.pawn)
		self.assertEqual(len(typeSet), 7)

	def testIdentifierUnique(self):
		idSet = set()

		value = Chessman.identifier(Chessman.king, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.mandarin, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.elephant, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.knight, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.rook, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.cannon, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.pawn, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.king, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.mandarin, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.elephant, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.knight, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.rook, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.cannon, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.identifier(Chessman.pawn, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.invalid()
		self.assertFalse(value in idSet)
		idSet.add(value)

		self.assertEqual(len(idSet), 15)

	def testIdentifierTransform(self):
		redKing = Chessman.identifier(Chessman.king, Chessman.red)
		blackKing = Chessman.identifier(Chessman.king, Chessman.black)

		self.assertNotEqual(redKing, blackKing)

		self.assertEqual(Chessman.type(redKing), Chessman.king)
		self.assertEqual(Chessman.type(blackKing), Chessman.king)

		self.assertEqual(Chessman.color(redKing), Chessman.red)
		self.assertEqual(Chessman.color(blackKing), Chessman.black)

	def testOppositeColor(self):
		self.assertEqual(Chessman.oppositeColor(Chessman.red), Chessman.black)
		self.assertEqual(Chessman.oppositeColor(Chessman.black), Chessman.red)

	def testStaticIdentifierMethod(self):
		idSet = set()
		idSet.add(Chessman.redKing())
		idSet.add(Chessman.redMandarin())
		idSet.add(Chessman.redElephant())
		idSet.add(Chessman.redKnight())
		idSet.add(Chessman.redRook())
		idSet.add(Chessman.redCannon())
		idSet.add(Chessman.redPawn())
		idSet.add(Chessman.blackKing())
		idSet.add(Chessman.blackMandarin())
		idSet.add(Chessman.blackElephant())
		idSet.add(Chessman.blackKnight())
		idSet.add(Chessman.blackRook())
		idSet.add(Chessman.blackCannon())
		idSet.add(Chessman.blackPawn())
		idSet.add(Chessman.invalid())
		self.assertEqual(len(idSet), 15)


if __name__ == '__main__':
	unittest.main()
