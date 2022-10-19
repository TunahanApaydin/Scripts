import os
import cv2
import glob

class FrameExtraction:
    def __init__(self):
        self.video_path = "/home/tuna/Documents/Otopark/sayim_basarimi_analizi/yeni_model/2/"
        self.save_dir = "/home/tuna/Documents/Otopark/sayim_basarimi_analizi/yeni_model/frames/"
        self.frame_skip = 1

    def frame_capture(self, video_path, video_name_id, video_name):
        print("Frame Capturing Started for video {}".format(video_name))
        capture = cv2.VideoCapture(video_path)

        try:
            os.mkdir(self.save_dir + str(video_name))
        except OSError as error:
            print(error)

        i = 0
        frame_count = 0
        while capture.isOpened():
            ret, frame = capture.read()

            if not ret:
                break

            if i > self.frame_skip - 1:
                frame_count +=1
                cv2.imwrite(self.save_dir + str(video_name) + "/" + str(frame_count*self.frame_skip)+'.jpg', frame)
                print("Frame: {} Saved".format(str(frame_count*self.frame_skip)))
                i = 0
                continue
            i += 1

        print("Frame Capturing Finished")
        capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    fe = FrameExtraction()
    paths = glob.glob(fe.video_path + "*.mp4")

    video_name_id = 0
    for i in range(len(paths)):
        video_name = paths[i].split("/")[-1].split(".")[0]
        fe.frame_capture(paths[i], video_name_id, video_name)
        video_name_id +=1