from inputData.DataSet import DataSet
import tensorflow as tf
import time


def addResBlock(x, inputSize):
	w1 = tf.Variable(tf.random_uniform([inputSize, inputSize], -0.001, 0.01))
	b1 = tf.Variable(tf.random_uniform([1, inputSize], 0, 0.1))
	z1 = tf.matmul(x, w1) + b1
	y1 = tf.nn.relu(z1)
	w2 = tf.Variable(tf.random_uniform([inputSize, inputSize], -0.001, 0.01))
	b2 = tf.Variable(tf.random_uniform([1, inputSize], 0, 0.1))
	z2 = tf.matmul(y1, w2) + b2 + x
	y2 = tf.nn.relu(z2)
	return y2

def pickySoftmax(x, inputSize, outputSize, pickySwitch):
	w = tf.Variable(tf.random_uniform([inputSize, outputSize], -0.001, 0.01))
	b = tf.Variable(tf.random_uniform([1, outputSize], 0, 0.01))
	z = tf.matmul(x, w) + b
	# softmax[i] = exp(input[i]) / sum(exp(input))
	# pickySoftmax[i] = pickySwitch[i]*exp(input[i]) / sum(pickySwitch*exp(input))
	expVal = tf.exp(z) * pickySwitch
	y = expVal / tf.reduce_sum(expVal, 1, keep_dims=True)
	return y


boardInput = tf.placeholder(tf.float32, [None, 692])
moveInput = tf.placeholder(tf.float32, [None, 4209])
prediction = tf.placeholder(tf.float32, [None, 4209])

l1 = addResBlock(boardInput, 692)
l2 = addResBlock(l1, 692)
output = pickySoftmax(l2, 692, 4209, moveInput)

loss = - tf.reduce_sum(prediction * tf.log(tf.maximum(output, 0.000001)))
train = tf.train.GradientDescentOptimizer(1e-5).minimize(loss)

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
test loss 50128.7
test accuracy 0.304257
'''