import re
import os
import glob

"""
r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
a: open an existing file for append operation. It wont override existing data.
r+: To read and write data into the file. The previous data in the file will not be deleted.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It wont override existing data.
"""

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def get_sorted_names(file_dir, extention):
    paths = glob.glob(file_dir + extention)
    sorted_files = sorted(paths, key = numericalSort)
    names = [(os.path.basename(os.path.splitext(name)[0])) for name in sorted_files]
    return names

current_path = os.getcwd()
labels_path = "/home/tuna/Desktop/scripts/train" # set folder
label_names = get_sorted_names(labels_path, "/*.xml") # set file format 
file_name = "train_list.txt" # set text file name

if os.path.exists(current_path + "/" + file_name):
    print("The file is already exist!")
else:
    try:
        with open(current_path + "/" + file_name, "a") as txtfile:
            print("Created a new file with name {}".format(file_name))
            txtfile.close()
    except:
        pass

for label_name in label_names:
    with open(file_name, "a") as txtfile:
        print("{} has been added to text file".format(label_name))
        txtfile.writelines(label_name + ".xml" + "\n") # use <label_name + ".xml" + "\n"> if you want to write exention
txtfile.close()
