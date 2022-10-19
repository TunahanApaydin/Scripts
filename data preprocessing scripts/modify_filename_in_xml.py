'''
Bu script bir jpg image dosyasinin adini alir ve ona ait olan xml etiket dosyasi içindeki 'filename'
'''


import glob
import os
import re
import xml.etree.ElementTree as ET

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

path = "/home/tuna/Documents/Otopark/datas_with_labels/dataset_v2/"
xmls = glob.glob(path + "*.xml")
sorted_xmls = sorted(xmls, key =  numericalSort)

print("Modifing xml file operation is started''")
for xml in sorted_xmls:
    head_tail = os.path.split(xml)
    name = head_tail[1]
    name = name.rsplit('.', 1)[0]

    tree = ET.parse(xml)
    root = tree.getroot()
    text = root.find('filename')
    text.text = name + ".jpg"
    
    tree.write(xml)
print("Modifing xml file operation is finished''")