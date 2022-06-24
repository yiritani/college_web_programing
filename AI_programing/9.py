import numpy as np
from keras.datasets import mnist
(x_trains, y_trains), (x_tests, y_tests) = mnist.load_data()
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

	def train(self,
			  inputs_list,
			  targets_list  # AH/ORRI
			  ):
		inputs = np.array(
			np.append(inputs_list, (1)),
			ndmin=2
		).T
		hidden_inputs = np.dot(self.w_h,
							   inputs)
		hidden_outputs = self.activation_function(hidden_inputs)
		hidden_outputs = np.append(hidden_outputs,
								   [[1]],
								   axis=0)
		final_inputs = np.dot(self.w_o,
							  hidden_outputs)
		final_outputs = self.activation_function(final_inputs)
		return final_outputs




import time
start = time.time()
input_neurons = 784
hidden_neuronss = 200
output_neurons = 10
learning_rate = 0.1


n = neuralNetwork(input_neurons,
				 hidden_neuronss,
				 output_neurons,
				 learning_rate)
epochs = 5

for e in range (epochs) :
	for (inputs, target) in zip(x_trains, y_trains):
			targets = np.zeros (output_neurons)
			targets[int (target) ] = 0.99
			n.train (inputs,
					  targets)

print ('done')
print ("Computation time: (0:.3f) sec".format (time.time() - start))
