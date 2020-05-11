from functools import partial
from tkinter import filedialog as fd
from tkinter import*
import logging
import pickle
import os


# Execute Other Scripts
def call_upload_new_photos():
    os.system('python3 Upload_New_Photos.py')


def call_match_photos():
    os.system('python3 Match_Faces.py')


def call_update_training_set():
    os.system('python3 Update_Training_Set.py')


def call_deploy():
    os.system('python3 Deploy.py')


# add to the already existing training file
def append_training_file():
    file1 = open("/Users/alexjoslin/Documents/PycharmProjects/Face_Sorter/Sets/current_training_set", "w")
    file2 = open("/Users/alexjoslin/Documents/PycharmProjects/Face_Sorter/Sets/total_training_set", "a")
    for item in training_container:
        for photo in item:
            file1.write(photo + "\n")
            file2.write(photo + "\n")
    file1.close()
    file2.close()


def write_photos():
    with open("/Users/alexjoslin/Documents/PycharmProjects/Face_Sorter/Serialized/photos.pkl", "wb") as file:
        pickle.dump(upload_container, file)


# execute when finished
def done(window):
    global STATE
    append_training_file()
    write_photos()
    window.quit()
    window.destroy()
    STATE = False
    logging.info("complete, next event\n")


# execute if user wants to upload photos
def upload_photos():
    global PHOTOS_UPLOADED
    paths = fd.askopenfilenames(filetypes=[("jpeg", ".jpeg"), ("png", ".png"), ("jpg", ".jpg")])
    PHOTOS_UPLOADED = True
    upload_container.append(paths)
    logging.info("adding to photos")


# execute if user wants to update training
def update_training():
    global TRAINING_UPDATED
    paths = fd.askopenfilenames(filetypes=[("jpeg",".jpeg"), ("png",".png"), ("jpg",".jpg")])
    if paths != "":
        TRAINING_UPDATED = True
    training_container.append(paths)
    logging.info("adding to training")


def main():
    global STATE
    window = Tk()
    window.title("Face Sorter")
    window.geometry("200x150+600+200")

    # GUI BUTTOONS
    up_button = Button(window, text="upload photos", command=upload_photos)
    up_button.pack(pady=10, fill=X)
    tr_button = Button(window, text="update training set", command=update_training)
    tr_button.pack(pady=10, fill=X)
    done_button = Button(window, text="done", command=partial(done, window))
    done_button.pack(pady=10, fill=X)

    # Keep window open
    STATE = True
    while STATE:
        window.update()

    # Handle situtation if user presses one button and no the other
    if TRAINING_UPDATED and not PHOTOS_UPLOADED:
        call_update_training_set()
    elif TRAINING_UPDATED and PHOTOS_UPLOADED:
        call_update_training_set()
        call_upload_new_photos()
        call_match_photos()
        call_deploy()
    else:
        call_upload_new_photos()
        call_match_photos()
        call_deploy()


if __name__ == '__main__':
    # initialize vairables
    STATE = None
    upload_container = []
    training_container = []
    logging.basicConfig(filename="/Users/alexjoslin/Documents/PycharmProjects/Face_Sorter/Logs/text.log", level=logging.DEBUG, filemode=W,
                        format='%(filename)s\t|\t%(funcName)s\t|\t%(levelname)s: %(message)s')
    TRAINING_UPDATED = False
    PHOTOS_UPLOADED = False
    main()




