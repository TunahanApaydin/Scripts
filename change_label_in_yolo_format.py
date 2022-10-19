import os
import re
import glob
from dictionaries import getDictionary

class ChangeLabelNumber:
    def __init__(self):
        pass

    def numericalSort(self, value):
        numbers = re.compile(r'(\d+)')
        parts = numbers.split(value)
        parts[1::2] = map(int, parts[1::2])
        return parts

    def changeLabelNumber(self, data_path):
        print("Changing label for YOLO format is started!!")

        # dict = {
        #     "5" : "4",
        #     "4" : "8",
        #     "6" : "10",
        #     "10" : "2",
        #     "11" : "1",
        #     "3" : "5",
        #     "8" : "6",
        #     "0" : "18",
        #     "1" : "9",
        #     "7" : "3",
        #     "2" : "20",
        #     "9" : "0"
        # }

        # dict = {
        #     "11" : "0", # 2021 dataset için düzenlenecek
        #     "10" : "1",
        #     #" " : "2",
        #     "15" : "3",
        #     "14" : "4",
        #     "8" : "5",
        #     "9" : "6",
        #     "2" : "7",
        #     "4" : "8",
        #     "7" : "9",
        #     "0" : "10",
        #     "13" : "11",
        #     "3" : "12",
        #     "6" : "13",
        #     "16" : "14",
        #     "5" : "15",
        #     #" " : "16",
        #     #" " : "17",
        #     #" " : "18",
        #     #" " : "19",
        #     "17" : "20",
        #     "1" : "21"
        # }

        dict = {
            "4" : "4",
            "8" : "8",
            "10" : "10",
            "2" : "0",
            "1" : "2",
            "5" : "5",
            "6" : "6",
            "18" : "12",
            "9" : "9",
            "3" : "3",
            "20" : "20",
            "0" : "1"
        }

        #dict = getDictionary("pre_dict")

        lab_file = filter(os.path.isfile, glob.glob(data_path + "*.txt"))
        list_of_label_files = sorted(lab_file, key =  self.numericalSort)

        for txt in list_of_label_files:
            with open(txt, "r") as rtxt:
                lines = rtxt.readlines()
                # txt.close()

                with open(txt, "w") as wtxt:
                    for line in lines:
                        print("--------------")
                        class_number = line.split(" ")[0] # class numarasını al.
                        others = line.split(" ")[1:]

                        true_label =  dict[class_number]

                        others_str = " ".join(others)
                        new_line = true_label + " " + others_str

                        #write_txt = line.replace(line, new_line)
                        wtxt.write(new_line)
                        
                    wtxt.close()
            
        print("Changing label for YOLO format is finished!!")
                    
if __name__ == "__main__":
    compare = ChangeLabelNumber()
    data_path = "/home/tuna/Desktop/Ko-Drive/dataset/2021_labels_and_images/"
    compare.changeLabelNumber(data_path)