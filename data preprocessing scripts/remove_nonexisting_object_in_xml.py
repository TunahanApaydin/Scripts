from shutil import move
import glob
import os
import xml.etree.ElementTree as ET

def getNonexistingObject(xmls, images, move_path):
    print("Moving nonexisting object in xml file operation started!!")
    for xml, image in zip(xmls, images):
        tree = ET.parse(xml)
        root = tree.getroot()

        objects = root.findall("object")

        if len(objects) == 0:
            
            head_tail = os.path.splitext(xml)
            head = head_tail[0]
            image_path = head + ".jpg"
            move(xml, move_path)
            move(image_path, move_path)
    print("Moving nonexisting object in xml file operation finished!!")

if __name__ == "__main__":
    folder_path = "/home/tuna/Documents/Otopark/datas_with_labels/dataset_v2/"
    move_path = "/home/tuna/Documents/Otopark/datas_with_labels/move/"
    xmls = glob.glob(folder_path + "*.xml")
    images = glob.glob(folder_path + "*.jpg")
    getNonexistingObject(xmls, images, move_path)