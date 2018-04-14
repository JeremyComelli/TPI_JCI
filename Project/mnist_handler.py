import sys
import struct
import os


class MNIST:
    def __init__(self, training, path, limit=0):

        if limit is not 0:
            self.limit = limit
            print("Counter exists")
            self.counter = 0
        else:
            self.counter = -1

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

        '''image_id, image = self.get_image(12)
        print("Image Value: " + str(image_id))
        self.print_image(image)'''

    def read_file(self):
        # TODO: récupérer le nombre d'images dans les 16 premiers bytes, et mettre une limite
        print("Processing files, please wait...")
        # Opening files
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
                if self.counter <= self.limit:
                    # Each pixel is mapped to a decimal value between 0.0 and 0.254
                    chunk.append(pixel/1000)
                    if len(chunk) > 783:
                        if self.counter > -1:
                            self.counter += 1
                        label = int.from_bytes(labels_file.read(1), byteorder='big')
                        entry = [label, chunk]
                        self.data.append(entry)
                        chunk = list()
                else:
                    break
        else:
            sys.exit("Training File or Label File missing")

        labels_file.close()
        data_file.close()

    def print_image(self, image_id):
        value, image = self.get_image(image_id)
        line = list()
        i = 0

        print("\n\nImage #" + str(image_id) + ", Value: " + str(value) + "\n")
        for pixel in image:
            # For readability, pixel is converted from float to int
            pixel = int(pixel * 1000)
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

    # Returns an array of 2 values, image ID, and actual image
    def get_image(self, image_id=0):
        if image_id is 0:
            image_id = int(input("image_id: "))
        elif image_id > len(self.data):
            sys.exit("Image index out of range")
        return self.data[image_id][0], self.data[image_id][1]
