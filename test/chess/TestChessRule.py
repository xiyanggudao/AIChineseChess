import unittest
from chess.ChessRule import ChessRule
from chess.Chessgame import Chessgame
from chess.ChessData import Move
from chess.ChessData import ChessmanOnBoard
from chess.Chessman import Chessman


class TestChessRule(unittest.TestCase):

	def testPositionRange(self):
		rule = ChessRule()
		move = Move((1, 2), (4, 2), None, None)
		self.assertTrue(rule.isPositionRangeLegal(move))
		move = Move((0, 0), (8, 9), None, None)
		self.assertTrue(rule.isPositionRangeLegal(move))
		move = Move((0, -1), (4, 2), None, None)
		self.assertFalse(rule.isPositionRangeLegal(move))
		move = Move((0, 2), (-1, 2), None, None)
		self.assertFalse(rule.isPositionRangeLegal(move))
		move = Move((9, 2), (4, 2), None, None)
		self.assertFalse(rule.isPositionRangeLegal(move))
		move = Move((0, 2), (4, 10), None, None)
		self.assertFalse(rule.isPositionRangeLegal(move))

	def testIsMoveConformToChessboard(self):
		game = Chessgame()
		rule = ChessRule()
		rule.setChessmenOnBoard(game.chessmenOnBoard())
		rule.setActiveColor(game.activeColor())
		move = Move((1, 2), (4, 2), Chessman.redCannon(), None)
		self.assertTrue(rule.isMoveConformToChessboard(move))
		move = Move((1, 2), (4, 2), None, None)
		self.assertFalse(rule.isMoveConformToChessboard(move))
		move = Move((1, 2), (4, 2), Chessman.redCannon(), Chessman.blackCannon())
		self.assertFalse(rule.isMoveConformToChessboard(move))

	def testMoveActiveColorChessman(self):
		game = Chessgame()
		rule = ChessRule()
		rule.setChessmenOnBoard(game.chessmenOnBoard())
		rule.setActiveColor(game.activeColor())
		move = Move((1, 2), (4, 2), Chessman.redCannon(), None)
		self.assertTrue(rule.isMoveRightColor(move))
		move = Move((1, 7), (4, 7), Chessman.blackCannon(), None)
		self.assertFalse(rule.isMoveRightColor(move))

	def testNotEatSelf(self):
		game = Chessgame()
		rule = ChessRule()
		rule.setChessmenOnBoard(game.chessmenOnBoard())
		rule.setActiveColor(game.activeColor())
		move = Move((0, 0), (0, 3), Chessman.redRook(), Chessman.redPawn())
		self.assertTrue(rule.isEatSelf(move))
		move = Move((0, 0), (0, 1), Chessman.redRook(), None)
		self.assertFalse(rule.isEatSelf(move))

	def testMoveRuleOfRedKing(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 1), Chessman.redKing())])
		move = Move((4, 1), (3, 1), Chessman.redKing(), None)
		self.assertTrue(rule.isMoveOfRedKingLegal(move))
		move = Move((4, 1), (4, 2), Chessman.redKing(), None)
		self.assertTrue(rule.isMoveOfRedKingLegal(move))
		move = Move((4, 1), (5, 2), Chessman.redKing(), None)
		self.assertFalse(rule.isMoveOfRedKingLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((5, 1), Chessman.redKing())])
		move = Move((5, 1), (6, 1), Chessman.redKing(), None)
		self.assertFalse(rule.isMoveOfRedKingLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 2), Chessman.redKing())])
		move = Move((4, 2), (4, 3), Chessman.redKing(), None)
		self.assertFalse(rule.isMoveOfRedKingLegal(move))

	def testMoveRuleOfBlackKing(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 8), Chessman.blackKing())])
		move = Move((4, 8), (3, 8), Chessman.blackKing(), None)
		self.assertTrue(rule.isMoveOfBlackKingLegal(move))
		move = Move((4, 8), (4, 9), Chessman.blackKing(), None)
		self.assertTrue(rule.isMoveOfBlackKingLegal(move))
		move = Move((4, 8), (5, 9), Chessman.blackKing(), None)
		self.assertFalse(rule.isMoveOfBlackKingLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((5, 8), Chessman.blackKing())])
		move = Move((5, 8), (6, 8), Chessman.blackKing(), None)
		self.assertFalse(rule.isMoveOfBlackKingLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 9), Chessman.blackKing())])
		move = Move((4, 9), (4, 10), Chessman.blackKing(), None)
		self.assertFalse(rule.isMoveOfBlackKingLegal(move))

	def testMoveRuleOfRedMandarin(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 1), Chessman.redMandarin())])
		move = Move((4, 1), (5, 0), Chessman.redMandarin(), None)
		self.assertTrue(rule.isMoveOfRedMandarinLegal(move))
		move = Move((4, 1), (3, 2), Chessman.redMandarin(), None)
		self.assertTrue(rule.isMoveOfRedMandarinLegal(move))
		move = Move((4, 1), (4, 2), Chessman.redMandarin(), None)
		self.assertFalse(rule.isMoveOfRedMandarinLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((3, 2), Chessman.redMandarin())])
		move = Move((3, 2), (2, 1), Chessman.redMandarin(), None)
		self.assertFalse(rule.isMoveOfRedMandarinLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((5, 2), Chessman.redMandarin())])
		move = Move((5, 2), (6, 3), Chessman.redMandarin(), None)
		self.assertFalse(rule.isMoveOfRedMandarinLegal(move))

	def testMoveRuleOfBlackMandarin(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 8), Chessman.blackMandarin())])
		move = Move((4, 8), (5, 9), Chessman.blackMandarin(), None)
		self.assertTrue(rule.isMoveOfBlackMandarinLegal(move))
		move = Move((4, 8), (3, 7), Chessman.blackMandarin(), None)
		self.assertTrue(rule.isMoveOfBlackMandarinLegal(move))
		move = Move((4, 8), (3, 8), Chessman.blackMandarin(), None)
		self.assertFalse(rule.isMoveOfBlackMandarinLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((3, 7), Chessman.blackMandarin())])
		move = Move((3, 7), (4, 6), Chessman.blackMandarin(), None)
		self.assertFalse(rule.isMoveOfBlackMandarinLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((5, 7), Chessman.blackMandarin())])
		move = Move((5, 7), (4, 6), Chessman.blackMandarin(), None)
		self.assertFalse(rule.isMoveOfBlackMandarinLegal(move))

	def testMoveRuleOfRedElephant(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((2, 4), Chessman.redElephant())])
		move = Move((2, 4), (0, 2), Chessman.redElephant(), None)
		self.assertTrue(rule.isMoveOfRedElephantLegal(move))
		move = Move((2, 4), (0, 6), Chessman.redElephant(), None)
		self.assertFalse(rule.isMoveOfRedElephantLegal(move))

	def testMoveRuleOfBlackElephant(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((6, 5), Chessman.blackElephant())])
		move = Move((6, 5), (8, 7), Chessman.blackElephant(), None)
		self.assertTrue(rule.isMoveOfBlackElephantLegal(move))
		move = Move((6, 5), (8, 3), Chessman.blackElephant(), None)
		self.assertFalse(rule.isMoveOfBlackElephantLegal(move))

	def testMoveRuleOfElephantEye(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((6, 5), Chessman.blackElephant())])
		move = Move((6, 5), (8, 7), Chessman.blackElephant(), None)
		self.assertTrue(rule.isMoveOfBlackElephantLegal(move))
		rule.setChessmenOnBoard([
			ChessmanOnBoard((6, 5), Chessman.blackElephant()),
			ChessmanOnBoard((7, 6), Chessman.blackRook())])
		move = Move((6, 5), (8, 7), Chessman.blackElephant(), None)
		self.assertFalse(rule.isMoveOfBlackElephantLegal(move))

	def testMoveRuleOfKnight(self):
		pass

	def testMoveRuleOfRook(self):
		pass

	def testMoveRuleOfCannon(self):
		pass

	def testMoveRuleOfRedPawn(self):
		pass

	def testMoveRuleOfBlackPawn(self):
		pass

	def testKingNotMeet(self):
		pass

	def testSetChessmenOnBoardMultiTimes(self):
		pass

	def testNotChecked(self):
		pass

	# 循环长捉
	def testCircleToEat(self):
		pass

	# 综合考虑走棋是否合法
	def testIsMoveLegal(self):
		pass


if __name__ == '__main__':
	unittest.main()
