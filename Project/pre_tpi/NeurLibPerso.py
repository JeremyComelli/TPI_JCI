import numpy


class NeuralNetwork:
    # stuff of dreams
    def __init__(self, input_layer, hidden_layer, output_layer):
        # set neural network specs from input
        # this is a three layered neural network, but in the end, we should be able to specify n number of layers through a matrix
        self.input_layer_size = input_layer
        self.hidden_layer_size = hidden_layer
        self.output_layer_size = output_layer

        self.first_layer = ()
        for i in range(0, self.input_layer):

            neuron = Perceptron(numpy.matrix('1 1 1 1'), 0)
            self.first_layer.append(    )


class Perceptron:

    def __init__(self, input_matrix, layer_id):
        # Perceptron receives a matrix as input. Each line represents a weight,
        # and the last row is the bias

        # Layer ID: 0 -> Input | 1 -> Hidden | 2-> Output
        self.layer = layer_id
        self.bias = input_matrix.item(input_matrix.size-1)

        # If layer is 0, it means it's the input layer; therefore, there is one weight, which is 1
        if self.layer == 0:
            self.weights = numpy.matrix('1')
        else:
            self.weights = input_matrix.item
        print(input_matrix.size)

        for i in range(0, input_matrix.size-1):
            print(i)
            self.weights.append(input_matrix.item(0, i))

        print("bias =" + str(self.bias))
        print("Weights =" + str(self.weights))

    def compute(self):
        # Here lies the real part of the Algorithm.
        # The neuron takes current input, weights and bias, a sigmoid activation function,
        # shakes everything together and returns an output smoothie

        # Neuron algorithm: Sig(W1 * I1 + Bias)
        print("test")

        return 1


