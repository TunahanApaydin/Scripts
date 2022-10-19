import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join

classes = ['car', 'ir_car', 'ir_light_car', 'bus', 'ir_bus', 'motorcycle', 'ir_motorcycle', 'truck', 'ir_truck']
counter = [0]*(len(classes))
classCounterDict ={}

def getLabelsInDir(dir_path):
    lable_name_list = []
    for filename in glob.glob(dir_path + '/*.xml'):
        lable_name_list.append(filename)

    return lable_name_list

def convert_annotation(dir_path, label_path):
    global counter

    basename = os.path.basename(label_path)
    basename_no_ext = os.path.splitext(basename)[0]

    in_file = open(dir_path + '/' + basename_no_ext + '.xml')
    tree = ET.parse(in_file)
    root = tree.getroot()
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes: #or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        counter[cls_id] += 1

cwd = getcwd()

labels_path = r"/home/tuna/Desktop/Otopark/datas_with_labels/full_dataset"

label_paths = getLabelsInDir(labels_path)
list_file = open(labels_path + 'ClassCounts.txt', 'w')

for label_path in label_paths:
    try:
        convert_annotation(labels_path, label_path)
    except:
        pass


for idx in range(0,len(classes)):
    classCounterDict[classes[idx]]=counter[idx]

print("Finished processing" )
print("Count of classes:" )


for k, v in classCounterDict.items():
    list_file.write(k+ " = " +str(v) + '\n')
    print(k, v)
list_file.close()