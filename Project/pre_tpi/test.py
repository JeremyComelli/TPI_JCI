from pre_tpi import NeurLibPerso
import numpy as np
# tensorflow & Tkinter

'''input_matrix = np.matrix([1, 0, 1, 1])
weights_ih = np.matrix([np.random * 2 - 1])
matrix = np.matrix('1 2 5 4')
neuron = NeurLibPerso.Perceptron(np)'''

np.random.seed(1)

nn = NeurLibPerso.NeuralNetwork(15, 15, 1)

print(nn.compute(np.random.random((nn.input_layer_size, 1)) * 2 - 1, np.random.random((nn.input_layer_size, 1)) * 2 - 1))
