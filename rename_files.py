import os
import re
import glob
from shutil import copyfile, copy

class CompareFileNames:
    def __init__(self):
        pass

    def numericalSort(self, value):
        numbers = re.compile(r'(\d+)')
        parts = numbers.split(value)
        parts[1::2] = map(int, parts[1::2])
        return parts

    def get_sorted_files(self, file_dir):
        list_subfolders_with_paths = [f.path for f in os.scandir(file_dir) if f.is_dir()]
        sorted_subfolders = sorted(list_subfolders_with_paths, key =  self.numericalSort)
        return sorted_subfolders

    def get_sorted_names(self, file_dir, extention):
        paths = glob.glob(file_dir + extention)
        sorted_files = sorted(paths, key = self.numericalSort)
        names = [(os.path.basename(os.path.splitext(name)[0])) for name in sorted_files]
        return names

    def rename_file_names(self, file_dir, extention, save_dir):   
        sorted_subfolders = self.get_sorted_files(file_dir)
        
        count = 0
        for file_child_dir in sorted_subfolders:
            label_names = self.get_sorted_names(file_child_dir, "/*.jpg") # change
            files = glob.glob(file_child_dir + extention)
            files = sorted(files, key =  self.numericalSort)
            
            for i, file in enumerate(files):
                
                #file2 = save_dir +label_names[i] + ".jpg" # change
                new_name = save_dir + "tuna5_" + "0"*(6-len(str(int(count))))+str(int(count)) + ".jpg" # change
                #os.rename(file2, new_name)
                #copyfile(file, save_dir + label_names[i] +".xml") # change
                copyfile(file, new_name)
                count += 1
            print("Files in subfolder {} renamed".format(file_child_dir))
      

if __name__ == "__main__":
    compare = CompareFileNames()
    label_dir = "/home/tuna/Documents/Otopark/datas_with_labels/2/"
    image_dir = "/home/tuna/Documents/Otopark/datas_with_labels/2/"
    extention = ["/*.xml", "/*.jpg"]
    save_label_dir = "/home/tuna/Documents/Otopark/datas_with_labels/move/"
    save_image_dir = "/home/tuna/Documents/Otopark/datas_with_labels/move/"
    compare.rename_file_names(image_dir, extention[1], save_image_dir) #change all of them: xxx_dir - extention[x] - save_xxx_dir
