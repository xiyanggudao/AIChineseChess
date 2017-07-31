import unittest
from chess.Chessgame import Chessgame
from chess.Chessgame import ChessmanOnBoard
from chess.Chessman import Chessman


class TestChessmanOnBoard(unittest.TestCase):
	def testProperty(self):
		chess = ChessmanOnBoard((0, 1), Chessman.getIdentifier(Chessman.rook, Chessman.black))
		self.assertEqual(chess.identifier, Chessman.getIdentifier(Chessman.rook, Chessman.black))
		self.assertEqual(chess.position, (0, 1))
		self.assertEqual(chess.type, Chessman.rook)
		self.assertEqual(chess.color, Chessman.black)
		self.assertEqual(chess.x, 0)
		self.assertEqual(chess.y, 1)

class TestChessgame(unittest.TestCase):
	def testConstructorDefault(self):
		game = Chessgame()
		self.assertEqual(game.getMoveSize(), 0)


if __name__ == '__main__':
	unittest.main()
