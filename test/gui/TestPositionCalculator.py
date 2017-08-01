import unittest
from gui.PositionCalculator import PositionCalculator


class TestPositionCalculator(unittest.TestCase):
	def testConstructorDefault(self):
		posCalculator = PositionCalculator()

		self.assertEqual(posCalculator.getOutlinePos(), (0, 0))
		self.assertEqual(posCalculator.getOutlineSize(), (0, 0))

		self.assertEqual(posCalculator.getBorderPos(), (0, 0))
		self.assertEqual(posCalculator.getBorderSize(), (0, 0))

		self.assertEqual(posCalculator.getChessmanSize(), 0)

		self.assertEqual(posCalculator.getCoordinatePos(2, 0), (0, 0))
		self.assertEqual(posCalculator.getCoordinatePos(0, 4), (0, 0))
		self.assertEqual(posCalculator.getCoordinatePos(0, 5), (0, 0))
		self.assertEqual(posCalculator.getCoordinatePos(8, 9), (0, 0))

	def testMargin(self):
		posCalculator = PositionCalculator()

		posCalculator.setMargin(20)
		posCalculator.setChessboardSize(40, 40)

		self.assertEqual(posCalculator.getOutlinePos(), (20, 20))
		self.assertEqual(posCalculator.getOutlineSize(), (0, 0))

		self.assertEqual(posCalculator.getBorderPos(), (20, 20))
		self.assertEqual(posCalculator.getBorderSize(), (0, 0))

		self.assertEqual(posCalculator.getChessmanSize(), 0)

		self.assertEqual(posCalculator.getCoordinatePos(2, 0), (20, 20))
		self.assertEqual(posCalculator.getCoordinatePos(0, 4), (20, 20))
		self.assertEqual(posCalculator.getCoordinatePos(0, 5), (20, 20))
		self.assertEqual(posCalculator.getCoordinatePos(8, 9), (20, 20))

	def testPadding(self):
		posCalculator = PositionCalculator()

		posCalculator.setPadding(5)
		posCalculator.setChessboardSize(10, 10)

		self.assertEqual(posCalculator.getOutlinePos(), (0, 0))
		self.assertEqual(posCalculator.getOutlineSize(), (10, 10))

		self.assertEqual(posCalculator.getBorderPos(), (5, 5))

		self.assertEqual(posCalculator.getChessmanSize(), 0)

		self.assertEqual(posCalculator.getCoordinatePos(2, 0), (5, 5))
		self.assertEqual(posCalculator.getCoordinatePos(0, 4), (5, 5))
		self.assertEqual(posCalculator.getCoordinatePos(0, 5), (5, 5))
		self.assertEqual(posCalculator.getCoordinatePos(8, 9), (5, 5))

	def testChessmanSpacing(self):
		posCalculator = PositionCalculator()

		posCalculator.setChessmanSpacing(10)
		posCalculator.setChessboardSize(80, 90)

		self.assertEqual(posCalculator.getOutlinePos(), (0, 0))
		self.assertEqual(posCalculator.getOutlineSize(), (80, 90))

		self.assertEqual(posCalculator.getBorderPos(), (0, 0))
		self.assertEqual(posCalculator.getBorderSize(), (80, 90))

		self.assertEqual(posCalculator.getChessmanSize(), 0)

		self.assertEqual(posCalculator.getCoordinatePos(2, 0), (20, 0))
		self.assertEqual(posCalculator.getCoordinatePos(0, 4), (0, 40))
		self.assertEqual(posCalculator.getCoordinatePos(0, 5), (0, 50))
		self.assertEqual(posCalculator.getCoordinatePos(8, 9), (80, 90))

	# 楚河汉界的宽度
	def testOpposingSpacing(self):
		posCalculator = PositionCalculator()

		posCalculator.setOpposingSpacing(2)
		posCalculator.setChessboardSize(0, 2)

		self.assertEqual(posCalculator.getOutlinePos(), (0, 0))
		self.assertEqual(posCalculator.getOutlineSize(), (0, 2))

		self.assertEqual(posCalculator.getBorderPos(), (0, 0))
		self.assertEqual(posCalculator.getOutlineSize(), (0, 2))

		self.assertEqual(posCalculator.getChessmanSize(), 0)

		self.assertEqual(posCalculator.getCoordinatePos(2, 0), (0, 0))
		self.assertEqual(posCalculator.getCoordinatePos(0, 4), (0, 0))
		self.assertEqual(posCalculator.getCoordinatePos(0, 5), (0, 2))
		self.assertEqual(posCalculator.getCoordinatePos(8, 9), (0, 2))

	def testCalculateChessmanSize(self):
		posCalculator = PositionCalculator()
		posCalculator.setChessboardSize(80, 90)
		self.assertEqual(posCalculator.getChessmanSize(), 10)
		posCalculator.setChessboardSize(85, 90)
		self.assertEqual(posCalculator.getChessmanSize(), 10)
		posCalculator.setChessboardSize(160, 90)
		self.assertEqual(posCalculator.getChessmanSize(), 10)
		posCalculator.setChessboardSize(160, 95)
		self.assertEqual(posCalculator.getChessmanSize(), 10)
		posCalculator.setOpposingSpacing(10)
		self.assertEqual(posCalculator.getChessmanSize(), 9)

	def testCalculateOutlineSize(self):
		posCalculator = PositionCalculator()
		posCalculator.setChessboardSize(80, 90)
		self.assertEqual(posCalculator.getOutlineSize(), (80, 90))
		posCalculator.setChessboardSize(85, 90)
		self.assertEqual(posCalculator.getOutlineSize(), (80, 90))
		posCalculator.setChessboardSize(160, 90)
		self.assertEqual(posCalculator.getOutlineSize(), (80, 90))
		posCalculator.setChessboardSize(160, 95)
		self.assertEqual(posCalculator.getOutlineSize(), (80, 90))
		posCalculator.setOpposingSpacing(10)
		self.assertEqual(posCalculator.getOutlineSize(), (72, 81))
		pass

	def testCalculateBorderSize(self):
		pass

	def testCalculateBoardSize(self):
		pass


if __name__ == '__main__':
	unittest.main()
