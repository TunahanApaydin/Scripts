import glob
import re
import os
from shutil import move
import xml.etree.ElementTree as ET

labelmap_list = ["car", "ir_car", "ir_light_car"]
move_path = "/home/tuna/Documents/Otopark/datas_with_labels/m/"

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def move_wrong_labeled_xml(xml):
    move(xml, move_path)

def compare_label_and_labelmap(xml, xml_lbls):
    for xml_lbl in xml_lbls:
        if xml_lbl in labelmap_list:
            continue
        else:
            move_wrong_labeled_xml(xml)
            print("moved: {}".format(xml))
            break

def get_labels_in_xml(xmls):
    print("Moving wrong labeled xml file operation is started")
    for xml in xmls:
        xml_lbls = []
        tree = ET.parse(xml)
        root = tree.getroot()
        objects = root.findall('object')
        for obj in objects:
            name = obj.find("name")
            class_name = name.text
            xml_lbls.append(class_name)

        compare_label_and_labelmap(xml, xml_lbls)
        print("------------")
    print("Moving wrong labeled xml file operation is finished")

if __name__ == "__main__":
    path = "/home/tuna/Documents/Otopark/datas_with_labels/deneme/"
    
    xmls = glob.glob(path + "*.xml")
    sorted_xmls = sorted(xmls, key =  numericalSort)
    get_labels_in_xml(sorted_xmls)