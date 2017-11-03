import subprocess
from chess.ChessData import Move

class UcciBrain:

	def __init__(self):
		self.__process = subprocess.Popen(
			['./xqwizard/ELEEYE.EXE'],
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE
		)
		self.sendCommand('ucci\n')
		self.getResult('ucciok')

	def __del__(self):
		self.sendCommand('quit\n')

	def sendCommand(self, commandStr):
		self.__process.stdin.write(commandStr.encode())
		self.__process.stdin.flush()

	def getResult(self, keyword):
		while True:
			out = self.__process.stdout.readline()
			outStr = out.decode()
			#print(outStr, end='')
			if outStr.find(keyword) != -1:
				return outStr

	def positionCommand(self, game):
		commandStr = 'position startpos moves'
		for i in range(game.moveSize()):
			move = game.moveAt(i)
			commandStr = commandStr + ' '+move.ucciStr()
		return commandStr + '\n'

	def generate(self, game, moves):
		self.sendCommand(self.positionCommand(game))
		self.sendCommand('go depth 7\n')
		bestMoveKey = 'bestmove '
		bestMoveLine = self.getResult(bestMoveKey)
		assert bestMoveLine.startswith(bestMoveKey)

		bestMoveStr = bestMoveLine[len(bestMoveKey):len(bestMoveKey)+4]
		#print(bestMoveStr)
		fx = ord(bestMoveStr[0])-ord('a')
		fy = ord(bestMoveStr[1])-ord('0')
		tx = ord(bestMoveStr[2])-ord('a')
		ty = ord(bestMoveStr[3])-ord('0')
		move = Move((fx, fy), (tx, ty), game.chessmanAt((fx, fy)), game.chessmanAt((tx, ty)))

		probability = [0 for i in range(len(moves))]
		probability[moves.index(move)] = 1.

		return probability
