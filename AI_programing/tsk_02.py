import numpy as np
from keras.datasets import mnist


class neuralNetwork:
	def __init__(self,
				 input_neurons,
				 hidden_neurons,  # 恩机層の二 一口 数
				 output_neurons,  # 出力層の二 一口 数
				 learning_rate):
		self.inneurons = input_neurons
		self.hneurons = hidden_neurons
		self.oneurons = output_neurons
		self.lr = learning_rate
		self.weight_initialize()

	def weight_initialize(self):
		self.w_h = np.random.normal(0.0,
									pow(self.inneurons, -0.5),
									(self.hneurons,
									 self.inneurons
									 + 1))

		self.w_o = np.random.normal(0.0,
									pow(self.hneurons, -0.5),
									(self.oneurons,
									 self.hneurons
									 + 1))

	def activation_function(self, x):
		return 1 / (1 + np.exp(-x))

	def train(self, inputs_list, targets_list):
		inputs = np.array(
			np.append(inputs_list, (1)),
			ndmin=2
		).T
		targets = np.array(targets_list, ndmin=2).T
		hidden_inputs = np.dot(self.w_h, inputs)
		hidden_outputs = self.activation_function(hidden_inputs)
		hidden_outputs = np.append(hidden_outputs, [[1]], axis=0)
		final_inputs = np.dot(self.w_o, hidden_outputs)
		final_outputs = self.activation_function(final_inputs)
		output_errors = targets - final_outputs
		hidden_errors = np.dot(self.w_o.T, output_errors)

		self.w_o += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)),
									 np.transpose(hidden_outputs))

		hidden_errors_nobias = np.delete(
			hidden_errors,
			self.hneurons,
			axis=0)
		hidden_outputs_nobias = np.delete(
			hidden_outputs,
			self.hneurons,
			axis=0)

		self.w_h += self.lr * np.dot((hidden_errors_nobias * hidden_outputs_nobias * (1.0 - hidden_outputs_nobias)),
									 np.transpose(inputs))

	def evaluate(self, inputs_list):
		inputs = np.array(
			np.append(inputs_list, [1]),
			ndmin=2).T
		hidden_inputs = np.dot(self.w_h,
							   inputs)

		hidden_outputs = self.activation_function(hidden_inputs)

		final_inputs = np.dot(self.w_o, np.append(hidden_outputs, [1]), )
		final_outputs = self.activation_function(final_inputs)
		return final_outputs



(x_trains, y_trains), (x_test, y_test) = mnist.load_data()
x_trains = x_trains.reshape((60000, 784))
x_trains = (x_trains / 255.0 * 0.99) + 0.01

import time

start = time.time()
input_neurons = 784
hidden_neuronss = 200
output_neurons = 10
learning_rate = 0.1

n = neuralNetwork(input_neurons, hidden_neuronss, output_neurons, learning_rate)

epochs = 5

for e in range(epochs):
	for (inputs, target) in zip(x_trains, y_trains):
		targets = np.zeros(output_neurons) + 0.01
		targets[int(target)] = 0.99
		n.train(inputs, targets)

print('done')
print("Computation time: {0:.3f} sec".format(time.time() - start))


import matplotlib.pyplot as plt
plt.figure(1, figsize=(12, 3.2))
plt.subplots_adjust(wspace=0.5)
plt.gray()
plt.subplot(1,3,1)
img = x_test[0, :, :].reshape((28, 28))
plt.pcolor(255-img)
plt.xlim(0, 27)
plt.ylim(27,0)
plt.show()


input_neurons = 3
hidden_neurons = 100
output_neurons = 3
learning_rate = 0.9
n = neuralNetwork(input_neurons, hidden_neurons, output_neurons, learning_rate)
print(n.train([1.0, 1.5, 2.0], [1.0, 1.5, 2.0]))

x_tests = x_test.reshape((10000, 784))
x_tests = (x_tests / 255.0 * 0.99) + 0.01

score = []
for (inputs, correct_label) in zip(x_tests, y_test):
	outputs = n.evaluate(inputs)
	targets = np.zeros(output_neurons) + 0.01
	targets[int(correct_label)] = 0.99
	label = np.argmax(outputs)
	if (label == correct_label):
		score.append(1)
	else:
		score.append(0)

score_arry = np.asarray(score)
print("performance=",score_arry.sum()/score_arry.size)