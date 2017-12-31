from chess.Chessman import Chessman
import numpy as np

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

def boardImageIds(chessmenOnBoard, active):
	ret = np.empty(len(chessmenOnBoard), np.int32)
	typeIndexMap = {
		Chessman.king: 0,
		Chessman.mandarin: 1,
		Chessman.elephant: 2,
		Chessman.knight: 3,
		Chessman.rook: 4,
		Chessman.cannon: 5,
		Chessman.pawn: 6,
	}
	for i in range(len(chessmenOnBoard)):
		piece = chessmenOnBoard[i]
		if active == piece.color:
			offset = 0
		else:
			offset = 7
		typeIndex = offset+typeIndexMap[piece.type]
		id = typeIndex*90+piece.y*9+piece.x
		ret[i] = id
	return ret

def imageIdToIndex(id):
	h = id//90
	y = id%90//9
	x = id%9
	return (x, y, h)

def initMoveToIdMap(moveToIdMap):
	moveToIdMap.fill(-1)
	id = 0
	# 纵横
	for fx in range(9):
		for fy in range(10):
			for tx in range(9):
				if fx != tx:
					assert moveToIdMap[fx,fy,tx,fy] == -1
					moveToIdMap[fx,fy,tx,fy] = id
					id += 1
			for ty in range(10):
				if fy != ty:
					assert moveToIdMap[fx,fy,fx,ty] == -1
					moveToIdMap[fx,fy,fx,ty] = id
					id += 1
	# 马
	kightPath = ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1))
	for fx in range(9):
		for fy in range(10):
			for path in kightPath:
				tx = fx + path[0]
				ty = fy + path[1]
				if 0 <= tx < 9 and 0 <= ty < 10:
					assert moveToIdMap[fx, fy, tx, ty] == -1
					moveToIdMap[fx, fy, tx, ty] = id
					id += 1
	# 象
	elephantPath = (
		(2,0,0,2),(2,0,4,2),(0,2,2,0),(0,2,2,4),
		(2,4,0,2),(2,4,4,2),(6,4,4,2),(6,4,8,2),
		(8,2,6,4),(8,2,6,0),(6,0,8,2),(6,0,4,2),
		(4,2,6,0),(4,2,2,0),(4,2,2,4),(4,2,6,4)
	)
	for path in elephantPath:
		fx, fy, tx, ty = path
		assert abs(fx-tx) == 2
		assert abs(fy-ty) == 2
		assert moveToIdMap[fx, fy, tx, ty] == -1
		assert moveToIdMap[8-fx, 9-fy, 8-tx, 9-ty] == -1
		moveToIdMap[fx, fy, tx, ty] = id
		moveToIdMap[8-fx, 9-fy, 8-tx, 9-ty] = id
		id += 1
	# 士
	mandarinPath = (
		(4, 1, 3, 0), (4, 1, 5, 0), (4, 1, 3, 2), (4, 1, 5, 2),
		(3, 0, 4, 1), (5, 0, 4, 1), (3, 2, 4, 1), (5, 2, 4, 1)
	)
	for path in mandarinPath:
		fx, fy, tx, ty = path
		assert abs(fx-tx) == 1
		assert abs(fy-ty) == 1
		assert moveToIdMap[fx, fy, tx, ty] == -1
		assert moveToIdMap[8-fx, 9-fy, 8-tx, 9-ty] == -1
		moveToIdMap[fx, fy, tx, ty] = id
		moveToIdMap[8-fx, 9-fy, 8-tx, 9-ty] = id
		id += 1
	assert id == 2062

moveToIdMap = np.empty((9,10,9,10),np.int32)
initMoveToIdMap(moveToIdMap)
def moveFeatureId2(fromPos, toPos):
	id = moveToIdMap[fromPos[0],fromPos[1],toPos[0],toPos[1]]
	assert id != -1
	return id

def outputProbability2(moves, outputFeature):
	probability = []
	for move in moves:
		id = moveFeatureId2(move.fromPos, move.toPos)
		probability.append(outputFeature[id])
	totalProbability = sum(probability)
	totalProbability2 = sum(outputFeature)

	assert abs(totalProbability - totalProbability2) < 1e-6
	assert abs(totalProbability - 1) < 1e-6

	return probability