
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
	def invalid():
		return 0

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
	def redKing():
		return Chessman.identifier(Chessman.king, Chessman.red)

	@staticmethod
	def redMandarin():
		return Chessman.identifier(Chessman.mandarin, Chessman.red)

	@staticmethod
	def redElephant():
		return Chessman.identifier(Chessman.elephant, Chessman.red)

	@staticmethod
	def redKnight():
		return Chessman.identifier(Chessman.knight, Chessman.red)

	@staticmethod
	def redRook():
		return Chessman.identifier(Chessman.rook, Chessman.red)

	@staticmethod
	def redCannon():
		return Chessman.identifier(Chessman.cannon, Chessman.red)

	@staticmethod
	def redPawn():
		return Chessman.identifier(Chessman.pawn, Chessman.red)

	@staticmethod
	def blackKing():
		return Chessman.identifier(Chessman.king, Chessman.black)

	@staticmethod
	def blackMandarin():
		return Chessman.identifier(Chessman.mandarin, Chessman.black)

	@staticmethod
	def blackElephant():
		return Chessman.identifier(Chessman.elephant, Chessman.black)

	@staticmethod
	def blackKnight():
		return Chessman.identifier(Chessman.knight, Chessman.black)

	@staticmethod
	def blackRook():
		return Chessman.identifier(Chessman.rook, Chessman.black)

	@staticmethod
	def blackCannon():
		return Chessman.identifier(Chessman.cannon, Chessman.black)

	@staticmethod
	def blackPawn():
		return Chessman.identifier(Chessman.pawn, Chessman.black)

	@staticmethod
	def text(identifier):
		if identifier == None:
			identifier = Chessman.invalid()
		allText = [
			'空','帥','仕','相','馬','車','砲','兵',
			'空','將','士','象','馬','車','炮','卒'
		]
		return allText[identifier]