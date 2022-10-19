import os
import re
import glob
from shutil import copyfile

class CompareSampleRename:
    def __init__(self):
        self.format = "label"
        self.img_file_extension = ["*.jpg", ".jpg"]
        self.label_file_extension = ["*.txt", ".txt"]
        self.sample_number = 3
        self.images_path = "/home/tuna/Desktop/d/image_2/*.jpg"
        self.new_images_path = "/home/tuna/Desktop/d/new/"
        self.labels_path = "/home/tuna/Desktop/d/label_2/*.txt"
        self.new_labels_path = "/home/tuna/Desktop/d/new/"
    
    def definePaths(self):
        images_paths = [self.images_path, self.new_images_path, self.img_file_extension]
        label_paths = [self.labels_path, self.new_labels_path, self.label_file_extension]

        
        if self.format == "image":
            self.takeSample(images_paths)
            self.renameFiles(images_paths)
        else:
            self.takeSample(label_paths)
            self.renameFiles(label_paths)

    def numericalSort(self, value):
        numbers = re.compile(r'(\d+)')
        parts = numbers.split(value)
        parts[1::2] = map(int, parts[1::2])
        return parts

    def takeSample(self, paths):
        list_of_files = filter(os.path.isfile, glob.glob(paths[0])) # d1

        list_of_files = sorted(list_of_files, key =  self.numericalSort)
        list_of_files = list_of_files[::self.sample_number] #number of the samples
        #print(list_of_files)
        
        for item in list_of_files:
            filename = os.path.basename(item)
            copyfile(item, os.path.join(paths[1], filename)) # d2

    def renameFiles(self, paths):
        list_of_new_files = filter(os.path.isfile, glob.glob(paths[1] + paths[2][0])) # d3 - d4
        list_of_new_files = sorted(list_of_new_files, key =  self.numericalSort)

        count = 0
        for file in list_of_new_files:
            path_name = paths[1] # d5
            new_name = path_name + "0"*(6-len(str(int(count))))+str(int(count)) + paths[2][1] # d6
            os.rename(file, new_name)
            count += 1

    def compareFiles(self, paths):
        img_file = filter(os.path.isfile, glob.glob(paths[0]))
        lab_file = filter(os.path.isfile, glob.glob(paths[0]))

        list_of_img_files = sorted(img_file, key =  self.numericalSort)
        list_of_label_files = sorted(lab_file, key =  self.numericalSort)

        # for img_name in list_of_img_files:
        #     name = os.path.basename(os.path.splitext(img_name)[0])
        #     #print(name)
        
        image_name = [(os.path.basename(os.path.splitext(img_name)[0])) for img_name in list_of_img_files]
        label_name = [(os.path.basename(os.path.splitext(lab_name)[0])) for lab_name in list_of_label_files]

        for label in label_name:
            for image in image_name:
                if label == image:
                    copyfile(lbl_pth + label + ".txt", dst_lbl_pth + label + ".txt")
                    copyfile(img_pth + label + ".jpg", dst_img_pth + label + ".jpg")

if __name__ == "__main__":
    sp = CompareSampleRename()
    sp.definePaths()
