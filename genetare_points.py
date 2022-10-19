import cv2
import numpy as np

image_name = "1920x1080.jpg"
text_file_name = "1920x1080.txt"

def read_image():

    image_path = str(image_name)
    image = cv2.imread(image_path)

    return image

def load_text_file_content():

    text_path = str(text_file_name)
    text_content = np.loadtxt(text_path).astype(int)

    return text_content

def save_point_to_txt(x,y):
    
    calibFile = open("1920x1080_new.txt",'a')
    calibFile.write(str(x)+" "+str(y)+"\n")
    calibFile.close()

def put_points_on_image():
    global image
    
    image = read_image()
    points = load_text_file_content()

    for point in points:
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.circle(image, (point[0], point[1]), 20, (255, 0, 0), -1)
        cv2.putText(image, str(point[0]) + ',' + str(point[1]), (point[0]+5,point[1]+5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    cv2.namedWindow("Calibration Image", cv2.WND_PROP_FULLSCREEN)
    cv2.imshow("Calibration Image",image)
    cv2.setMouseCallback("Calibration Image", click_event)
    

def click_event(event, x, y, flags, params):
    
    if event ==  cv2.EVENT_LBUTTONDOWN: # sol click yapıldı mı?
        print(x, " ", y) # koordinatları gösterme

        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(image, str(x) + ',' + str(y), (x,y), font, 1, (0, 0, 255), 2) # imge üzerine yazı ekleme
        cv2.imshow("Calibration Image", image)

        key = cv2.waitKey(0)
        if key == ord("s"):
            save_point_to_txt(x, y)

if __name__ == "__main__":
    
    put_points_on_image()

    if cv2.waitKey(0) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
