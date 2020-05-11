import pickle
import os

# moves photos to their proper folder
def sort_photos(package):
    """
    :param package -> [[folder_name, [MATCHED, photo_name, photo_path]]]:
    """
    destination = "/Users/alexjoslin/Desktop/sorted"
    if not os.path.exists(destination):
        os.mkdir(destination)

    for folder in package:
        folder_destination_name = destination + '/' + folder[0]
        if not os.path.exists(folder_destination_name):
            os.mkdir(folder_destination_name)

        count = 1
        for group in folder[1]:
            location = folder_destination_name + '/' + group[0]
            if not os.path.exists(location):
                os.rename(group[1], location)
            else:
                location = location + f' copy({count})'
                os.rename(group[1], location)
                count += 1


# load package with matching faces and their paths
def load_package():
    with open("/Users/alexjoslin/Documents/PycharmProjects/Face_Sorter/Serialized/package.pkl", "rb") as file:
        package = pickle.load(file)
    return package


def main():
    pack = load_package()
    sort_photos(pack)


if __name__ == '__main__':
    main()
