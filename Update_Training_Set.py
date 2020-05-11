import pickle
from face_recognition import*
import os


# deploy training encodings
def write_encodings():
    with open("/Users/alexjoslin/Documents/PycharmProjects/Face_Sorter/Serialized/train_encodings.pkl", "wb") as file:
        pickle.dump(data_encodings, file)


# convert to training images to their encodings
def convert_to_encodings(path):
    image = load_image_file(path)
    encoding = face_encodings(image)[0]
    # os.path.split splits a path into its HEAD and TAIL
    # -->  head[0] (path not including name)
    # -->  tail[1] (name including extension)
    name = os.path.split(path)[1]  # head[0], tail[1]
    data_encodings.append([encoding, name, path])


# open training set
def load_file():
    with open("/Users/alexjoslin/Documents/PycharmProjects/Face_Sorter/Sets/current_training_set", "r") as file:
        for line in file:
            line = line.strip("\n")
            convert_to_encodings(line)


def main():
    load_file()
    write_encodings()


if __name__ == '__main__':
    data_encodings = []
    main()

