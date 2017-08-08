
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
	def identifier(type, color):
		return type | color

	@staticmethod
	def type(identifier):
		return identifier & 0x7

	@staticmethod
	def color(identifier):
		return identifier & 0x8

	@staticmethod
	def oppositeColor(color):
		return color ^ 0x8

	@staticmethod
	def text(identifier):
		allText = [
			'空','帥','仕','相','馬','車','砲','兵',
			'空','將','士','象','馬','車','炮','卒'
		]
		return allText[identifier]