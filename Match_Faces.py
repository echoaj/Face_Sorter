from face_recognition import*
import pickle


def write_package(package):
    with open("/Users/alexjoslin/Documents/PycharmProjects/Face_Sorter/Serialized/package.pkl", "wb") as file:
        pickle.dump(package, file)


# compare trainig encodings to new photo encodings
def compare_images(training_encodings, new_photo_encodings):
    """
    :param: training_encodings   - > [[encoding, name, path]...]
    :param: new_photo_encodings  - > [[encoding, name, path]...]
    """
    package = []
    for train_list in training_encodings:
        group = []
        for photo_list in new_photo_encodings:
            train_encoding = train_list[0]      # [0] => encoding
            photo_encoding = photo_list[0]     # [0] => encoding
            train_name = train_list[1]          # [1] => name
            photo_name = photo_list[1]# [1] => name
            photo_path = photo_list[2]# [2] => path

            results = compare_faces([train_encoding], photo_encoding)        # compare encodings
            if results[0]:                                                  # case if they match
                group.append([photo_name, photo_path])

        if len(group) != 0:
            folder_name = train_name.strip(".jpg").strip(".jpeg").strip(".png")
            package.append([folder_name, group])
    return package


# open training encodings
def open_train_encodings():
    with open("/Users/alexjoslin/Documents/PycharmProjects/Face_Sorter/Serialized/train_encodings.pkl", "rb") as file:
        training_encodings = pickle.load(file)
    return training_encodings


# open photo encodings
def open_photo_encodings():
    with open("/Users/alexjoslin/Documents/PycharmProjects/Face_Sorter/Serialized/photo_encodings.pkl", "rb") as file:
        training_encodings = pickle.load(file)
    return training_encodings


def main():
    te = open_train_encodings()
    pe = open_photo_encodings()
    pack = compare_images(te, pe)
    write_package(pack)


if __name__ == '__main__':
    main()

