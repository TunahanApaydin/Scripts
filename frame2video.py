import cv2
import glob
import os
import re
from tqdm import tqdm

save_path = "/home/tuna/Documents/Otopark/train_test_videos/"
video_name = "test_video"
fps = 4
result = cv2.VideoWriter(save_path + video_name + ".mp4",  
                        cv2.VideoWriter_fourcc(*'DIVX'), 
                        fps, (640,480))

def save_as_video(frame):
    result.write(frame)

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def get_sorted_files(file_dir):
    list_subfolders_with_paths = [f.path for f in os.scandir(file_dir) if f.is_dir()]
    sorted_subfolders = sorted(list_subfolders_with_paths, key = numericalSort)
    return sorted_subfolders

def get_len(sorted_subfolders):
    return len(sorted_subfolders)

if __name__ == "__main__":
    frame_paths = "/home/tuna/Documents/Otopark/train_test_videos/test_frames/"
    sorted_subfolders = get_sorted_files(frame_paths)
    print("Frame to video operation is started!!")
    for sub_folder in tqdm(sorted_subfolders):
        frames = glob.glob(sub_folder + "/*.jpg")
        sorted_frames = sorted(frames, key = numericalSort)
        for frame in tqdm(sorted_frames):
            frame = cv2.imread(frame)
            save_as_video(frame)
    result.release()
    print("Frame to video operation is finished!!")