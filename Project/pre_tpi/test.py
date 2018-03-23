from pre_tpi import NeurLibPerso
from pre_tpi import mnist_handler as MNIST_Handler
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
if sys.argv[1] is None or sys.argv[2] is None:
    sys.exit("Error, missing argument")

handler = MNIST_Handler.MNIST(True, sys.argv[1])

handler.print_data()


# print(str(image_byte))
# np.random.seed(12)

# Setting the print precision to 3, to get simpler readings
# np.set_printoptions(precision=3)

#  Suppresses scientific notation for small values, because I'm lazy and don't want to think
# np.set_printoptions(suppress=True)

# nn = NeurLibPerso.NeuralNetwork(10, 10, 1)

# print("\n\nOutput from first layer:")
# print(DataFrame(nn.compute(nn.input_values, nn.weights_ih)))'''
