import numpy as np

np.random.seed(1)
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import Adam


model = Sequential()
model.add(Conv2D(filters=16,
				 kernel_size=(3, 3),
				 input_shape=(28, 28, 1),
				 padding='same',
				 activation='relu'
				 ))
model.add(Conv2D(filters=32,
				 kernel_size=(3, 3),
				 padding='same',
				 activation='relu'
				 ))

model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(filters=64,
				 kernel_size=(3, 3),
				 padding='same',
				 activation='relu'
				 ))
model.add(
	MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Flatten())

model.add(Dense(128,
				activation='relu'
				))
# model.add (Dropout (0.25))
model.add(Dense(10,
				activation=
				'softmax'
				))
model.compile(
	loss=
	'categorical_ crossentropy',
	optimizer=Adam(),
	metrics=['accuracy']
)
model.summary()

import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 28, 28, 1)
x_train = x_train.astype('float32')
x_train /= 255
correct = 10
y_train = np_utils.to_categorical(y_train, correct)
x_test = x_test.reshape(10000, 28, 28, 1)
x_test = x_test.astype('float32')
x_test /= 255
y_test = np_utils.to_categorical(y_test, correct)
model.compile()
import time

start = time.time()
history = model.fit(x_train,
					y_train,
					batch_size=100,
					epochs=20,
					verbose=1,
					validation_data=(
						x_test, y_test
					))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
print("Computation time: (0:.3f, sec".format(time.time() - start))