import sys
import struct


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

        self.data = list()
        self.read_file()

    def read_file(self, limit=0):
        # TODO: récupérer le nombre d'images dans les 16 premiers bytes, et mettre une limite
        print("Processing files, please wait...")
        # Open files
        data_file = open(self.data_path, "rb")
        labels_file = open(self.labels_path, "rb")

        # Ignoring the first 16 bytes of the data file, which is metadata
        data_file.seek(16)

        labels_file.seek(8)

        # Reading chunks of 784 bytes, each of which represents one image
        # We then add each entry to a list, which will contain all data and all labels
        chunk = list()
        for pixel in data_file.read():
            chunk.append(pixel)
            if len(chunk) > 783:
                label = int.from_bytes(labels_file.read(1), byteorder='big')
                entry = [label, chunk]
                self.data.append(entry)
                chunk = list()
        id = int(input("ID: "))
        self.print_image(self.data[id][1])
        print("Value: " + str(self.data[id][0]))

    @staticmethod
    def print_image(image):
        line = list()
        i = 0

        for pixel in image:
            space = ""
            if pixel < 10:
                space = "  "
            elif pixel < 100:
                space = " "
            line.append(space + str(pixel))
            i += 1
            if i > 27:
                print(line)
                line = list()
                i = 0


