import cv2
from svgpathtools import svg2paths
import json


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


def open_studio(img_path: str):
    boxes = []
    assets = {}
    img = cv2.imread(img_path)
    svg_path = input("Enter the path to the svg file: ")
    coordinates = interpret_svg(svg_path)
    print("Press the key that corresponds on the keypad on image")
    for i, coordinate in enumerate(coordinates):
        crop = img[coordinate[1] : coordinate[3], coordinate[0] : coordinate[2]]
        cv2.imshow("crop", crop)
        key = chr(cv2.waitKey(0))
        print(f"Key: {key}")
        boxes.append(coordinate)
        assets[key] = f"assets/{i}.png"
        cv2.imwrite(f"assets/{i}.png", crop)
    cv2.destroyAllWindows()
    boxes.sort(key=lambda box: (box[1], box[0]))
    json_data = {"boxes": boxes, "assets": assets}
    with open("data.json", "w") as f:
        json.dump(json_data, f)


if __name__ == "__main__":
    img_path = input("Enter the path to the image: ")
    open_studio(img_path)
    print("Done!")
