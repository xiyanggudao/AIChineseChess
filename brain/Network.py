import tensorflow as tf
import os

class Network:

	def __init__(self):
		g = tf.Graph()
		with g.as_default():
			boardInput = tf.placeholder(tf.float32, [1, 692])
			moveInput = tf.placeholder(tf.float32, [1, 4209])
			input = tf.concat([boardInput, moveInput], 1)
			l1 = self.__addLayer(input, 692+4209, 692+4209, tf.nn.relu)
			l2 = self.__addLayer(l1, 692+4209, 692+4209, tf.nn.relu)
			l3 = self.__addLayer(l2, 692+4209, 692+4209, tf.nn.relu)
			l4 = self.__addLayer(l3, 692+4209, 692+4209, tf.nn.relu)
			l5 = self.__addLayer(l4, 692+4209, 692+4209, tf.nn.relu)
			l6 = self.__addLayer(l5, 692+4209, 692+4209, tf.nn.relu)
			l7 = self.__addLayer(l6, 692+4209, 692+4209, tf.nn.relu)
			l8 = self.__addLayer(l7, 692+4209, 692+4209, tf.nn.relu)
			l9 = self.__addLayer(l8, 692+4209, 692+4209, tf.nn.relu)
			z = self.__addLayer(l9, 692+4209, 4209, None)
			output = self.__pickySoftmax(z, moveInput)

			reward = tf.placeholder(tf.float32, [])
			moveId = tf.placeholder(tf.int32, [])
			loss = reward * tf.log(output[0][moveId])
			train = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

			session = tf.Session(graph=g)

			saver = tf.train.Saver()
			if os.path.exists("./model/20171016"):
				saver.restore(session, "./model/20171017/model.ckpt")
			else:
				session.run(tf.global_variables_initializer())
				saver.save(session, "./model/20171017/model.ckpt")

		self.__graph = g
		self.__boardInput = boardInput
		self.__moveInput = moveInput
		self.__z = z
		self.__output = output
		self.__session = session
		self.__train = train
		self.__reward = reward
		self.__moveId = moveId

	def __pickySoftmax(self, input, pickySwitch):
		# softmax[i] = exp(input[i]) / sum(exp(input))
		# pickySoftmax[i] = pickySwitch[i]*exp(input[i]) / sum(pickySwitch*exp(input))
		expVal = input * pickySwitch
		output = expVal / tf.reduce_sum(expVal)
		return output

	def __addLayer(self, input, inputSize, outputSize, activationFunction):
		w = tf.Variable(tf.random_uniform([inputSize, outputSize], 0, 0.001))
		b = tf.Variable(tf.random_uniform([1, outputSize], 0, 0.01))
		z = tf.matmul(input, w) + b
		if activationFunction:
			output = activationFunction(z)
		else:
			output = z
		return output

	def generate(self, boardFeature: list, moveFeature: list):
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
			if i%20==0:
				print('')
			print(z[0][i],end=' ')
		print('\n---------------------------------------------------------------------------------------')
		for i in range(len(result[0])):
			if i%20==0:
				print('')
			print(result[0][i],end=' ')
		'''
		return result[0]

	def train(self, boardFeature: list, moveFeature: list, moveId, reward):
		self.__session.run(
			self.__train,
			feed_dict={
				self.__boardInput: [boardFeature],
				self.__moveInput: [moveFeature],
				self.__reward: reward,
				self.__moveId: moveId
			}
		)

	def save(self):
		print('save start')
		with self.__graph.as_default():
			saver = tf.train.Saver()
			saver.save(self.__session, "./model/20171017/model.ckpt")
		print('save finished')

#n = Network()
'''
a = tf.Variable(tf.random_uniform([1, 4], 0, 0.01))
i = tf.placeholder(tf.int32, [])
y = a[0][i]
init_op = tf.initialize_all_variables()
with tf.Session() as sess:
	sess.run(init_op)
	print(sess.run(y, feed_dict={i:2}))
'''
'''
a = tf.placeholder(tf.float32, [1,2])
b = tf.placeholder(tf.float32, [1,3])

c = tf.concat([a,b], 1)

init_op = tf.initialize_all_variables()

with tf.Session() as sess:
	sess.run(init_op)
	print(sess.run(c, feed_dict={a:[[1.,2.]],b:[[4.,5.,6.]]}))
'''