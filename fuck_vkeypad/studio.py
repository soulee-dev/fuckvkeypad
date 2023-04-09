import cv2
from svgpathtools import parse_path, svg2paths
import json

def interpret_svg():
    coordinates = []
    paths, _ = svg2paths('test.svg')

    for path in paths:
        x_values = []
        y_values = []
        for segment in path:
            for point in segment:
                x_values.append(point.real)
                y_values.append(point.imag)
        x1, y1 = int(x_values[0]), int(y_values[0])
        x2, y2 = int(x_values[3]), int(y_values[3])
        coordinates.append((x1, y1, x2, y2))

    coordinates.pop()
    coordinates.pop()
    return coordinates


def open_studio(img_path: str):
    boxes = {}
    assets = {}
    img = cv2.imread(img_path)
    coordinates = interpret_svg()
    print("Press the key that corresponds on the keypad on image")
    for i, coordinate in enumerate(coordinates):
        crop = img[coordinate[1]:coordinate[3], coordinate[0]:coordinate[2]]
        cv2.imshow("crop", crop)
        key = chr(cv2.waitKey(0) % 256)
        print(f"key: {key}")
        boxes[key] = coordinate
        assets[key] = f"assets/{i}.png"
        cv2.imwrite(f"assets/{i}.png", crop)

    json_data = {
        "boxes": boxes,
        "assets": assets
    }
    # save json data
    with open("data.json", "w") as f:
        json.dump(json_data, f)


if __name__ == "__main__":
    img_path = input("Enter the path to the image: ")
    open_studio(img_path)
