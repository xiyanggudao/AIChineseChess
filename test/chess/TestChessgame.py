import unittest
from chess.Chessgame import Chessgame
from chess.Chessgame import ChessmanOnBoard
from chess.Chessman import Chessman


class TestChessmanOnBoard(unittest.TestCase):
	def testProperty(self):
		chess = ChessmanOnBoard((0, 1), Chessman.identifier(Chessman.rook, Chessman.black))
		self.assertEqual(chess.identifier, Chessman.identifier(Chessman.rook, Chessman.black))
		self.assertEqual(chess.position, (0, 1))
		self.assertEqual(chess.type, Chessman.rook)
		self.assertEqual(chess.color, Chessman.black)
		self.assertEqual(chess.x, 0)
		self.assertEqual(chess.y, 1)

class TestChessgame(unittest.TestCase):
	def testConstructorDefault(self):
		game = Chessgame()
		self.assertEqual(game.moveSize(), 0)

		rKing = Chessman.identifier(Chessman.king, Chessman.red)
		rMandarin = Chessman.identifier(Chessman.mandarin, Chessman.red)
		rElephant = Chessman.identifier(Chessman.elephant, Chessman.red)
		rKnight = Chessman.identifier(Chessman.knight, Chessman.red)
		rRook = Chessman.identifier(Chessman.rook, Chessman.red)
		rCannon = Chessman.identifier(Chessman.cannon, Chessman.red)
		rPawn = Chessman.identifier(Chessman.pawn, Chessman.red)
		bKing = Chessman.identifier(Chessman.king, Chessman.black)
		bMandarin = Chessman.identifier(Chessman.mandarin, Chessman.black)
		bElephant = Chessman.identifier(Chessman.elephant, Chessman.black)
		bKnight = Chessman.identifier(Chessman.knight, Chessman.black)
		bRook = Chessman.identifier(Chessman.rook, Chessman.black)
		bCannon = Chessman.identifier(Chessman.cannon, Chessman.black)
		bPawn = Chessman.identifier(Chessman.pawn, Chessman.black)
		board = [
			[rRook,rKnight,rElephant,rMandarin,rKing,rMandarin,rElephant,rKnight,rRook],
			[None,None,None,None,None,None,None,None,None],
			[None,rCannon,None,None,None,None,None,rCannon,None],
			[rPawn,None,rPawn,None,rPawn,None,rPawn,None,rPawn],
			[None,None,None,None,None,None,None,None,None],
			[None,None,None,None,None,None,None,None,None],
			[bPawn,None,bPawn,None,bPawn,None,bPawn,None,bPawn],
			[None,bCannon,None,None,None,None,None,bCannon,None],
			[None,None,None,None,None,None,None,None,None],
			[bRook,bKnight,bElephant,bMandarin,bKing,bMandarin,bElephant,bKnight,bRook]
		]

		aliveChessmen = game.aliveChessmen()
		for chess in aliveChessmen:
			self.assertEqual(chess.identifier, board[chess.y][chess.x], chess.position)
		for x in range(0, 9):
			for y in range(0, 10):
				id = board[y][x]
				if id == None:
					continue
				for chess in aliveChessmen:
					if chess.position == (x, y) and chess.identifier == id:
						break
				else:
					self.assertTrue(False)
		self.assertEqual(len(aliveChessmen), 32)


if __name__ == '__main__':
	unittest.main()
