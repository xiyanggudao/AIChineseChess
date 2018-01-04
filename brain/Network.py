import tensorflow as tf
import os
import time
import brain.NetworkFeature as nf
from chess.Chessman import Chessman
import numpy as np


def batchNormalization(x):
	mean, variance = tf.nn.moments(x, [0])
	return tf.nn.batch_normalization(x, mean, variance, 0, 1, 1e-8)

def addLayer(x, in_channels, out_channels, kSize = 3):
	w1 = tf.Variable(tf.truncated_normal([kSize, kSize, in_channels, out_channels], 0., 0.1))
	b1 = tf.Variable(tf.truncated_normal([out_channels], 0.1, 0.05))
	z1 = tf.nn.conv2d(x, w1, strides=[1, 1, 1, 1], padding='SAME')
	norm1 = batchNormalization(z1) + b1
	y = tf.nn.relu(norm1)
	if in_channels == out_channels:
		w2 = tf.Variable(tf.truncated_normal([kSize, kSize, in_channels, out_channels], 0., 0.1))
		b2 = tf.Variable(tf.truncated_normal([out_channels], 0.1, 0.05))
		z2 = tf.nn.conv2d(y, w2, strides=[1, 1, 1, 1], padding='SAME') + x
		norm2 = batchNormalization(z2) + b2
		y = tf.nn.relu(norm2)
	return y


def pickySoftmax(x, inputSize, outputSize, pickySwitch):
	w = tf.Variable(tf.truncated_normal([inputSize, outputSize], 0, 0.1))
	b = tf.Variable(tf.truncated_normal([1, outputSize], 0.1, 0.05))
	z = tf.matmul(x, w)
	norm = batchNormalization(z) + b
	# softmax[i] = exp(input[i]) / sum(exp(input))
	# pickySoftmax[i] = pickySwitch[i]*exp(input[i]) / sum(pickySwitch*exp(input))
	expVal = tf.exp(norm) * pickySwitch
	y = expVal / tf.reduce_sum(expVal, 1, keep_dims=True)
	return y

class Network:

	def __init__(self, initPath):
		g = tf.Graph()
		with g.as_default():
			boardInput = tf.placeholder(tf.float32, [None, 9, 10, 14])
			moveInput = tf.placeholder(tf.float32, [None, 2062])
			l1 = addLayer(boardInput, 14, 128)
			l1 = addLayer(l1, 128, 128)
			l1 = addLayer(l1, 128, 128)
			l1 = addLayer(l1, 128, 128)
			l1 = addLayer(l1, 128, 128)
			l1 = addLayer(l1, 128, 128)
			l1 = addLayer(l1, 128, 128)
			l1 = addLayer(l1, 128, 128)
			l1 = addLayer(l1, 128, 128)
			l1 = addLayer(l1, 128, 24, 1)
			flat = tf.reshape(l1, [-1, 9*10*24])
			output = pickySoftmax(flat, 9*10*24, 2062, moveInput)

			session = tf.Session(graph=g)

			saver = tf.train.Saver()
			name = '/model.ckpt'
			assert initPath.endswith(name)
			if os.path.exists(initPath[0:len(initPath) - len(name)]):
				saver.restore(session, initPath)
			else:
				session.run(tf.global_variables_initializer())
				saver.save(session, initPath)

		self.__boardInput = boardInput
		self.__moveInput = moveInput
		self.__output = output
		self.__session = session

	def generate(self, game, moves):
		boardIds = nf.boardImageIds(game.chessmenOnBoard(), game.activeColor())
		boardFeature = np.zeros((9, 10, 14), dtype=np.float32)
		for id in boardIds:
			x, y, h = nf.imageIdToIndex(id)
			assert boardFeature[x][y][h] == 0
			boardFeature[x][y][h] = 1
		moveFeature = np.zeros(2062, np.float32)
		for move in moves:
			id = nf.moveFeatureId2(move.fromPos, move.toPos)
			assert moveFeature[id] == 0
			moveFeature[id] = 1

		result = self.__session.run(
			self.__output,
			feed_dict={self.__boardInput:[boardFeature], self.__moveInput:[moveFeature]}
		)

		return nf.outputProbability2(moves, result[0])
