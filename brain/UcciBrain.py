import subprocess
from chess.ChessData import Move
from threading import Timer

class UcciBrain:

	def __init__(self, path):
		self.setDepth(7)
		self.__process = subprocess.Popen(
			[path],
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE
		)
		self.sendCommand('ucci\n')
		self.getResult('ucciok')

	def __del__(self):
		self.sendCommand('quit\n')

	def setDepth(self, depth):
		self.__levelCommand = 'go depth '+str(depth)+'\n'

	def sendCommand(self, commandStr):
		self.__process.stdin.write(commandStr.encode())
		self.__process.stdin.flush()

	def getResult(self, keyword):
		while True:
			kill = lambda process: process.kill()
			my_timer = Timer(60, kill, [self.__process])
			try:
				my_timer.start()
				out = self.__process.stdout.readline()
			finally:
				my_timer.cancel()

			if self.__process.poll():
				raise Exception('get result of subprocess failed')
			outStr = out.decode(encoding='utf-8', errors='ignore')
			#print(outStr, end='')
			if outStr.find(keyword) != -1:
				#print('---------')
				return outStr

	def positionCommand(self, game):
		commandStr = 'position startpos'
		for i in range(game.moveSize()):
			if i == 0:
				commandStr += ' moves'
			move = game.moveAt(i)
			commandStr = commandStr + ' '+move.ucciStr()
		return commandStr + '\n'

	def generate(self, game, moves):
		self.sendCommand(self.positionCommand(game))
		self.sendCommand(self.__levelCommand)
		bestMoveKey = 'bestmove'
		bestMoveLine = self.getResult(bestMoveKey)
		if bestMoveLine.startswith('nobestmove') or bestMoveLine.find('resign') != -1:
			average = 1./len(moves)
			return [average for i in range(len(moves))]

		assert bestMoveLine.startswith(bestMoveKey)

		bestMoveStr = bestMoveLine[len(bestMoveKey)+1:len(bestMoveKey)+5]
		#print(bestMoveStr)
		fx = ord(bestMoveStr[0])-ord('a')
		fy = ord(bestMoveStr[1])-ord('0')
		tx = ord(bestMoveStr[2])-ord('a')
		ty = ord(bestMoveStr[3])-ord('0')
		if not (0 <= fx <= 8 and 0 <= tx <= 8 and 0 <= fy <= 9 and 0 <= ty <= 9):
			raise Exception('unknown best move ', bestMoveLine)
		move = Move((fx, fy), (tx, ty), game.chessmanAt((fx, fy)), game.chessmanAt((tx, ty)))

		probability = [0 for i in range(len(moves))]
		probability[moves.index(move)] = 1.

		return probability
