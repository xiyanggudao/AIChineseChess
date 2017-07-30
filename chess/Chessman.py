
class Chessman:
	# 类型
	king     = 1
	mandarin = 2
	elephant = 3
	knight   = 4
	rook     = 5
	cannon   = 6
	pawn     = 7

	# 颜色
	red   = 0
	black = 8

	@staticmethod
	def getIdentifier(type, color):
		return type | color

	@staticmethod
	def getType(identifier):
		return identifier & 0x7

	@staticmethod
	def getColor(identifier):
		return identifier & 0x8