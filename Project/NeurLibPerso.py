import numpy as np
from pandas.io.parsers import *
import math


# pandas is mainly used to pretty-print matrices
class NeuralNetwork:
    # stuff of dreams
    def __init__(self, config, nb_layers=0, activation_function=0):

        self.config = config['NEURALNET']

        # Setting the print precision to 3, to get simpler readings
        np.set_printoptions(precision=7)

        #  Suppresses scientific notation for small values, improves readability
        # np.set_printoptions(suppress=True)

        if nb_layers > 0:
            self.layers = nb_layers
        else:
            self.layers = config['structure']


        # Current step is used by recursive layer computation function to know which layer is currently processed
        self.current_step = 0

        # Generating weights for the different layers
        self.weights = self.generate_weights(self.layers)

        if self.config['verbose'] and int(self.config['log_level']) > 1:
            print(DataFrame(self.weights))

        # TODO: generate_biases()

        if activation_function > 0:
            self.activation_function = activation_function
        else:
            self.activation_function = self.config['activation_function']

        if self.config['verbose'] and int(self.config['log_level']) > 0:
            print("\nNeural network Initialized Successfully\n")

    # Generates random weights between 2 layers. Every value is between -1 and 1
    @staticmethod
    def generate_weights(nb_layers):
        weights = list()
        i = 0
        for current_layer in nb_layers:
            if i < len(nb_layers) - 1:
                weights.append(np.matrix(np.random.rand(nb_layers[i + 1], current_layer)/1000))
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

    def compute_image(self, input_vector=0):

        # if no input is specified, we use dummy values for testing
        if input_vector is 0:
            if self.config['verbose'] and int(self.config['log_level']) > 0:
                print("\nNo input values specified, using dummy-random values")

            input_vector = np.matrix(np.random.rand(self.layers[self.current_step], 1))
            input_answer = np.random.randint(0, 10)

            # Recursive magic happening here
            output = self.compute_layer(input_vector)
        else:
            input_answer, raw_input_image = input_vector
            input_image = np.matrix(raw_input_image)
            output = self.compute_layer(input_image.transpose())

        return  input_answer, output

    # Recursive function that computes a layer, then calls itself with
    def compute_layer(self, input_vector):
        if self.current_step + 1 is not len(self.layers):
            if self.config['verbose'] and int(self.config['log_level']) > 0:
                print("\n\n\nInput from layer " + str(self.current_step) + " to layer " + str(self.current_step + 1) + ":")
        else:
            if self.config['verbose'] and int(self.config['log_level']) > 0:
                print("\n\n\nOutput (Layer " + str(self.current_step) + "): ")

        print(DataFrame(input_vector))

        # print(DataFrame(self.weights[self.current_step]))
        # Recursion happens here, if there is another layer, we need to go deeper
        if self.current_step < len(self.layers) - 1:
            #
            layer_output = np.dot(self.weights[self.current_step], input_vector)
            self.current_step += 1
            return self.compute_layer(self.activate(layer_output))

        return input_vector

    # Calculates the network's error.
    # TODO: right now, the output layer is 10 neurons, improve scalability
    def get_error(self, value, network_output):
        target = self.get_target_output(value)
        error = np.zeros(shape=(10, 1))
        if error.shape == network_output.shape:
            for i in range(0, 10):
                error[i, 0] = target[i, 0] - network_output[i, 0]
        else:
            print("Error shape:" + str(error.shape))
            print("Network output shape:" + str(network_output.shape))
            sys.exit("Error: Can't compute error because network output doesn't match standard output")

        return error

    # Simple function to get the wanted output as a matrix. Used to calculate error
    @staticmethod
    def get_target_output(value):
        if value > 9:
            sys.exit("Cannot get target output: Value is greater than 9")

        return_value = np.zeros(shape=(10, 1))
        for i in range(0, 10):
            if i is value:
                return_value[i, 0] += 1

        return return_value


