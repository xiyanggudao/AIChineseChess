import tensorflow as tf
import time
import sys
sys.path.append("..")
from inputData.DataSet2 import DataSet


layer_cnt = 0
def addLayer(x, in_channels, out_channels, kSize=5):
	global layer_cnt
	layer_cnt += 1
	w1 = tf.Variable(tf.truncated_normal([kSize, kSize, in_channels, out_channels], 0., 0.02))
	b1 = tf.Variable(tf.constant(0.1, shape=[out_channels]))
	z1 = tf.nn.conv2d(x, w1, strides=[1, 1, 1, 1], padding='SAME') + b1
	tf.summary.histogram("weight_bias/weight" + str(layer_cnt), w1)
	tf.summary.histogram("weight_bias/bias" + str(layer_cnt), b1)
	tf.summary.histogram("weight_bias/z" + str(layer_cnt), z1)
	y = tf.nn.relu(z1)
	if in_channels == out_channels:
		layer_cnt += 1
		w2 = tf.Variable(tf.truncated_normal([5, 5, in_channels, out_channels], 0., 0.02))
		b2 = tf.Variable(tf.constant(0.1, shape=[out_channels]))
		z2 = tf.nn.conv2d(y, w2, strides=[1, 1, 1, 1], padding='SAME') + b2 + x
		tf.summary.histogram("weight_bias/weight" + str(layer_cnt), w2)
		tf.summary.histogram("weight_bias/bias" + str(layer_cnt), b2)
		tf.summary.histogram("weight_bias/z" + str(layer_cnt), z2)
		y = tf.nn.relu(z2)
	return y

def pickySoftmax(x, inputSize, outputSize, pickySwitch):
	global layer_cnt
	layer_cnt += 1
	w = tf.Variable(tf.truncated_normal([inputSize, outputSize], 0, 0.01))
	b = tf.Variable(tf.constant(0.1, shape=[1, outputSize]))
	z = tf.matmul(x, w) + b
	tf.summary.histogram("weight_bias/weight" + str(layer_cnt), w)
	tf.summary.histogram("weight_bias/bias" + str(layer_cnt), b)
	tf.summary.histogram("weight_bias/z" + str(layer_cnt), z)
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
l1 = addLayer(l1, 128, 64, 1)
flat = tf.reshape(l1, [-1, 9*10*64])
output = pickySoftmax(flat, 9*10*64, 4209, moveInput)

loss = - tf.reduce_sum(prediction * tf.log(tf.maximum(output, 1e-8)))
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
dataTime = 0
trainTime = 0
for i in range(300000):
	dataStart = time.time()
	boards, moves, predictions = inputData.nextBatch(128)
	dataTime += time.time() - dataStart
	feed = {
		boardInput: boards,
		moveInput: moves,
		prediction: predictions,
	}
	if i%1000 == 0:
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
test loss 29602.0
test accuracy 0.3066
'''