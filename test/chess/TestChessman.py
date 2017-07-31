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

		value = Chessman.getIdentifier(Chessman.king, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.mandarin, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.elephant, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.knight, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.rook, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.cannon, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.pawn, Chessman.red)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.king, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.mandarin, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.elephant, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.knight, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.rook, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.cannon, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		value = Chessman.getIdentifier(Chessman.pawn, Chessman.black)
		self.assertFalse(value in idSet)
		idSet.add(value)

		self.assertEqual(len(idSet), 14)

	def testIdentifierTransform(self):
		redKing = Chessman.getIdentifier(Chessman.king, Chessman.red)
		blackKing = Chessman.getIdentifier(Chessman.king, Chessman.black)

		self.assertNotEqual(redKing, blackKing)

		self.assertEqual(Chessman.getType(redKing), Chessman.king)
		self.assertEqual(Chessman.getType(blackKing), Chessman.king)

		self.assertEqual(Chessman.getColor(redKing), Chessman.red)
		self.assertEqual(Chessman.getColor(blackKing), Chessman.black)


if __name__ == '__main__':
	unittest.main()
