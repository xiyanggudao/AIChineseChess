import unittest
from chess.Chessgame import Chessgame
from chess.ChessData import Move
from chess.Chessman import Chessman


class TestChessgame(unittest.TestCase):
	def testConstructorDefault(self):
		game = Chessgame()
		self.assertEqual(game.moveSize(), 0)

		rKing = Chessman.redKing()
		rMandarin = Chessman.redMandarin()
		rElephant = Chessman.redElephant()
		rKnight = Chessman.redKnight()
		rRook = Chessman.redRook()
		rCannon = Chessman.redCannon()
		rPawn = Chessman.redPawn()
		bKing = Chessman.blackKing()
		bMandarin = Chessman.blackMandarin()
		bElephant = Chessman.blackElephant()
		bKnight = Chessman.blackKnight()
		bRook = Chessman.blackRook()
		bCannon = Chessman.blackCannon()
		bPawn = Chessman.blackPawn()
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

		aliveChessmen = game.chessmenOnBoard()
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

	def testChessmanAtPosition(self):
		game = Chessgame()
		self.assertEqual(game.chessmanAt((0, 1)), Chessman.invalid())
		self.assertEqual(game.chessmanAt((0, 0)), Chessman.redRook())

	def testActiveColor(self):
		game = Chessgame()
		self.assertEqual(game.activeColor(), Chessman.red)

	def testMakeMoveNoEat(self):
		game = Chessgame()
		game.makeMove((1, 2), (4, 2))
		self.assertEqual(game.moveSize(), 1)
		self.assertEqual(game.activeColor(), Chessman.black)
		self.assertEqual(game.lastMove(), Move((1, 2), (4, 2), Chessman.redCannon(), Chessman.invalid()))
		self.assertEqual(game.chessmanAt((1, 2)), Chessman.invalid())
		self.assertEqual(game.chessmanAt((4, 2)), Chessman.redCannon())
		self.assertEqual(len(game.chessmenOnBoard()), 32)

	def testMakeMoveEat(self):
		game = Chessgame()
		game.makeMove((1, 2), (1, 9))
		self.assertEqual(game.moveSize(), 1)
		self.assertEqual(game.activeColor(), Chessman.black)
		self.assertEqual(game.lastMove(), Move((1, 2), (1, 9),
			Chessman.redCannon(), Chessman.blackKnight()))
		self.assertEqual(game.chessmanAt((1, 2)), Chessman.invalid())
		self.assertEqual(game.chessmanAt((1, 9)), Chessman.redCannon())
		self.assertEqual(len(game.chessmenOnBoard()), 31)

	def testGetUcciFen(self):
		game = Chessgame()
		ucciFen = game.ucciFen()
		self.assertEqual(ucciFen, 'rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1')

	def testSetWithUcciFen(self):
		game = Chessgame()
		game.makeMove((1, 0), (2, 2))

		gameUcci = Chessgame()
		ucciFen = 'rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1CN4C1/9/R1BAKABNR b - - 0 1'
		gameUcci.setWithUcciFen(ucciFen)

		self.assertEqual(game.activeColor(), gameUcci.activeColor())
		chessmen = game.chessmenOnBoard()
		chessmenUcci = gameUcci.chessmenOnBoard()
		self.assertEqual(len(chessmen), len(chessmenUcci))
		for i in range(len(chessmen)):
			self.assertEqual(chessmen[i], chessmenUcci[i])


if __name__ == '__main__':
	unittest.main()
