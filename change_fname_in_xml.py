import os
import glob
import xml.etree.ElementTree as ET

xml_path = "/home/kule/models/research/object_detection/images/test/tuna_001459.xml"

tree = ET.parse(xml_path)
root = tree.getroot()

paths_in_file = root.findall("path")

for path in paths_in_file:
    text = path.text
    splited_path = text.split("/")
    new_path = splited_path[0] + "/" +  splited_path[1] + "/" + "tuna_" + splited_path[2]
    path.text = new_path
    path.set("path", "yes")
    print(path.text)
    
tree.write(splited_path[2])

if __name__ == "__main__":
    pass