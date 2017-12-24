import tensorflow as tf
import time
import sys
sys.path.append("..")
from inputData.DataSet2 import DataSet


def addLayer(x, in_channels, out_channels):
	w1 = tf.Variable(tf.random_uniform([3, 3, in_channels, out_channels], -0.01, 0.01))
	b1 = tf.Variable(tf.random_uniform([out_channels], 0, 0.01))
	z1 = tf.nn.conv2d(x, w1, strides=[1, 1, 1, 1], padding='SAME') + b1
	y = tf.nn.relu(z1)
	if in_channels == out_channels:
		w2 = tf.Variable(tf.random_uniform([3, 3, in_channels, out_channels], -0.01, 0.01))
		b2 = tf.Variable(tf.random_uniform([out_channels], 0, 0.01))
		z2 = tf.nn.conv2d(y, w2, strides=[1, 1, 1, 1], padding='SAME') + b2 + x
		y = tf.nn.relu(z2)
	return y

def pickySoftmax(x, inputSize, outputSize, pickySwitch):
	w = tf.Variable(tf.random_uniform([inputSize, outputSize], -0.01, 0.01))
	b = tf.Variable(tf.random_uniform([1, outputSize], 0, 0.01))
	z = tf.matmul(x, w) + b
	# softmax[i] = exp(input[i]) / sum(exp(input))
	# pickySoftmax[i] = pickySwitch[i]*exp(input[i]) / sum(pickySwitch*exp(input))
	expVal = tf.exp(z) * pickySwitch
	y = expVal / tf.reduce_sum(expVal, 1, keep_dims=True)
	return y


boardInput = tf.placeholder(tf.float32, [None, 9, 10, 14])
moveInput = tf.placeholder(tf.float32, [None, 4209])
prediction = tf.placeholder(tf.float32, [None, 4209])

l1 = addLayer(boardInput, 14, 128)
l1 = addLayer(l1, 128, 128)
l1 = addLayer(l1, 128, 128)
l1 = addLayer(l1, 128, 128)
flat = tf.reshape(l1, [-1, 9*10*128])
output = pickySoftmax(flat, 9*10*128, 4209, moveInput)

loss = - tf.reduce_sum(prediction * tf.log(tf.maximum(output, 1e-8)))
train = tf.train.GradientDescentOptimizer(1e-6).minimize(loss)

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
dataTime = 0
trainTime = 0
for i in range(200000):
	dataStart = time.time()
	boards, moves, predictions = inputData.nextBatch(128)
	dataTime += time.time() - dataStart
	feed = {
		boardInput: boards,
		moveInput: moves,
		prediction: predictions,
	}
	if i%300 == 0:
		summary_str = session.run(merged_summary_op, feed_dict = feed)
		summary_writer.add_summary(summary_str, i)
	trainStart = time.time()
	session.run(train, feed_dict = feed)
	trainTime += time.time() - trainStart


print('train finished dataTime', int(dataTime), 'trainTime', int(trainTime))
testData = DataSet('../data/test.gz')
boards, moves, predictions = testData.nextBatch(10000)#len(testData.dataIds))
res = session.run([loss, accuracy], feed_dict = {
	boardInput: boards,
	moveInput: moves,
	prediction: predictions,
})
print('test loss', res[0])
print('test accuracy', res[1])
'''
test loss 30833.2
test accuracy 0.2606
'''