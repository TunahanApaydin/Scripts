import os
import glob
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

class LabelCount:
    def __init__(self):
        self.number_of_car = 0
        self.number_of_ir_car = 0
        self.number_of_bus = 0
        self.number_of_truck = 0
        self.number_of_ir_light_car = 0
        self.number_of_ir_bus = 0
        self.number_of_ir_truck = 0
        self.number_of_motorcycle = 0
        self.number_of_ir_motorcycle = 0

    def get_labels_count(self, path):
        tree = ET.parse(path)
        root = tree.getroot()

        objects = root.findall("object")

        for object in objects:
            label_name = object[0].text

            if label_name == "car":
                self.number_of_car += 1
            elif label_name == "ir_car":
                self.number_of_ir_car += 1
            elif label_name == "ir_light_car":
                self.number_of_ir_light_car += 1
            elif label_name == "bus":
                self.number_of_bus += 1
            elif label_name == "ir_bus":
                self.number_of_ir_bus += 1
            elif label_name == "motorcycle":
                self.number_of_motorcycle += 1
            elif label_name == "ir_motorcycle":
                self.number_of_ir_motorcycle += 1
            elif label_name == "ir_truck":
                self.number_of_ir_truck += 1
            else:
                self.number_of_truck += 1

    def visualize_label_count(self):
        counts = [self.number_of_car, self.number_of_ir_car,  self.number_of_ir_light_car, self.number_of_bus, self.number_of_ir_bus, self.number_of_motorcycle, self.number_of_ir_motorcycle, self.number_of_truck, self.number_of_ir_truck ]
        langs = ['car', 'ir_car', 'ir_light_car', 'bus', 'ir_bus', 'motorcycle', 'ir_motorcycle', 'truck', 'ir_truck']
        self.number_of_bus += 1
        plt.bar(langs, counts)
        plt.xlabel("class names")
        plt.ylabel("total number of classes")
        plt.show()

if __name__ == "__main__":
    LC = LabelCount()

    parent_dir = "/home/tuna/Documents/Otopark/datas_with_labels/dataset_v2/"
    list_subfolders_with_paths = [f.path for f in os.scandir(parent_dir) if f.is_dir()]

    if list_subfolders_with_paths is None:
        for child_dir in list_subfolders_with_paths:
            xml_paths = glob.glob(child_dir + "/*.xml")
            for xml_path in xml_paths:
                LC.get_labels_count(xml_path)
    else:
        xml_paths = glob.glob(parent_dir + "*.xml")
        for xml_path in xml_paths:
            LC.get_labels_count(xml_path)

    print("car: {}".format(LC.number_of_car))
    print("person: {}".format(LC.number_of_ir_car))
    print("bus: {}".format(LC.number_of_ir_light_car))
    print("truck: {}".format(LC.number_of_bus))
    print("car: {}".format(LC.number_of_ir_bus))
    print("person: {}".format(LC.number_of_motorcycle))
    print("bus: {}".format(LC.number_of_ir_motorcycle))
    print("truck: {}".format(LC.number_of_truck))
    print("truck: {}".format(LC.number_of_ir_truck))
    print("Total: {}".format(LC.number_of_car+LC.number_of_ir_car+LC.number_of_ir_light_car+LC.number_of_bus+LC.number_of_ir_bus+LC.number_of_motorcycle+LC.number_of_ir_motorcycle+LC.number_of_truck+LC.number_of_ir_truck))

    LC.visualize_label_count()