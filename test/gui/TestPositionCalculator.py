import unittest
from gui.PositionCalculator import PositionCalculator


class TestPositionCalculator(unittest.TestCase):
	def testConstructorDefault(self):
		posCalculator = PositionCalculator()
		self.assertEqual(posCalculator.getOutlinePos(), (0, 0))
		self.assertEqual(posCalculator.getBorderPos(), (0, 0))
		self.assertEqual(posCalculator.getCoordinatePos(0, 2), (0, 0))
		self.assertEqual(posCalculator.getCoordinatePos(4, 0), (0, 0))
		self.assertEqual(posCalculator.getCoordinatePos(5, 0), (0, 0))
		self.assertEqual(posCalculator.getCoordinatePos(9, 8), (0, 0))

	def testMargin(self):
		posCalculator = PositionCalculator()
		posCalculator.setMargin(20)
		posCalculator.setBoardSize(40, 40)
		self.assertEqual(posCalculator.getOutlinePos(), (20, 20))
		self.assertEqual(posCalculator.getBorderPos(), (20, 20))
		self.assertEqual(posCalculator.getCoordinatePos(0, 2), (20, 20))
		self.assertEqual(posCalculator.getCoordinatePos(4, 0), (20, 20))
		self.assertEqual(posCalculator.getCoordinatePos(5, 0), (20, 20))
		self.assertEqual(posCalculator.getCoordinatePos(9, 8), (20, 20))

	def testPadding(self):
		posCalculator = PositionCalculator()
		posCalculator.setPadding(5)
		posCalculator.setBoardSize(10, 10)
		self.assertEqual(posCalculator.getOutlinePos(), (0, 0))
		self.assertEqual(posCalculator.getBorderPos(), (5, 5))
		self.assertEqual(posCalculator.getCoordinatePos(0, 2), (5, 5))
		self.assertEqual(posCalculator.getCoordinatePos(4, 0), (5, 5))
		self.assertEqual(posCalculator.getCoordinatePos(5, 0), (5, 5))
		self.assertEqual(posCalculator.getCoordinatePos(9, 8), (5, 5))

	def testChessSpacing(self):
		posCalculator = PositionCalculator()
		posCalculator.setChessSpacing(3)


if __name__ == '__main__':
	unittest.main()
