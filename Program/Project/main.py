from Project import NeurLibPerso
from Project import mnist_handler as MNIST_Handler
import numpy as np
import os
from pandas import *
import sys
import configparser

if len(sys.argv) < 0:
    sys.exit("Error, missing argument")

if os.path.isfile(sys.argv[1]):
    config = configparser.ConfigParser()
    config.read(sys.argv[1])
else:
    sys.exit("Error: missing config file")

if config['GLOBAL']['verbose'] and int(config['GLOBAL']['log_level']) > 0:
    print("Config file: " + sys.argv[1])
    print("\nConfig sections found:")
    print(config.sections())

if config['MNIST']['active']:
    handler = MNIST_Handler.MNIST(config)

if config['NEURALNET']['active']:
    # Creating Neural Network without overriding network structure or activation function
    nn = NeurLibPerso.NeuralNetwork(config)

if config['GLOBAL']['verbose'] and int(config['GLOBAL']['log_level']) > 0:
    # Printing a parsed image, for fun
    handler.print_image(1)

nn.compute_image(handler.get_image(1))
