import re
import os
import glob

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def get_sorted_names(file_dir, extention):
    paths = glob.glob(file_dir + extention)
    sorted_files = sorted(paths, key = numericalSort)
    names = [(os.path.basename(os.path.splitext(name)[0])) for name in sorted_files]
    return names, sorted_files

current_path = os.getcwd()
folder_path = "/home/tuna/Desktop/bitirme_tezi/ByteTrack/datasets/test" # set folder "/home/tuna/Desktop/bitirme_tezi/ByteTrack/datasets/test"
label_names = get_sorted_names(folder_path, "/*.xml") # set file format

sorted_img_files = list()
images_path = glob.glob(folder_path + "/*.jpg")
sorted_img_files = sorted(images_path, key = numericalSort)

file_name = "test.txt" # set text file name

if os.path.exists(current_path + "/" + file_name):
    print("The file is already exist!")
else:
    try:
        with open(current_path + "/" + file_name, "a") as txtfile:
            print("Created a new file with name {}".format(file_name))
            txtfile.close()
    except:
        pass

for img_name in sorted_img_files:
    with open(file_name, "a") as txtfile:
        print("{} has been added to text file".format(img_name))
        txtfile.writelines(img_name + "\n") # use <label_name + ".xml" + "\n"> if you want to write exention
txtfile.close()
