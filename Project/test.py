from Project import NeurLibPerso
from Project import mnist_handler as MNIST_Handler
import numpy as np
from pandas import *
import sys
# tensorflow & Tkinter

'''input_matrix = np.matrix([1, 0, 1, 1])
weights_ih = np.matrix([np.random * 2 - 1])
matrix = np.matrix('1 2 5 4')
neuron = NeurLibPerso.Perceptron(np)'''


# Handling args, right now it's kind of unusual, but it works.
# TODO: find a way to handle args properly
# TODO: maybe a config file would be simpler for portability?
# TODO: implement a verbose setting
if len(sys.argv) < 0:
    sys.exit("Error, missing argument")

handler = MNIST_Handler.MNIST(True, sys.argv[1], 50)

np.random.seed(13)

layers = 784, 1000, 500, 10

nn = NeurLibPerso.NeuralNetwork(layers, 0)

# handler.print_image(50)

#image_id, image = handler.get_image(28)
nn.compute(handler.get_image(50))
# print("\n\nOutput from first layer:") handler.get_image(50)
# print(DataFrame(nn.compute(nn.input_values, nn.weights_ih)))'''
