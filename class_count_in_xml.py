# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
import glob
import xml.etree.ElementTree as ET


path = "/home/tuna/Documents/Otopark/datas_with_labels/dataset_v5/*.xml"
xml_files = glob.glob(path)

classes=[]

for xml_file in xml_files:
    
    tree = ET.parse(xml_file)
    myroot = tree.getroot()
    
    for etiket in myroot.iter('name'):
        sinif=(etiket.text)
        classes.append(sinif)

df=pd.DataFrame(classes,columns=["classes"])
df.groupby(classes).count()

plt.figure(figsize=(10,6))
sns.displot(df.classes)
plt.title("Dataset Classes Counts")
plt.xlabel("Class Names")
plt.xticks(rotation=45)
plt.ylabel("Counts")
plt.show()





