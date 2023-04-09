import json
from functools import reduce
import math
import operator
from PIL import Image, ImageChops


def rms_diff(img1: Image, img2: Image):
    h = ImageChops.difference(img1, img2).histogram()
    return math.sqrt(reduce(operator.add,
                            map(lambda h, i: h * (i ** 2), h, range(256))
                            ) / (float(img1.size[0]) * img1.size[1]))


def get_keypad_num_list(img: Image, threshold: float):
    # load json file
    with open("data.json", "r") as f:
        data = json.load(f)
    boxes = data["boxes"]
    assets = data["assets"]
    keypad_num_list = []

    for k, box in boxes.items():
        crop = img.crop(box=box)
        for key, asset in assets.items():
            try:
                diff = rms_diff(crop, Image.open(asset))
                if diff < threshold:
                    keypad_num_list.append(key)
            except Exception as e:
                print(e)
    return keypad_num_list


if __name__ == '__main__':
    img = Image.open("test.png")
    print(get_keypad_num_list(img, 13))
