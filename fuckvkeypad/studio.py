import os
import cv2
import json
import argparse
from svgpathtools import svg2paths


def interpret_svg(svg_path: str):
    coordinates = []
    paths, _ = svg2paths(svg_path)
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
    coordinates = coordinates[2:]
    return coordinates


def open_studio(img_path: str, svg_path: str):
    boxes = []
    assets = {}
    img = cv2.imread(img_path)
    coordinates = interpret_svg(svg_path)
    print("Press the key that corresponds on the keypad on image")
    if not os.path.exists("assets"):
        os.makedirs("assets")
    for i, coordinate in enumerate(coordinates):
        crop = img[coordinate[1] : coordinate[3], coordinate[0] : coordinate[2]]
        cv2.imshow("crop", crop)
        key = chr(cv2.waitKey(0))
        print(f"Key: {key}")
        boxes.append(coordinate)
        assets[key] = f"{i}.png"
        cv2.imwrite(f"assets/{i}.png", crop)
    cv2.destroyAllWindows()
    boxes.sort(key=lambda box: (box[1], box[0]))
    json_data = {"boxes": boxes, "assets": assets}
    with open("data.json", "w") as f:
        json.dump(json_data, f, indent=4)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("img_path", help="Path to the image")
    parser.add_argument("svg_path", help="Path to the svg")
    args = parser.parse_args()
    open_studio(args.img_path, args.svg_path)


if __name__ == "__main__":
    main()
