from inputData.DataSet import DataSet
import tensorflow as tf


def pickySoftmax(x, inputSize, outputSize, pickySwitch):
	w = tf.Variable(tf.random_uniform([inputSize, outputSize], -0.01, 0.1))
	b = tf.Variable(tf.random_uniform([1, outputSize], 0, 0.1))
	z = tf.matmul(x, w) + b
	# softmax[i] = exp(input[i]) / sum(exp(input))
	# pickySoftmax[i] = pickySwitch[i]*exp(input[i]) / sum(pickySwitch*exp(input))
	expVal = tf.exp(z) * pickySwitch
	y = expVal / tf.reduce_sum(expVal, 1, keep_dims=True)
	return y


boardInput = tf.placeholder(tf.float32, [None, 692])
moveInput = tf.placeholder(tf.float32, [None, 4209])
prediction = tf.placeholder(tf.float32, [None, 4209])

output = pickySoftmax(boardInput, 692, 4209, moveInput)

loss = - tf.reduce_sum(prediction * tf.log(tf.maximum(output, 0.000001)))
train = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

session = tf.Session()
session.run(tf.global_variables_initializer())

tf.summary.scalar('loss', loss)
merged_summary_op = tf.summary.merge_all()
summary_writer = tf.summary.FileWriter('logs')

inputData = DataSet('../data/merged.txt')
for i in range(5000):
	boards, moves, predictions = inputData.nextBatch(128)
	feed = {
		boardInput: boards,
		moveInput: moves,
		prediction: predictions,
	}
	session.run(train, feed_dict = feed)
	summary_str = session.run(merged_summary_op, feed_dict = feed)
	summary_writer.add_summary(summary_str, i)
