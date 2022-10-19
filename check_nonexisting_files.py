import os
import re
import glob
from shutil import move

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

    def compareFiles(self, data_path, move_path):
        print("Moving nonexisting file operation started!!")
        #img_file = filter(os.path.isfile, glob.glob(data_path + "*.jpg"))
        lab_file = filter(os.path.isfile, glob.glob(data_path + "*.xml"))
        
        extentions = ['png', 'jpg', 'jpeg']
        files = []
        [files.extend(glob.glob(data_path + '*.' + e)) for e in extentions]
        
        list_of_img_files = sorted(files, key =  self.numericalSort)
        list_of_label_files = sorted(lab_file, key =  self.numericalSort)

        # for img_name in list_of_img_files:
        #     name = os.path.basename(os.path.splitext(img_name)[0])
        #     #print(name)
        
        image_name = [(os.path.basename(os.path.splitext(img_name)[0])) for img_name in list_of_img_files]
        ext = [(os.path.basename(os.path.splitext(img_name)[1])) for img_name in list_of_img_files]
        label_name = [(os.path.basename(os.path.splitext(lab_name)[0])) for lab_name in list_of_label_files]
        
        list_of_nonexist_files = []
        for label in label_name:
            for i, image in enumerate(image_name):
                if image != label:
                    continue
                else:
                    if ext[i] == ".jpg":
                        move(data_path + image + ".jpg", move_path)
                    elif ext[i] == ".jpeg":
                        move(data_path + image + ".jpeg", move_path)
                    elif ext[i] == ".png":
                        move(data_path + image + ".png", move_path)
                        
                    move(data_path + label + ".xml", move_path)
                    break
        print("Moving nonexisting file operation finished!!")
                    
if __name__ == "__main__":
    compare = CompareFileNames()
    data_path = "/home/tuna/Documents/Otopark/datas_with_labels/dataset_v5/"
    move_path = "/home/tuna/Documents/Otopark/datas_with_labels/move/"
    lbl_pth = "/home/tuna/Desktop/Otopark/datas_with_labels/tuna2/2_labels/*.xml"
    img_pth = "/home/tuna/Desktop/Otopark/datas_with_labels/tuna2/2/*.jpg"
    compare.compareFiles(data_path, move_path)
    
    # label_dir = "/home/kule/Desktop/otopark/datas/renamed_labels"
    # image_dir = "/home/kule/Desktop/otopark/Yolo2Pascal-annotation-conversion/demo/yolo2pascal/images"
    # extention = ["/*.txt", "/*.jpg"]
    # save_label_dir = "/home/kule/Desktop/otopark/datas/renamed_labels_2/"
    # save_image_dir = "/home/kule/Desktop/otopark/datas/renamed_images_2/"
    # compare.renameFiles(label_dir, extention[0], save_label_dir) #change all of them: xxx_dir - extention[x] - save_xxx_dir