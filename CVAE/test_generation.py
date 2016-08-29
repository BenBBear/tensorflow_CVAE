from configuration import *
import numpy as np
import tensorflow as tf
from os.path import realpath
from random import randint
num_iter = 10
model_path = "./save/"
from tensor_definition import test_epsilon, test_x_hat

saver = tf.train.Saver()

def test(sess):
    normalized_z = np.random.normal(0, 1.0, latent_dim).reshape((1, latent_dim))
    feed_dict = {test_epsilon: normalized_z}
    r = sess.run(test_x_hat, feed_dict=feed_dict)
    return r.reshape((28, 28))


results = []
model_path = realpath(model_path)
with tf.Session() as sess:
    ckpt = tf.train.get_checkpoint_state(model_path)
    if ckpt and ckpt.model_checkpoint_path:
        saver.restore(sess, model_path + "/model.ckpt")
        print("Model loaded")
        for i in range(num_iter):
            results.append(test(sess))
    else:
        print("No checkpoint file found")


# analyze the results
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

id = 7
plt.imshow(results[id])

print("Finished")
# Session.run tutorial:
# a = tf.constant([10, 20])
# b = tf.constant([1.0, 2.0])
# 'fetches' can be a singleton
# v = session.run(a)
# v is the numpy array [10, 20]
# 'fetches' can be a list.
# v = session.run([a, b])
# v a Python list with 2 numpy arrays: the numpy array [10, 20] and the
# 1-D array [1.0, 2.0]
# 'fetches' can be arbitrary lists, tuples, namedtuple, dicts:
# MyData = collections.namedtuple('MyData', ['a', 'b'])
# v = session.run({'k1': MyData(a, b), 'k2': [b, a]})
# v is a dict with
# v['k1'] is a MyData namedtuple with 'a' the numpy array [10, 20] and
# 'b' the numpy array [1.0, 2.0]
# v['k2'] is a list with the numpy array [1.0, 2.0] and the numpy array
# [10, 20].



# The optional feed_dict argument allows the caller to override the value of tensors in the graph.
# Each key in feed_dict can be one of the following types:
#
# If the key is a Tensor, the value may be a Python scalar, string, list, or numpy ndarray
# that can be converted to the same dtype as that tensor. Additionally, if the key is a placeholder,
# the shape of the value will be checked for compatibility with the placeholder.
#
# If the key is a SparseTensor, the value should be a SparseTensorValue.
# If the key is a nested tuple of Tensors or SparseTensors, the value should be a nested tuple with the same
#  structure that maps to their corresponding values as above.
#
# Each value in feed_dict must be convertible to a numpy array of the dtype of the corresponding key.