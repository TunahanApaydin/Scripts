import os
import glob
import cv2
import matplotlib.pyplot as plt
import time
import codecs
import numpy as np

def colormap(rgb=False):
    color_list = np.array(
        [
            0.000, 0.447, 0.741,
            0.850, 0.325, 0.098,
            0.929, 0.694, 0.125,
            0.494, 0.184, 0.556,
            0.466, 0.674, 0.188,
            0.301, 0.745, 0.933,
            0.635, 0.078, 0.184,
            0.300, 0.300, 0.300,
            0.600, 0.600, 0.600,
            1.000, 0.000, 0.000,
            1.000, 0.500, 0.000,
            0.749, 0.749, 0.000,
            0.000, 1.000, 0.000,
            0.000, 0.000, 1.000,
            0.667, 0.000, 1.000,
            0.333, 0.333, 0.000,
            0.333, 0.667, 0.000,
            0.333, 1.000, 0.000,
            0.667, 0.333, 0.000,
            0.667, 0.667, 0.000,
            0.667, 1.000, 0.000,
            1.000, 0.333, 0.000,
            1.000, 0.667, 0.000,
            1.000, 1.000, 0.000,
            0.000, 0.333, 0.500,
            0.000, 0.667, 0.500,
            0.000, 1.000, 0.500,
            0.333, 0.000, 0.500,
            0.333, 0.333, 0.500,
            0.333, 0.667, 0.500,
            0.333, 1.000, 0.500,
            0.667, 0.000, 0.500,
            0.667, 0.333, 0.500,
            0.667, 0.667, 0.500,
            0.667, 1.000, 0.500,
            1.000, 0.000, 0.500,
            1.000, 0.333, 0.500,
            1.000, 0.667, 0.500,
            1.000, 1.000, 0.500,
            0.000, 0.333, 1.000,
            0.000, 0.667, 1.000,
            0.000, 1.000, 1.000,
            0.333, 0.000, 1.000,
            0.333, 0.333, 1.000,
            0.333, 0.667, 1.000,
            0.333, 1.000, 1.000,
            0.667, 0.000, 1.000,
            0.667, 0.333, 1.000,
            0.667, 0.667, 1.000,
            0.667, 1.000, 1.000,
            1.000, 0.000, 1.000,
            1.000, 0.333, 1.000,
            1.000, 0.667, 1.000,
            0.167, 0.000, 0.000,
            0.333, 0.000, 0.000,
            0.500, 0.000, 0.000,
            0.667, 0.000, 0.000,
            0.833, 0.000, 0.000,
            1.000, 0.000, 0.000,
            0.000, 0.167, 0.000,
            0.000, 0.333, 0.000,
            0.000, 0.500, 0.000,
            0.000, 0.667, 0.000,
            0.000, 0.833, 0.000,
            0.000, 1.000, 0.000,
            0.000, 0.000, 0.167,
            0.000, 0.000, 0.333,
            0.000, 0.000, 0.500,
            0.000, 0.000, 0.667,
            0.000, 0.000, 0.833,
            0.000, 0.000, 1.000,
            0.000, 0.000, 0.000,
            0.143, 0.143, 0.143,
            0.286, 0.286, 0.286,
            0.429, 0.429, 0.429,
            0.571, 0.571, 0.571,
            0.714, 0.714, 0.714,
            0.857, 0.857, 0.857,
            1.000, 1.000, 1.000
        ]
    ).astype(np.float32)
    color_list = color_list.reshape((-1, 3)) * 255
    if not rgb:
        color_list = color_list[:, ::-1]
    return color_list

start_time = time.time()
curFolder = r'/home/tuna/Desktop/Ko-Drive/dataset/2021_labels_and_images'
#curFolder = os.path.dirname(os.path.abspath(_file_))  # This is your Project Root
textFilePath = curFolder + "/"
imageFilePath = curFolder + "/*.jpg"

dict = {
            "0" : "Yesil_Isik",
            "1" : "Kirmizi_Isik",
            "2" : "Sari_Isik",
            "3" : "Park_Yapilabilir",
            "4" : "Durak_Isarati",
            "5" : "Saga_Donulmez",
            "6" : "Sola_Donulmez",
            "7" : "Ileri_ve_Sola_Donus",
            "8" : "Sola_Mecburi_Donus",
            "9" : "Saga_Mecburi_Donus",
            "10" : "Girilmez",
            "11" : "Dur",
            "12" : "Ileri_ve_Saga_Donus",
            "13" : "Azami_Hiz_20",
            "14" : "Hiz_Sinirlamasi_Sonu_20",
            "15" : "Azami_Hiz_30",
            "16" : "Hiz_Sinirlamasi_Sonu_30",
            "17" : "Azami_Hiz_50",
            "18" : "Hiz_Sinirlamasi_Sonu_50",
            "19" : "Ters_Tabela",
            "20" : "Park_Yapilmaz",
            "21" : "Sinirlamalarin_Sonu"
        }

imageContent = glob.glob(imageFilePath)
print(imageContent)
AnnIDs = 0
for x in range(0, len(imageContent)):
    print("CurrIm: {} --- TotalIm: {}".format(x, len(imageContent)))
    print(curFolder+"/isaretlemeler/"+os.path.basename(imageContent[x])[0:-4]+".jpg")
    img = cv2.imread(imageContent[x])
    temp_image = img
    ImHeight, ImWidth, channels = img.shape
    #print(ImHeight,ImWidth)
    if not (os.path.isfile(textFilePath+os.path.basename(imageContent[x])[0:-4]+".txt")):
        print(textFilePath+os.path.basename(imageContent[x])[0:-4]+"txt")
        print("cant read")
        continue
    currFile = codecs.open(textFilePath+os.path.basename(imageContent[x])[0:-4]+".txt", encoding='utf-8-sig')
    #currFile = open(textFilePath+os.path.basename(imageContent[x])[0:-4]+".txt","r")

    for line in currFile:
        line_element = line.split(" ")
        category_id = int(line_element[0])
        #if not(category_id == 0 or category_id == 8):
        #    continue
        bbox_width = round(float(line_element[3]) * ImWidth)
        bbox_height = round(float(line_element[4]) * ImHeight)
        bbox_x = round((float(line_element[1]) * ImWidth) - (bbox_width / 2))
        bbox_y = round((float(line_element[2]) * ImHeight) - (bbox_height / 2))
        bbox = [bbox_x, bbox_y, bbox_width, bbox_height]

        color_list = colormap()
        color = tuple(color_list[category_id].reshape(1, -1)[0])
        r = int(color[0])
        g = int(color[1])
        b = int(color[2])
        color = (r, g, b)
        #cv2.putText(temp_image,dict[str(category_id)],(bbox[0]+5,bbox[1]+40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1,cv2.LINE_AA) # class adi göstermek için
        cv2.putText(temp_image,str(category_id),(bbox[0]+5,bbox[1]+40),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,0),2,cv2.LINE_AA) #class number göstermek için
        cv2.rectangle(temp_image,(bbox[0],bbox[1]),(bbox[0]+bbox[2],bbox[1]+bbox[3]), color ,5) #colors[category_id]
    cv2.imwrite(curFolder+"/isaretlemeler/"+os.path.basename(imageContent[x])[0:-4]+".jpg",temp_image)

print("--- %s seconds ---" % (time.time() - start_time))