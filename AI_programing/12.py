import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape (60000, 28, 28, 1)
X_train = x_train.astype ('float32')
x_train /= 255
correct = 10
y_train = np_utils.to_categorical (y_train, correct)
x_test = x_test.reshape (10000, 28, 28, 1)
x_test = x_test.astype ('float32')
x_test /= 255
y_test = np_utils.to_categorical(y_test, correct)


import time
start = time.time()
history = model.fit(x_train,
y_train,
batch_size=100,
epochs=20,
verbose=1,
validation data=
X test, y test #子 卜 一女の指定
))
score = model.evaluate(x test, y _test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])