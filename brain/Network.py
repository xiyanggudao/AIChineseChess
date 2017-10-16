import tensorflow as tf

class Network:

	def __init__(self):
		self.__boardInput = tf.placeholder(tf.float32, [1, 692])
		self.__moveInput = tf.placeholder(tf.float32, [1, 4209])
		allInput = tf.concat([self.__boardInput, self.__moveInput], 1)
		l1 = self.__addLayer(allInput, 692+4209, 692+4209, tf.nn.relu)
		l2 = self.__addLayer(l1, 692+4209, 692+4209, tf.nn.relu)
		l3 = self.__addLayer(l2, 692+4209, 692+4209, tf.nn.relu)
		l4 = self.__addLayer(l3, 692+4209, 692+4209, tf.nn.relu)
		l5 = self.__addLayer(l4, 692+4209, 692+4209, tf.nn.relu)
		l6 = self.__addLayer(l5, 692+4209, 692+4209, tf.nn.relu)
		l7 = self.__addLayer(l6, 692+4209, 692+4209, tf.nn.relu)
		l8 = self.__addLayer(l7, 692+4209, 692+4209, tf.nn.relu)
		l9 = self.__addLayer(l8, 692+4209, 692+4209, tf.nn.relu)
		z = self.__addLayer(l9, 692+4209, 4209, None)
		self.__output = self.__pickySoftmax(z, self.__moveInput)

		self.__session = tf.Session()
		self.__z = z
		self.__session.run(tf.global_variables_initializer())

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

#n = Network()
'''
a = tf.Variable(tf.random_uniform([1, 4], 0, 0.01))
init_op = tf.initialize_all_variables()
with tf.Session() as sess:
	sess.run(init_op)
	print(sess.run(a[0][2]))
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