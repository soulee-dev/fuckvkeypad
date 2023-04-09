import json
import cv2
import numpy as np


def diff_img(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    abs_diff = cv2.absdiff(img1, img2)
    mean_diff = np.mean(abs_diff)
    max_pixel_value = 255
    percentage = 100 - ((mean_diff / max_pixel_value) * 100)
    return percentage


def get_keypad_num_list(img, threshold: float):
    # load json file
    with open("data.json", "r") as f:
        data = json.load(f)
    boxes = data["boxes"]
    assets = data["assets"]
    keypad_num_list = []
    for box in boxes:
        crop = img[box[1]:box[3], box[0]:box[2]]
        for key, asset in assets.items():
            try:
                diff = diff_img(crop, cv2.imread(asset))
                if diff > threshold:
                    keypad_num_list.append(key)
            except Exception as e:
                print(e)
    return keypad_num_list


if __name__ == '__main__':
    img = cv2.imread("v 1.png")
    print(get_keypad_num_list(img, 99))
