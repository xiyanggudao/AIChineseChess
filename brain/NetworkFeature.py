from chess.Chessman import Chessman

def chessmanFeatureId(type, color, position, active):
	if color == active:
		offset = 0
	else:
		offset = 9 + 5 + 7 + 90 * 3 + 55

	if color == Chessman.red:
		x, y = position
	else:
		assert color == Chessman.black
		x, y = 8 - position[0], 9 - position[1]

	if type == Chessman.king:
		id = y * 3 + x - 3
	elif type == Chessman.mandarin:
		offset += 9
		id = (x + y - 3) // 2 + y
	elif type == Chessman.elephant:
		offset += 9 + 5
		id = (x + y) // 4 + y
	elif type == Chessman.knight:
		offset += 9 + 5 + 7
		id = y * 9 + x
	elif type == Chessman.rook:
		offset += 9 + 5 + 7 + 90
		id = y * 9 + x
	elif type == Chessman.cannon:
		offset += 9 + 5 + 7 + 90 * 2
		id = y * 9 + x
	elif type == Chessman.pawn:
		offset += 9 + 5 + 7 + 90 * 3
		if y < 5:
			id = (y - 3) * 5 + x // 2
		else:
			id = (y - 5) * 9 + x + 10
	else:
		assert False

	return offset + id

def moveFeatureId(type, color, fromPos, toPos, active):
	assert color == active
	if color == Chessman.red:
		fx, fy = fromPos
		tx, ty = toPos
	else:
		assert color == Chessman.black
		fx, fy = 8 - fromPos[0], 9 - fromPos[1]
		tx, ty = 8 - toPos[0], 9 - toPos[1]
	dx, dy = tx-fx, ty-fy

	if type == Chessman.king:
		offset = 0
		posId = fy*3 + fx-3
		ids = [0, 1, None, 2, 3]
		moveId = ids[2*dx + dy + 2]
		moveCnt = 4
	elif type == Chessman.mandarin:
		offset = 9*4
		posId = [0,None,1,2,3,None,4][2*(fx-3) + fy]
		moveId = dx + (dy+3)//2
		moveCnt = 4
	elif type == Chessman.elephant:
		offset = 9*4+5*4
		posId = [0,1,None,2,3,4,None,5,6][fx+fy//2-1]
		moveId = dx//2 + (dy//2 + 3) // 2
		moveCnt = 4
	elif type == Chessman.knight:
		offset = 9*4+5*4+7*4
		posId = fy*9+fx
		ids = [
			0, None, 1, 2, None, None, None, 3,
			None, None, None,
			4, None, None, None, 5, 6, None, 7
		]
		moveId = ids[4*dx+dy+9]
		moveCnt = 8
	elif type == Chessman.rook:
		offset = 9*4+5*4+7*4+90*8
		posId = fy*9 + fx
		if dy == 0:
			moveId = tx
		else:
			assert dx == 0
			if dy > 0:
				moveId = ty+8
			else:
				moveId = ty+9
		moveCnt = 18
	elif type == Chessman.cannon:
		offset = 9*4+5*4+7*4+90*8+90*18
		posId = fy*9 + fx
		if dy == 0:
			moveId = tx
		else:
			assert dx == 0
			if dy > 0:
				moveId = ty+8
			else:
				moveId = ty+9
		moveCnt = 18
	elif type == Chessman.pawn:
		offset = 9*4+5*4+7*4+90*8+90*18*2
		if fy < 5:
			posId = (fy-3)*5+fx//2
		else:
			posId = (fy-5)*9+fx+10
		moveId = dx + 1
		moveCnt = 3
	else:
		assert False

	assert posId >= 0
	assert moveId >= 0
	return offset + posId*moveCnt + moveId

def inputFeature(chessmenOnBoard, moves):
	active = Chessman.color(moves[0].moveChessman)

	boardFeature = [0 for i in range((9+5+7+90*3+55)*2)]
	for piece in chessmenOnBoard:
		id = chessmanFeatureId(piece.type, piece.color, piece.position, active)
		assert boardFeature[id] == 0
		boardFeature[id] = 1

	moveFeature = [0 for i in range(9*4+5*4+7*4+90*8+90*18*2+55*3)]
	for move in moves:
		type = Chessman.type(move.moveChessman)
		color = Chessman.color(move.moveChessman)
		id = moveFeatureId(type, color, move.fromPos, move.toPos, active)
		assert moveFeature[id] == 0
		moveFeature[id] = 1

	return (boardFeature, moveFeature)

def outputProbability(moves, outputFeature):
	probability = []
	active = Chessman.color(moves[0].moveChessman)
	for move in moves:
		type = Chessman.type(move.moveChessman)
		color = Chessman.color(move.moveChessman)
		id = moveFeatureId(type, color, move.fromPos, move.toPos, active)
		probability.append(outputFeature[id])
	totalProbability = sum(probability)
	totalProbability2 = sum(outputFeature)

	assert abs(totalProbability - totalProbability2) < 0.000001

	return probability
