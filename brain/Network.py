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
		z = self.__addLayer(l5, 692+4209, 4209, None)
		self.__output = self.__pickySoftmax(z, self.__moveInput)

		self.__session = tf.Session()
		self.__session.run(tf.global_variables_initializer())

	def __pickySoftmax(self, input, pickySwitch):
		# softmax[i] = exp(input[i]) / sum(exp(input))
		# pickySoftmax[i] = pickySwitch[i]*exp(input[i]) / sum(pickySwitch*exp(input))
		expVal = input * pickySwitch
		output = expVal / tf.reduce_sum(expVal)
		return output

	def __addLayer(self, input, inputSize, outputSize, activationFunction):
		w = tf.Variable(tf.random_normal([inputSize, outputSize]))
		b = tf.Variable(tf.random_uniform([1, outputSize]))
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
		return result[0]

#n = Network()
'''
a = tf.placeholder(tf.float32, [1,2])
b = tf.placeholder(tf.float32, [1,3])

c = tf.concat([a,b], 1)

init_op = tf.initialize_all_variables()

with tf.Session() as sess:
	sess.run(init_op)
	print(sess.run(c, feed_dict={a:[[1.,2.]],b:[[4.,5.,6.]]}))
'''