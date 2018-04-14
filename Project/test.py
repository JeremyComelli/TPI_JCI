from Project import NeurLibPerso
from Project import mnist_handler as MNIST_Handler
import numpy as np
from pandas import *
import sys
import configparser
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
config = configparser.ConfigParser()
config.read(sys.argv[1])

if config['GLOBAL']['verbose'] and int(config['GLOBAL']['log_level']) > 0:
    print("Config file: " + sys.argv[1])
    print("\nConfig sections found:")
    print(config.sections())


handler = MNIST_Handler.MNIST(config)

#np.random.seed(13)

#layers = 784, 1000, 500, 10

#nn = NeurLibPerso.NeuralNetwork(layers, 0)

# handler.print_image(50)

#image_id, image = handler.get_image(28)
#print("Output is:" + str(nn.compute_image(handler.get_image(50))))

#test_output = np.matrix('0.456; 0.0; 0.203; 0.399; 0.0; 0.965; 0.344; 0.133; 0.200; 0.999')

#print(nn.get_error(nn.compute_image(handler.get_image(12))))

#print(nn.get_error(9, test_output))
# print("\n\nOutput from first layer:") handler.get_image(50)
# print(DataFrame(nn.compute(nn.input_values, nn.weights_ih)))'''
