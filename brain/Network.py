import tensorflow as tf
import os
import time
import brain.NetworkFeature as nf
from chess.Chessman import Chessman

class Network:

	def __init__(self, initPath):
		g = tf.Graph()
		with g.as_default():
			boardInput = tf.placeholder(tf.float32, [None, 692])
			moveInput = tf.placeholder(tf.float32, [None, 4209])
			input = tf.concat([boardInput, moveInput], 1)
			l1 = self.__addLayer(input, 692+4209, 692+4209, tf.nn.relu)
			l2 = self.__addLayer(l1, 692+4209, 692+4209, tf.nn.relu)
			l3 = self.__addLayer(l2, 692+4209, 692+4209, tf.nn.relu)
			l4 = self.__addLayer(l3, 692+4209, 692+4209, tf.nn.relu)
			l5 = self.__addLayer(l4, 692+4209, 692+4209, tf.nn.relu)
			l6 = self.__addLayer(l5, 692+4209, 692+4209, tf.nn.relu)
			z = self.__addLayer(l6, 692+4209, 4209, None)
			output = self.__pickySoftmax(z, moveInput)

			reward = tf.placeholder(tf.float32, [None], 'reward')
			moveId = tf.placeholder(tf.float32, [None, 4209], 'moveId')
			loss = - tf.reduce_mean(reward * tf.log(tf.reduce_sum(output*moveId, 1)))
			train = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

			session = tf.Session(graph=g)

			saver = tf.train.Saver()
			name = '/model.ckpt'
			assert initPath.endswith(name)
			if os.path.exists(initPath[0:len(initPath) - len(name)]):
				saver.restore(session, initPath)
			else:
				session.run(tf.global_variables_initializer())
				saver.save(session, initPath)

		self.__graph = g
		self.__boardInput = boardInput
		self.__moveInput = moveInput
		self.__z = z
		self.__output = output
		self.__session = session
		self.__train = train
		self.__reward = reward
		self.__moveId = moveId

		self.__trainBoardFeatures = []
		self.__trainMoveFeatures = []
		self.__trainRewards = []
		self.__trainMoveSelectors = []

	def __pickySoftmax(self, input, pickySwitch):
		# softmax[i] = exp(input[i]) / sum(exp(input))
		# pickySoftmax[i] = pickySwitch[i]*exp(input[i]) / sum(pickySwitch*exp(input))
		expVal = tf.exp(input) * pickySwitch
		output = expVal / tf.reduce_sum(expVal, 1, keep_dims=True)
		return output

	def __addLayer(self, input, inputSize, outputSize, activationFunction):
		w = tf.Variable(tf.random_uniform([inputSize, outputSize], -0.0001, 0.001))
		b = tf.Variable(tf.random_uniform([1, outputSize], 0, 0.01))
		z = tf.matmul(input, w) + b
		if activationFunction:
			output = activationFunction(z)
		else:
			output = z
		return output

	def generate(self, game, moves):
		boardFeature, moveFeature = nf.inputFeature(game.chessmenOnBoard(), moves)

		assert len(boardFeature) == 692
		assert len(moveFeature) == 4209

		result = self.__session.run(
			self.__output,
			feed_dict={self.__boardInput:[boardFeature], self.__moveInput:[moveFeature]}
		)

		'''
		z = self.__session.run(
			self.__z,
			feed_dict={self.__boardInput:[boardFeature], self.__moveInput:[moveFeature]}
		)
		for i in range(len(z[0])):
			if moveFeature[i] == 1:
				print(z[0][i],end=' ')
		print('\n---------------------------------------------------------------------------------------')
		for i in range(len(result[0])):
			if moveFeature[i] == 1:
				print(result[0][i],end=' ')
		print('\n---------------------------------------------------------------------------------------')
		'''
		return nf.outputProbability(moves, result[0])

	def addTrainData(self, chessmenOnBoard, moves, moveIndex, reward):
		if len(moves) > 1 and reward != 0:
			boardFeature, moveFeature = nf.inputFeature(chessmenOnBoard, moves)
			move = moves[moveIndex]
			type = Chessman.type(move.moveChessman)
			color = Chessman.color(move.moveChessman)
			moveId = nf.moveFeatureId(type, color, move.fromPos, move.toPos, color)
			moveSelector = [0 for i in range(4209)]
			moveSelector[moveId] = 1

			self.__trainBoardFeatures.append(boardFeature)
			self.__trainMoveFeatures.append(moveFeature)
			self.__trainRewards.append(reward)
			self.__trainMoveSelectors.append(moveSelector)

	def train(self):
		if len(self.__trainBoardFeatures) > 1:
			self.__session.run(
				self.__train,
				feed_dict={
					self.__boardInput: self.__trainBoardFeatures,
					self.__moveInput: self.__trainMoveFeatures,
					self.__reward: self.__trainRewards,
					self.__moveId: self.__trainMoveSelectors
				}
			)

			self.__trainBoardFeatures.clear()
			self.__trainMoveFeatures.clear()
			self.__trainRewards.clear()
			self.__trainMoveSelectors.clear()

	def save(self, path):
		print('save start')
		saveStart = time.time()
		with self.__graph.as_default():
			saver = tf.train.Saver()
			saver.save(self.__session, path)
		saveEnd = time.time()
		print('save finished, cost time', round(saveEnd-saveStart, 2))
