from pre_tpi import NeurLibPerso
import numpy as np
from pandas import *
# tensorflow & Tkinter

'''input_matrix = np.matrix([1, 0, 1, 1])
weights_ih = np.matrix([np.random * 2 - 1])
matrix = np.matrix('1 2 5 4')
neuron = NeurLibPerso.Perceptron(np)'''

np.random.seed(12)

# Setting the print precision to 3, to get simpler readings
np.set_printoptions(precision=3)

#  Suppresses scientific notation for small values, because I'm lazy and don't want to think
np.set_printoptions(suppress=True)

nn = NeurLibPerso.NeuralNetwork(10, 10, 1)

print("\n\nOutput from first layer:")
print(DataFrame(nn.compute(nn.input_values, nn.weights_ih)))
