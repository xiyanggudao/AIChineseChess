from inputData.DataSet import DataSet
import tensorflow as tf
import time


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
train = tf.train.GradientDescentOptimizer(0.002).minimize(loss)

correct_prediction = tf.equal(tf.argmax(prediction * output,1), tf.argmax(output,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

session = tf.Session()
session.run(tf.global_variables_initializer())

tf.summary.scalar('loss', loss)
tf.summary.scalar('accuracy', accuracy)
merged_summary_op = tf.summary.merge_all()
summary_writer = tf.summary.FileWriter('logs')

dataStart = time.time()
inputData = DataSet('../data/train.gz')
dataEnd = time.time()
print('data time', round(dataEnd - dataStart, 2), 'size', len(inputData.dataIds))
for i in range(300000):
	boards, moves, predictions = inputData.nextBatch(128)
	feed = {
		boardInput: boards,
		moveInput: moves,
		prediction: predictions,
	}
	if i%300 == 0:
		summary_str = session.run(merged_summary_op, feed_dict = feed)
		summary_writer.add_summary(summary_str, i)
	session.run(train, feed_dict = feed)

print('train finished')
testData = DataSet('../data/test.gz')
boards, moves, predictions = testData.nextBatch(len(testData.dataIds))
res = session.run([loss, accuracy], feed_dict = {
	boardInput: boards,
	moveInput: moves,
	prediction: predictions,
})
print('test loss', res[0])
print('test accuracy', res[1])
'''
test loss 42844.4
test accuracy 0.468958
'''
