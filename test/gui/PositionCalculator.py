import unittest
from gui.PositionCalculator import PositionCalculator


class TestPositionCalculator(unittest.TestCase):
	def testConstructor(self):
		posCalculator = PositionCalculator()
		self.assertEqual(posCalculator.getOutlinePos(), (0, 0))


if __name__ == '__main__':
	unittest.main()
