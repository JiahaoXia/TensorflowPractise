from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

# FLAGS = None
#
# mnist = input_data.read_data_sets("H/Machine Learning/Tensorflow Practice/mnist")
#
# a = tf.Variable([[1, 2, 3], [3, 2, 1], [1, 1, 1], [5, 6, 7]])
# b = tf.Variable([[1, 3], [2, 3], [4, 2]])
# c = tf.Variable([10, 10])
# z = tf.matmul(a, b) + c
#
# sess = tf.InteractiveSession()
# tf.global_variables_initializer().run()
#
# batch_xs, batch_ys = mnist.train.next_batch(100)

# print(sess.run(z))

def main(_):
	print("***done***")

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--learning_rate',
		type=float,
		default=0.01,
		help='Initial learning rate.'
	)
	parser.add_argument(
		'--input_data_dir',
		type=str,
		default=os.path.join(os.getenv('TEST_TMPDIR', 'H:/Machine Learning/Tensorflow Practice/TensorflowPractise/'),
							 'tensorflow/mnist/input_data'),
		help='Directory to put the input data'
	)
	FLAGS, unparsed = parser.parse_known_args()
	print("***done***")