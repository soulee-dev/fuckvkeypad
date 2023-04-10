import os
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


def get_keymap(
    img,
    asset_path: str,
    data_path: str,
    threshold: float = 100,
    verbose: bool = False,
):
    with open(data_path, "r") as f:
        data = json.load(f)
    boxes = data["boxes"]
    assets = data["assets"]
    keymap = []
    for box in boxes:
        crop = img[box[1] : box[3], box[0] : box[2]]
        for key, asset in assets.items():
            img_asset = cv2.imread(os.path.join(asset_path, asset))
            h1, w1 = crop.shape[:2]
            h2, w2 = img_asset.shape[:2]
            if (h1 != h2) or (w1 != w2):
                continue
            try:
                diff = diff_img(crop, img_asset)
                if verbose:
                    print(f"{key}: {diff:.2f}")
                if diff >= threshold:
                    keymap.append({"key_code": key, "box": box})
            except Exception as e:
                print(e)
    return keymap


def main():
    image_path = input("Enter image path: ")
    img = cv2.imread(image_path)
    keymap = get_keymap(
        img,
        threshold=100,
        asset_path="../test_assets",
        data_path="../test_assets/data.json",
    )
    for key in keymap:
        print(key["key_code"], key["box"])


if __name__ == "__main__":
    main()  # pragma: no cover
