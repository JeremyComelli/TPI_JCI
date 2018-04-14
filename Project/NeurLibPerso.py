import numpy as np
from pandas.io.parsers import *
import math


# pandas is mainly used to pretty-print matrices
class NeuralNetwork:
    # stuff of dreams
    def __init__(self, nb_layers, activation_function=0):

        # Setting the print precision to 3, to get simpler readings
        np.set_printoptions(precision=7)

        #  Suppresses scientific notation for small values, improves readability
        # np.set_printoptions(suppress=True)

        self.layers = nb_layers

        # Current step is used by recursive layer computation function to know which layer is currently processed
        self.current_step = 0

        # Generating weights for the different layers
        self.weights = self.generate_weights(nb_layers)

        # TODO: generate_biases()

        self.activation_function = activation_function

        print("\nNeural network Initialized Successfully\n")

    # Generates random weights between 2 layers. Every value is between -1 and 1
    @staticmethod
    def generate_weights(nb_layers):
        weights = list()
        i = 0
        for current_layer in nb_layers:
            if i < len(nb_layers) - 1:
                print(str(current_layer) + " | " + str(nb_layers[i + 1]))
                weights.append(np.matrix(np.random.rand(nb_layers[i + 1], current_layer)))
            i += 1
        return weights



    # Generates random biases for each neuron (except input and output)
    @staticmethod
    def generate_biases(nb_layers):
        # TODO: vérifier si les bias sont générés pour les bon layer
        biases = list()
        for current_layer in nb_layers:
            if current_layer > 0:
                biases.append(np.random.rand() * 10)
        return 0

    # Used to choose which activation function to use.
    # TODO: add new activation functions
    def activate(self, value):
        if self.activation_function is 0:
            return self.sigmoid(value, False)
        else:
            sys.exit("Error: activation function does not exist, please check your configuration file")
        return 0
    # Sigmoid function, taken from https://iamtrask.github.io/2015/07/12/basic-python-network/

    @staticmethod
    def sigmoid(x, deriv=False):
        if deriv:
            return x*(1-x)
        return 1/(1+np.exp(-x))

    def compute(self, input_vector=0):
        # if no input is specified, we use dummy values for testing
        if input_vector is 0:
            print("\nNo input values specified, using dummy-random values")
            input_vector = np.matrix(np.random.rand(self.layers[self.current_step], 1))
            input_answer = np.random.randint(0, 10)

            # Recursive magic happening here
            self.compute_layer(input_vector)
        else:
            input_answer, raw_input_image = input_vector
            input_image = np.matrix(raw_input_image)
            self.compute_layer(input_image.transpose())

        print(input_answer)
        return 0

    # Recursive function that computes a layer, then calls itself with
    def compute_layer(self, input_vector):
        if self.current_step + 1 is not len(self.layers):
            print("\n\n\nInput from layer " + str(self.current_step) + " to layer " + str(self.current_step + 1) + ":")
        else:
            print("\n\n\nOutput (Layer " + str(self.current_step) + "): ")

        print(DataFrame(input_vector))

        # print(DataFrame(self.weights[self.current_step]))
        # Recursion happens here, if there is another layer, we need to go deeper
        if self.current_step < len(self.layers) - 1:
            #
            layer_output = np.dot(self.weights[self.current_step], input_vector)
            self.current_step += 1
            self.compute_layer(self.activate(layer_output))

        return 0

    # Here we compute a weighted sum
    def compute_neuron(self, input_matrix, weight_matrix, bias=0):
        weight_matrix = weight_matrix.transpose()
        print(str(input_matrix.shape))
        print(str(weight_matrix.shape))
        # Prints used to troubleshoot neurons, remove for release
        '''print("\nNeuron input: \n" + str(input_matrix))
        print("\nNeuron Weights: \n" + str(weight_matrix.transpose()))
        print(str(type(weight_matrix)) + " " + str(type(input_matrix)))
        # print("\nNeuron Output: "+ str(np.tensordot(input_matrix, weight_matrix.transpose())))
        print("Weights Shape: " + str(weight_matrix.shape))'''
        # print("Inputs Shape: " + str(np.tensordot(input_matrix.transpose(), weight_matrix)))
        print(np.dot(input_matrix, weight_matrix))
        return self.activate(np.dot(input_matrix.transpose(), weight_matrix))


