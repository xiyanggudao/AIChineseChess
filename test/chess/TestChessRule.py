import unittest
from chess.ChessRule import ChessRule
from chess.Chessgame import Chessgame
from chess.ChessData import Move
from chess.ChessData import ChessmanOnBoard
from chess.Chessman import Chessman


class TestChessRule(unittest.TestCase):

	def testPositionRange(self):
		rule = ChessRule()
		move = Move((1, 2), (4, 2), Chessman.invalid(), Chessman.invalid())
		self.assertTrue(rule.isPositionRangeLegal(move))
		move = Move((0, 0), (8, 9), Chessman.invalid(), Chessman.invalid())
		self.assertTrue(rule.isPositionRangeLegal(move))
		move = Move((0, -1), (4, 2), Chessman.invalid(), Chessman.invalid())
		self.assertFalse(rule.isPositionRangeLegal(move))
		move = Move((0, 2), (-1, 2), Chessman.invalid(), Chessman.invalid())
		self.assertFalse(rule.isPositionRangeLegal(move))
		move = Move((9, 2), (4, 2), Chessman.invalid(), Chessman.invalid())
		self.assertFalse(rule.isPositionRangeLegal(move))
		move = Move((0, 2), (4, 10), Chessman.invalid(), Chessman.invalid())
		self.assertFalse(rule.isPositionRangeLegal(move))

	def testMoveToOrigin(self):
		rule = ChessRule()
		move = Move((1, 2), (1, 2), Chessman.invalid(), Chessman.invalid())
		self.assertFalse(rule.isPositionRangeLegal(move))

	def testIsMoveConformToChessboard(self):
		game = Chessgame()
		rule = ChessRule()
		rule.setBoard(game.board())
		rule.setActiveColor(game.activeColor())
		move = Move((1, 2), (4, 2), Chessman.redCannon(), Chessman.invalid())
		self.assertTrue(rule.isMoveConformToChessboard(move))
		move = Move((1, 2), (1, 9), Chessman.redCannon(), Chessman.blackKnight())
		self.assertTrue(rule.isMoveConformToChessboard(move))
		move = Move((1, 2), (4, 2), Chessman.invalid(), Chessman.invalid())
		self.assertFalse(rule.isMoveConformToChessboard(move))
		move = Move((1, 2), (4, 2), Chessman.redCannon(), Chessman.blackCannon())
		self.assertFalse(rule.isMoveConformToChessboard(move))

	def testMoveActiveColorChessman(self):
		game = Chessgame()
		rule = ChessRule()
		rule.setBoard(game.board())
		rule.setActiveColor(game.activeColor())
		move = Move((1, 2), (4, 2), Chessman.redCannon(), Chessman.invalid())
		self.assertTrue(rule.isMoveRightColor(move))
		move = Move((1, 7), (4, 7), Chessman.blackCannon(), Chessman.invalid())
		self.assertFalse(rule.isMoveRightColor(move))

	def testNotEatSelf(self):
		game = Chessgame()
		rule = ChessRule()
		rule.setBoard(game.board())
		rule.setActiveColor(game.activeColor())
		move = Move((0, 0), (0, 3), Chessman.redRook(), Chessman.redPawn())
		self.assertTrue(rule.isEatSelf(move))
		move = Move((0, 0), (0, 1), Chessman.redRook(), Chessman.invalid())
		self.assertFalse(rule.isEatSelf(move))

	def testMoveRuleOfRedKing(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 1), Chessman.redKing())])
		move = Move((4, 1), (3, 1), Chessman.redKing(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfRedKingLegal(move))
		move = Move((4, 1), (4, 2), Chessman.redKing(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfRedKingLegal(move))
		move = Move((4, 1), (5, 2), Chessman.redKing(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfRedKingLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((5, 1), Chessman.redKing())])
		move = Move((5, 1), (6, 1), Chessman.redKing(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfRedKingLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 2), Chessman.redKing())])
		move = Move((4, 2), (4, 3), Chessman.redKing(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfRedKingLegal(move))

	def testMoveRuleOfBlackKing(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 8), Chessman.blackKing())])
		move = Move((4, 8), (3, 8), Chessman.blackKing(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfBlackKingLegal(move))
		move = Move((4, 8), (4, 9), Chessman.blackKing(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfBlackKingLegal(move))
		move = Move((4, 8), (5, 9), Chessman.blackKing(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfBlackKingLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((5, 8), Chessman.blackKing())])
		move = Move((5, 8), (6, 8), Chessman.blackKing(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfBlackKingLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 9), Chessman.blackKing())])
		move = Move((4, 9), (4, 10), Chessman.blackKing(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfBlackKingLegal(move))

	def testKingToKing(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([
			ChessmanOnBoard((4, 0), Chessman.redKing()),
			ChessmanOnBoard((4, 9), Chessman.blackKing())])
		move = Move((4, 0), (4, 9), Chessman.redKing(), Chessman.blackKing())
		self.assertTrue(rule.isMoveOfRedKingLegal(move))
		move = Move((4, 9), (4, 0), Chessman.blackKing(), Chessman.redKing())
		self.assertTrue(rule.isMoveOfBlackKingLegal(move))

		rule.setChessmenOnBoard([
			ChessmanOnBoard((4, 0), Chessman.redKing()),
			ChessmanOnBoard((4, 9), Chessman.blackKing()),
			ChessmanOnBoard((4, 5), Chessman.redCannon())])
		move = Move((4, 0), (4, 9), Chessman.redKing(), Chessman.blackKing())
		self.assertFalse(rule.isMoveOfRedKingLegal(move))
		move = Move((4, 9), (4, 0), Chessman.blackKing(), Chessman.redKing())
		self.assertFalse(rule.isMoveOfBlackKingLegal(move))

	def testMoveRuleOfRedMandarin(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 1), Chessman.redMandarin())])
		move = Move((4, 1), (5, 0), Chessman.redMandarin(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfRedMandarinLegal(move))
		move = Move((4, 1), (3, 2), Chessman.redMandarin(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfRedMandarinLegal(move))
		move = Move((4, 1), (4, 2), Chessman.redMandarin(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfRedMandarinLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((3, 2), Chessman.redMandarin())])
		move = Move((3, 2), (2, 1), Chessman.redMandarin(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfRedMandarinLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((5, 2), Chessman.redMandarin())])
		move = Move((5, 2), (6, 3), Chessman.redMandarin(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfRedMandarinLegal(move))

	def testMoveRuleOfBlackMandarin(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 8), Chessman.blackMandarin())])
		move = Move((4, 8), (5, 9), Chessman.blackMandarin(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfBlackMandarinLegal(move))
		move = Move((4, 8), (3, 7), Chessman.blackMandarin(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfBlackMandarinLegal(move))
		move = Move((4, 8), (3, 8), Chessman.blackMandarin(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfBlackMandarinLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((3, 7), Chessman.blackMandarin())])
		move = Move((3, 7), (4, 6), Chessman.blackMandarin(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfBlackMandarinLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((5, 7), Chessman.blackMandarin())])
		move = Move((5, 7), (4, 6), Chessman.blackMandarin(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfBlackMandarinLegal(move))

	def testMoveRuleOfRedElephant(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((2, 4), Chessman.redElephant())])
		move = Move((2, 4), (0, 2), Chessman.redElephant(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfRedElephantLegal(move))
		move = Move((2, 4), (0, 6), Chessman.redElephant(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfRedElephantLegal(move))

	def testMoveRuleOfBlackElephant(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((6, 5), Chessman.blackElephant())])
		move = Move((6, 5), (8, 7), Chessman.blackElephant(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfBlackElephantLegal(move))
		move = Move((6, 5), (8, 3), Chessman.blackElephant(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfBlackElephantLegal(move))

	def testMoveRuleOfElephantEye(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((6, 5), Chessman.blackElephant())])
		move = Move((6, 5), (8, 7), Chessman.blackElephant(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfBlackElephantLegal(move))
		rule.setChessmenOnBoard([
			ChessmanOnBoard((6, 5), Chessman.blackElephant()),
			ChessmanOnBoard((7, 6), Chessman.blackRook())])
		move = Move((6, 5), (8, 7), Chessman.blackElephant(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfBlackElephantLegal(move))

	def testMoveRuleOfKnight(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((2, 2), Chessman.redKnight())])
		move = Move((2, 2), (1, 0), Chessman.redKnight(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfKnightLegal(move))

	def testMoveRuleOfKnightFoot(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([
			ChessmanOnBoard((2, 2), Chessman.redKnight()),
			ChessmanOnBoard((2, 1), Chessman.redKnight())])
		move = Move((2, 2), (1, 0), Chessman.redKnight(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfKnightLegal(move))

	def testMoveRuleOfRook(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([
			ChessmanOnBoard((0, 0), Chessman.redRook()),
			ChessmanOnBoard((5, 0), Chessman.redKnight()),
			ChessmanOnBoard((0, 6), Chessman.redKnight())])
		move = Move((0, 0), (6, 0), Chessman.redRook(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfRookLegal(move))
		move = Move((0, 0), (0, 7), Chessman.redRook(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfRookLegal(move))
		move = Move((0, 0), (5, 0), Chessman.redRook(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfRookLegal(move))
		move = Move((0, 0), (0, 6), Chessman.redRook(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfRookLegal(move))
		move = Move((0, 0), (1, 6), Chessman.redRook(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfRookLegal(move))

	def testMoveRuleOfCannon(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([
			ChessmanOnBoard((0, 0), Chessman.redCannon()),
			ChessmanOnBoard((5, 0), Chessman.redKnight()),
			ChessmanOnBoard((0, 6), Chessman.redKnight()),
			ChessmanOnBoard((0, 7), Chessman.blackKnight())])
		move = Move((0, 0), (6, 0), Chessman.redCannon(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfCannonLegal(move))
		move = Move((0, 0), (0, 7), Chessman.redCannon(), Chessman.blackKnight())
		self.assertTrue(rule.isMoveOfCannonLegal(move))
		move = Move((0, 0), (5, 0), Chessman.redCannon(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfCannonLegal(move))
		move = Move((0, 0), (0, 5), Chessman.redCannon(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfCannonLegal(move))
		move = Move((0, 0), (1, 6), Chessman.redCannon(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfCannonLegal(move))

	def testMoveRuleOfRedPawn(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((2, 3), Chessman.redPawn())])
		move = Move((2, 3), (2, 4), Chessman.redPawn(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfRedPawnLegal(move))
		move = Move((2, 3), (1, 3), Chessman.redPawn(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfRedPawnLegal(move))

		rule.setChessmenOnBoard([ChessmanOnBoard((2, 5), Chessman.redPawn())])
		move = Move((2, 5), (1, 5), Chessman.redPawn(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfRedPawnLegal(move))

	def testMoveRuleOfBlackPawn(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((2, 6), Chessman.blackPawn())])
		move = Move((2, 6), (2, 5), Chessman.blackPawn(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfBlackPawnLegal(move))
		move = Move((2, 6), (1, 6), Chessman.blackPawn(), Chessman.invalid())
		self.assertFalse(rule.isMoveOfBlackPawnLegal(move))

		rule.setChessmenOnBoard([ChessmanOnBoard((2, 5), Chessman.blackPawn())])
		move = Move((2, 4), (1, 4), Chessman.blackPawn(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfBlackPawnLegal(move))

	def testSetChessmenOnBoardMultiTimes(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((7, 6), Chessman.blackRook())])
		rule.setChessmenOnBoard([ChessmanOnBoard((6, 5), Chessman.blackElephant())])
		move = Move((6, 5), (8, 7), Chessman.blackElephant(), Chessman.invalid())
		self.assertTrue(rule.isMoveOfBlackElephantLegal(move))

	def testNotCheckedAfterMove(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([
			ChessmanOnBoard((4, 0), Chessman.redKing()),
			ChessmanOnBoard((4, 9), Chessman.blackKing()),
			ChessmanOnBoard((4, 5), Chessman.redCannon())])
		move = Move((4, 5), (0, 5), Chessman.redCannon(), Chessman.invalid())
		self.assertTrue(rule.isCheckedAfterMove(move))
		move = Move((4, 5), (4, 7), Chessman.redCannon(), Chessman.invalid())
		self.assertFalse(rule.isCheckedAfterMove(move))

	def testKingNotMeet(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([
			ChessmanOnBoard((4, 0), Chessman.redKing()),
			ChessmanOnBoard((5, 9), Chessman.blackKing())
		])
		move = Move((4, 0), (5, 0), Chessman.redKing(), Chessman.invalid())
		self.assertTrue(rule.isCheckedAfterMove(move))
		self.assertFalse(rule.isMoveLegal(move))

	# 长将：凡走子连续不停照将，而形成循环者，称为“长将”
	def testPerpetualCheck(self):
		pass

	# 长捉：凡走子连续追捉一子或数子，而形成循环者，称为“长捉”
	def testPerpetualChase(self):
		pass

	# 长杀：凡走子连续不停叫杀，而形成循环者，称为“长杀”
	def testPerpetualCheckmateThreat(self):
		pass

	# 一将一杀：凡走出一步将军而下一步将要被杀棋，待被将军的一方为了解杀也同样走一将一杀的着，
	# 前者需变着，否则被判负
	def testCheckAndCheckmateThreat(self):
		pass

	# 一将一捉：是指凡单个子力或多个子力循环将军又循环捉子且将不死又捉不到的着法，棋规是不允许的
	def testCheckAndChase(self):
		pass

	# 综合考虑走棋是否合法
	def testIsMoveLegal(self):
		pass


if __name__ == '__main__':
	unittest.main()
