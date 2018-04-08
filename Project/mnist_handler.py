import sys
import struct
import os


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

        image_id, image = self.get_image(12)
        print(image_id)
        self.print_image(image)

    def read_file(self, limit=0):
        # TODO: récupérer le nombre d'images dans les 16 premiers bytes, et mettre une limite
        print("Processing files, please wait...")
        # Open files
        if os.path.isfile(self.data_path) and os.path.isfile(self.labels_path):
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
        else:
            sys.exit("Training File or Label File missing")

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

    # Returns an array of 2 values, image numeric, and actual image
    def get_image(self, image_id=0):
        if image_id is 0:
            image_id = int(input("image_id: "))
        return self.data[image_id][0], self.data[image_id][1]
