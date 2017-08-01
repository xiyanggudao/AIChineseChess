import unittest
from gui.PositionCalculator import PositionCalculator


class TestPositionCalculator(unittest.TestCase):
	def testConstructorDefault(self):
		posCalculator = PositionCalculator()

		self.assertEqual(posCalculator.outlinePos(), (0, 0))
		self.assertEqual(posCalculator.outlineSize(), (0, 0))

		self.assertEqual(posCalculator.borderPos(), (0, 0))
		self.assertEqual(posCalculator.borderSize(), (0, 0))

		self.assertEqual(posCalculator.chessmanSize(), 0)

		self.assertEqual(posCalculator.coordinatePos(2, 0), (0, 0))
		self.assertEqual(posCalculator.coordinatePos(0, 4), (0, 0))
		self.assertEqual(posCalculator.coordinatePos(0, 5), (0, 0))
		self.assertEqual(posCalculator.coordinatePos(8, 9), (0, 0))

	def testMargin(self):
		posCalculator = PositionCalculator()

		posCalculator.setMargin(20)
		posCalculator.setChessboardSize(40, 40)

		self.assertEqual(posCalculator.outlinePos(), (20, 20))
		self.assertEqual(posCalculator.outlineSize(), (0, 0))

		self.assertEqual(posCalculator.borderPos(), (20, 20))
		self.assertEqual(posCalculator.borderSize(), (0, 0))

		self.assertEqual(posCalculator.chessmanSize(), 0)

		self.assertEqual(posCalculator.coordinatePos(2, 0), (20, 20))
		self.assertEqual(posCalculator.coordinatePos(0, 4), (20, 20))
		self.assertEqual(posCalculator.coordinatePos(0, 5), (20, 20))
		self.assertEqual(posCalculator.coordinatePos(8, 9), (20, 20))

	def testPadding(self):
		posCalculator = PositionCalculator()

		posCalculator.setPadding(5)
		posCalculator.setChessboardSize(10, 10)

		self.assertEqual(posCalculator.outlinePos(), (0, 0))
		self.assertEqual(posCalculator.outlineSize(), (10, 10))

		self.assertEqual(posCalculator.borderPos(), (5, 5))

		self.assertEqual(posCalculator.chessmanSize(), 0)

		self.assertEqual(posCalculator.coordinatePos(2, 0), (5, 5))
		self.assertEqual(posCalculator.coordinatePos(0, 4), (5, 5))
		self.assertEqual(posCalculator.coordinatePos(0, 5), (5, 5))
		self.assertEqual(posCalculator.coordinatePos(8, 9), (5, 5))

	def testChessmanSpacing(self):
		posCalculator = PositionCalculator()

		posCalculator.setChessmanSpacing(10)
		posCalculator.setChessboardSize(80, 90)

		self.assertEqual(posCalculator.outlinePos(), (0, 0))
		self.assertEqual(posCalculator.outlineSize(), (80, 90))

		self.assertEqual(posCalculator.borderPos(), (0, 0))
		self.assertEqual(posCalculator.borderSize(), (80, 90))

		self.assertEqual(posCalculator.chessmanSize(), 0)

		self.assertEqual(posCalculator.coordinatePos(2, 0), (20, 0))
		self.assertEqual(posCalculator.coordinatePos(0, 4), (0, 40))
		self.assertEqual(posCalculator.coordinatePos(0, 5), (0, 50))
		self.assertEqual(posCalculator.coordinatePos(8, 9), (80, 90))

	# 楚河汉界的宽度
	def testOpposingSpacing(self):
		posCalculator = PositionCalculator()

		posCalculator.setOpposingSpacing(2)
		posCalculator.setChessboardSize(0, 2)

		self.assertEqual(posCalculator.outlinePos(), (0, 0))
		self.assertEqual(posCalculator.outlineSize(), (0, 2))

		self.assertEqual(posCalculator.borderPos(), (0, 0))
		self.assertEqual(posCalculator.outlineSize(), (0, 2))

		self.assertEqual(posCalculator.chessmanSize(), 0)

		self.assertEqual(posCalculator.coordinatePos(2, 0), (0, 0))
		self.assertEqual(posCalculator.coordinatePos(0, 4), (0, 0))
		self.assertEqual(posCalculator.coordinatePos(0, 5), (0, 2))
		self.assertEqual(posCalculator.coordinatePos(8, 9), (0, 2))

	def testCalculateChessmanSize(self):
		posCalculator = PositionCalculator()
		posCalculator.setChessboardSize(80, 90)
		self.assertEqual(posCalculator.chessmanSize(), 10)
		posCalculator.setChessboardSize(85, 90)
		self.assertEqual(posCalculator.chessmanSize(), 10)
		posCalculator.setChessboardSize(160, 90)
		self.assertEqual(posCalculator.chessmanSize(), 10)
		posCalculator.setChessboardSize(160, 95)
		self.assertEqual(posCalculator.chessmanSize(), 10)
		posCalculator.setOpposingSpacing(10)
		self.assertEqual(posCalculator.chessmanSize(), 9)

	def testCalculateOutlineSize(self):
		posCalculator = PositionCalculator()
		posCalculator.setChessboardSize(80, 90)
		self.assertEqual(posCalculator.outlineSize(), (80, 90))
		posCalculator.setChessboardSize(85, 90)
		self.assertEqual(posCalculator.outlineSize(), (80, 90))
		posCalculator.setChessboardSize(160, 90)
		self.assertEqual(posCalculator.outlineSize(), (80, 90))
		posCalculator.setChessboardSize(160, 95)
		self.assertEqual(posCalculator.outlineSize(), (80, 90))
		posCalculator.setOpposingSpacing(10)
		self.assertEqual(posCalculator.outlineSize(), (72, 91))
		posCalculator.setPadding(1)
		self.assertEqual(posCalculator.outlineSize(), (74, 93))
		pass

	def testCalculateBorderSize(self):
		posCalculator = PositionCalculator()
		posCalculator.setChessboardSize(160, 95)
		posCalculator.setOpposingSpacing(10)
		posCalculator.setPadding(1)
		self.assertEqual(posCalculator.borderSize(), (72, 91))

	def testCalculateCoordinatePos(self):
		posCalculator = PositionCalculator()
		posCalculator.setChessboardSize(80, 100)
		posCalculator.setOpposingSpacing(10)
		self.assertEqual(posCalculator.coordinatePos(2, 0), (20, 0))
		self.assertEqual(posCalculator.coordinatePos(0, 4), (0, 40))
		self.assertEqual(posCalculator.coordinatePos(0, 5), (0, 60))
		self.assertEqual(posCalculator.coordinatePos(8, 9), (80, 100))
		posCalculator.setChessmanSpacing(1)
		self.assertEqual(posCalculator.coordinatePos(2, 0), (20, 0))
		self.assertEqual(posCalculator.coordinatePos(0, 4), (0, 40))
		self.assertEqual(posCalculator.coordinatePos(0, 5), (0, 60))
		self.assertEqual(posCalculator.coordinatePos(8, 9), (80, 100))

	def testCalculateBoardSize(self):
		posCalculator = PositionCalculator()
		self.assertEqual(posCalculator.boardSizeForFixedChessmanSize(10), (80, 90))
		posCalculator.setChessmanSpacing(1)
		self.assertEqual(posCalculator.boardSizeForFixedChessmanSize(10), (88, 99))
		posCalculator.setOpposingSpacing(2)
		self.assertEqual(posCalculator.boardSizeForFixedChessmanSize(10), (88, 101))
		posCalculator.setPadding(3)
		self.assertEqual(posCalculator.boardSizeForFixedChessmanSize(10), (94, 107))
		posCalculator.setMargin(4)
		self.assertEqual(posCalculator.boardSizeForFixedChessmanSize(10), (102, 115))


if __name__ == '__main__':
	unittest.main()
