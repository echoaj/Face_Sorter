from face_recognition import*
import pickle
import os


def write_photo_encodings():
    with open("/Users/alexjoslin/Documents/PycharmProjects/Face_Sorter/Serialized/photo_encodings.pkl", "wb") as file:
        pickle.dump(data_encodings, file)


# convert to photos to their encodings
def convert_to_encodings(new_photos):
    """
    The photos.pkl package only a list of
    tuples containing photo paths
    """
    for tup in new_photos:
        for path in tup:
            image = load_image_file(path)
            encoding = face_encodings(image)[0]
            # os.path.split splits a path into its HEAD and TAIL
            # -->  head[0] (path not including name)
            # -->  tail[1] (name including extension)
            name = os.path.split(path)[1]
            data_encodings.append([encoding, name, path])     #encodings, name, path


# opening file with photo paths
def open_photos():
    with open("/Users/alexjoslin/Documents/PycharmProjects/Face_Sorter/Serialized/photos.pkl", "rb") as file:
        photos = pickle.load(file)
        convert_to_encodings(photos)


def main():
    open_photos()
    write_photo_encodings()


if __name__ == '__main__':
    data_encodings = []
    main()
