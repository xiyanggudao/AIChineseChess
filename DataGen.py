from chess.Chessgame import Chessgame
from brain.MoveProbability import MoveProbability
from chess.MoveGenerator import MoveGenerator
from brain.UcciBrain import UcciBrain
import random
import time

brains = [
	UcciBrain('./ucci/bhws/Binghewusi.exe'),
	UcciBrain('./ucci/blcx/BLCX056.EXE'),
	UcciBrain('./ucci/eychessu/EYCHESSU.EXE'),
	UcciBrain('./ucci/hice/HICE.EXE'),
	UcciBrain('./ucci/jupiter/JUPITER.EXE'),
	UcciBrain('./ucci/king/King.exe'),
	UcciBrain('./ucci/mars/MARS.EXE'),
	UcciBrain('./ucci/nymphchess/EYE.EXE'),
	UcciBrain('./ucci/qstar/qst.exe'),
	UcciBrain('./ucci/sixteeners/sixteen.exe'),
	UcciBrain('./ucci/swallow/swallow.exe'),
	UcciBrain('./ucci/tht/THT.EXE'),
	UcciBrain('./ucci/tlxj/TLXJ.EXE'),
	UcciBrain('./ucci/xqcyclone/cyclone.exe'),
	UcciBrain('./ucci/xqspirit/XQSPIRIT.EXE'),
	UcciBrain('./ucci/xqwizard/ELEEYE.EXE'),
	UcciBrain('./ucci/yssy/YSSY.EXE'),
]

def play(red, black):
	pass

for i in range(10000):
	redIndex = random.randint(0, len(brains) - 1)
	blackIndex = random.randint(0, len(brains) - 1)

	redDepth = random.randint(5, 11)
	blackDepth = random.randint(5, 11)
	brains[redIndex].setDepth(redDepth)
	brains[blackIndex].setDepth(blackDepth)

	play(brains[redIndex], brains[blackIndex])
