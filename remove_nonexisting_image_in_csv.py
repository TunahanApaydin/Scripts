import pandas as pd
import glob
import os
import re

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def remove(sorted_image_names, sorted_image_names_in_csv):
    
    print(list)
    
csv_path = "/home/kule/Desktop/otopark/scripts/test_labels.csv"
df = pd.read_csv(csv_path)
image_names_in_csv = df["filename"].values
sorted_image_names_in_csv = sorted(image_names_in_csv, key =  numericalSort)
sorted_image_names_in_csv = list(set(sorted_image_names_in_csv))

image_path = "/home/kule/Desktop/otopark/scripts/test/"
extentions = ["*.jpg", "*.jpeg", "*.png"]
for ext in extentions:
    image_names = glob.glob(image_path + ext)
    sorted_image_names = sorted(image_names, key =  numericalSort)
    for name in sorted_image_names:
        head_tail = os.path.split(name)
        name = head_tail[1]
        for name_csv in sorted_image_names_in_csv:
            if name == name_csv:
                continue     
            else:
                list = df.loc[df['filename'] == name_csv].values
                break

    print(list)


# l = list(frozenset(sorted_image_names).intersection(sorted_image_names_in_csv))
# print(l)
