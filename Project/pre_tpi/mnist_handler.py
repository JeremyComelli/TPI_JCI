import sys

class MNIST:
    def __init__(self, training, path):
        self.training = training
        if self.training:
            self.labels_path = path + "\\training\\labels.idx1-ubyte"
            self.data_path = path + "\\training\\data.idx3-ubyte"
        else:
            self.labels_path = path + "\\test\\labels.idx1-ubyte"
            self.data_path = path + "\\test\\data.idx3-ubyte"

        print("Data Path: " + self.labels_path)
        print("Labels Path: " + self.data_path + "\n\n")

        self.data = open(self.data_path, "rb")
        self.labels = open(self.labels_path, "rb")

    def print_data(self):
        i = 0
        y = 0
        line = ""
        counter = 0

        # Ignoring the first 16 bytes of the data file, which is metadata
        self.data.seek(16)

        # Ignoring the first 8 bytes of the labels file, which is metadata
        self.labels.seek(8)

        # Looping trough the bytes of data, to print an output
        for image_byte in self.data.read():
            if i < 27:
                # The spaces are required for output formatting
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

                #this is ugly, but works for some reason
                for label in self.labels.read(1):
                    print("Answer: " + str(label))
                y = 0


