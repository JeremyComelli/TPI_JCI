import numpy as np
from pandas import *


# pandas is mainly used to pretty-print matrices
class NeuralNetwork:
    # stuff of dreams
    def __init__(self, input_layer, hidden_layer, output_layer):
        # set neural network specs from input
        # this is a three layered neural network, but in the end, we should be able to specify n number of layers through a matrix
        self.input_layer_size = input_layer
        self.hidden_layer_size = hidden_layer
        self.output_layer_size = output_layer

        # matrix of n rows, and 1 column, will be used for dot product

        # Generating hidden layer weights
        # Generates a matrix where rows = nb of neurons, and columns = nb of input + 1 columns of bias weights
        self.weights_ih = np.matrix(np.random.rand(self.hidden_layer_size, self.input_layer_size) * 2 - 1)

        # Generating hidden layer biases
        self.biases_hidden = np.matrix((np.random.rand(self.input_layer_size, 1)*10).round(0))

        # Generating input values
        self.input_values = np.matrix(np.random.rand(self.input_layer_size, 1).round(0))

        np.set_printoptions(precision=3)
        print("\n\nInput values")
        print(DataFrame(self.input_values).round(3))

        print("\n\nWeights")
        print(DataFrame(self.weights_ih).round(3))

        print("\n\nBiases")
        print(DataFrame(self.biases_hidden).round(3))

    # sigmoid function, taken from https://iamtrask.github.io/2015/07/12/basic-python-network/
    def sigmoid(self, input_number, deriv=False):
        if deriv:
            return input_number*(1-input_number)
        return 1/(1+np.exp(-input_number))

    def compute(self, input_matrix, weights_matrix):
        return self.sigmoid(np.dot(weights_matrix, input_matrix)+self.biases_hidden)



