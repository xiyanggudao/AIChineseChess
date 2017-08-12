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
		move = Move((1, 2), (4, 2), Chessman.identifier(Chessman.cannon, Chessman.red), None)
		self.assertTrue(rule.isMoveConformToChessboard(move))
		move = Move((1, 2), (4, 2), None, None)
		self.assertFalse(rule.isMoveConformToChessboard(move))
		move = Move((1, 2), (4, 2), Chessman.identifier(Chessman.cannon, Chessman.red), Chessman.identifier(Chessman.cannon, Chessman.black))
		self.assertFalse(rule.isMoveConformToChessboard(move))

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
		move = Move((0, 0), (0, 3), Chessman.identifier(Chessman.rook, Chessman.red), Chessman.identifier(Chessman.pawn, Chessman.red))
		self.assertTrue(rule.isEatSelf(move))
		move = Move((0, 0), (0, 1), Chessman.identifier(Chessman.rook, Chessman.red), None)
		self.assertFalse(rule.isEatSelf(move))

	def testMoveRuleOfRedKing(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 1), Chessman.identifier(Chessman.king, Chessman.red))])
		move = Move((4, 1), (3, 1), Chessman.identifier(Chessman.king, Chessman.red), None)
		self.assertTrue(rule.isMoveOfRedKingLegal(move))
		move = Move((4, 1), (4, 2), Chessman.identifier(Chessman.king, Chessman.red), None)
		self.assertTrue(rule.isMoveOfRedKingLegal(move))
		move = Move((4, 1), (5, 2), Chessman.identifier(Chessman.king, Chessman.red), None)
		self.assertFalse(rule.isMoveOfRedKingLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((5, 1), Chessman.identifier(Chessman.king, Chessman.red))])
		move = Move((5, 1), (6, 1), Chessman.identifier(Chessman.king, Chessman.red), None)
		self.assertFalse(rule.isMoveOfRedKingLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 2), Chessman.identifier(Chessman.king, Chessman.red))])
		move = Move((4, 2), (4, 3), Chessman.identifier(Chessman.king, Chessman.red), None)
		self.assertFalse(rule.isMoveOfRedKingLegal(move))

	def testMoveRuleOfBlackKing(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 8), Chessman.identifier(Chessman.king, Chessman.black))])
		move = Move((4, 8), (3, 8), Chessman.identifier(Chessman.king, Chessman.black), None)
		self.assertTrue(rule.isMoveOfBlackKingLegal(move))
		move = Move((4, 8), (4, 9), Chessman.identifier(Chessman.king, Chessman.black), None)
		self.assertTrue(rule.isMoveOfBlackKingLegal(move))
		move = Move((4, 8), (5, 9), Chessman.identifier(Chessman.king, Chessman.black), None)
		self.assertFalse(rule.isMoveOfBlackKingLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((5, 8), Chessman.identifier(Chessman.king, Chessman.black))])
		move = Move((5, 8), (6, 8), Chessman.identifier(Chessman.king, Chessman.black), None)
		self.assertFalse(rule.isMoveOfBlackKingLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 9), Chessman.identifier(Chessman.king, Chessman.black))])
		move = Move((4, 9), (4, 10), Chessman.identifier(Chessman.king, Chessman.black), None)
		self.assertFalse(rule.isMoveOfBlackKingLegal(move))

	def testMoveRuleOfRedMandarin(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 1), Chessman.identifier(Chessman.mandarin, Chessman.red))])
		move = Move((4, 1), (5, 0), Chessman.identifier(Chessman.mandarin, Chessman.red), None)
		self.assertTrue(rule.isMoveOfRedMandarinLegal(move))
		move = Move((4, 1), (3, 2), Chessman.identifier(Chessman.mandarin, Chessman.red), None)
		self.assertTrue(rule.isMoveOfRedMandarinLegal(move))
		move = Move((4, 1), (4, 2), Chessman.identifier(Chessman.mandarin, Chessman.red), None)
		self.assertFalse(rule.isMoveOfRedMandarinLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((3, 2), Chessman.identifier(Chessman.mandarin, Chessman.red))])
		move = Move((3, 2), (2, 1), Chessman.identifier(Chessman.mandarin, Chessman.red), None)
		self.assertFalse(rule.isMoveOfRedMandarinLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((5, 2), Chessman.identifier(Chessman.mandarin, Chessman.red))])
		move = Move((5, 2), (6, 3), Chessman.identifier(Chessman.mandarin, Chessman.red), None)
		self.assertFalse(rule.isMoveOfRedMandarinLegal(move))

	def testMoveRuleOfBlackMandarin(self):
		rule = ChessRule()
		rule.setChessmenOnBoard([ChessmanOnBoard((4, 8), Chessman.identifier(Chessman.mandarin, Chessman.black))])
		move = Move((4, 8), (5, 9), Chessman.identifier(Chessman.mandarin, Chessman.black), None)
		self.assertTrue(rule.isMoveOfBlackMandarinLegal(move))
		move = Move((4, 8), (3, 7), Chessman.identifier(Chessman.mandarin, Chessman.black), None)
		self.assertTrue(rule.isMoveOfBlackMandarinLegal(move))
		move = Move((4, 8), (3, 8), Chessman.identifier(Chessman.mandarin, Chessman.black), None)
		self.assertFalse(rule.isMoveOfBlackMandarinLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((3, 7), Chessman.identifier(Chessman.mandarin, Chessman.black))])
		move = Move((3, 7), (4, 6), Chessman.identifier(Chessman.mandarin, Chessman.black), None)
		self.assertFalse(rule.isMoveOfBlackMandarinLegal(move))
		rule.setChessmenOnBoard([ChessmanOnBoard((5, 7), Chessman.identifier(Chessman.mandarin, Chessman.black))])
		move = Move((5, 7), (4, 6), Chessman.identifier(Chessman.mandarin, Chessman.black), None)
		self.assertFalse(rule.isMoveOfBlackMandarinLegal(move))

	def testMoveRuleOfRedElephant(self):
		pass

	def testMoveRuleOfBlackElephant(self):
		pass

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
