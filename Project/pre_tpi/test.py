from pre_tpi import NeurLibPerso
from pre_tpi import mnist_handler as mnistReader
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
    print("Error, missing argument")




else:
    # Load data
    data_path = sys.argv[1] + "\\data.idx3-ubyte"
    labels_path = sys.argv[1] + "\\labels.idx1-ubyte"
    mode = sys.argv[2]

print("\nData path: " + data_path)
print("\nLabels path: " + labels_path + "\n")

data = open(data_path, "rb")
labels = open(labels_path, "rb")

i = 0
y = 0
line = ""
counter = 0

# Ignoring the first 16 bytes, which are metadata
data.seek(16)

# Looping trough the bytes of data, to print an output
for image_byte in data.read():
    if i < 27:
        # The spaces are required for formatting the output
        first_space = " "
        if image_byte < 10:
                first_space = "   "
        elif image_byte < 100:
                first_space = "  "

        line += first_space + str(image_byte)
        i += 1
    else:
        i = 0
        print(line)
        line = ""
        y += 1

    if y > 27:
        counter += 1
        print("\n\nImage " + str(counter) + "\n")
        y = 0



# print(str(image_byte))
# np.random.seed(12)

# Setting the print precision to 3, to get simpler readings
# np.set_printoptions(precision=3)

#  Suppresses scientific notation for small values, because I'm lazy and don't want to think
# np.set_printoptions(suppress=True)

# nn = NeurLibPerso.NeuralNetwork(10, 10, 1)

# print("\n\nOutput from first layer:")
# print(DataFrame(nn.compute(nn.input_values, nn.weights_ih)))
