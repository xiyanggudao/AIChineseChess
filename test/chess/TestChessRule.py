import unittest
from chess.ChessRule import ChessRule
from chess.Chessgame import Chessgame
from chess.ChessData import Move
from chess.Chessman import Chessman


class TestChessRule(unittest.TestCase):

	def testIsMoveConformToChessboard(self):
		game = Chessgame()
		rule = ChessRule()
		rule.setChessmenOnBoard(game.chessmenOnBoard())
		rule.setActiveColor(game.activeColor())
		move = Move((1, 2), (4, 2), Chessman.identifier(Chessman.cannon, Chessman.red), None)
		self.assertTrue(rule.isMoveConformToChessboard(move))

	def testMoveActiveColorChessman(self):
		game = Chessgame()
		rule = ChessRule()
		rule.setChessmenOnBoard(game.chessmenOnBoard())
		rule.setActiveColor(game.activeColor())
		move = Move((1, 2), (4, 2), Chessman.identifier(Chessman.cannon, Chessman.red), None)
		self.assertTrue(rule.isMoveRightColor(move))
		move = Move((1, 7), (4, 7), Chessman.identifier(Chessman.cannon, Chessman.black), None)
		self.assertFalse(rule.isMoveRightColor(move))

	def testNotEatSelf(self):
		game = Chessgame()
		rule = ChessRule()
		rule.setChessmenOnBoard(game.chessmenOnBoard())
		rule.setActiveColor(game.activeColor())


if __name__ == '__main__':
	unittest.main()
