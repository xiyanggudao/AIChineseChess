import unittest
from chess.ChessData import ChessmanOnBoard
from chess.Chessman import Chessman


class TestChessmanOnBoard(unittest.TestCase):
	def testProperty(self):
		chess = ChessmanOnBoard((0, 1), Chessman.blackRook())
		self.assertEqual(chess.identifier, Chessman.blackRook())
		self.assertEqual(chess.position, (0, 1))
		self.assertEqual(chess.type, Chessman.rook)
		self.assertEqual(chess.color, Chessman.black)
		self.assertEqual(chess.x, 0)
		self.assertEqual(chess.y, 1)


if __name__ == '__main__':
	unittest.main()
