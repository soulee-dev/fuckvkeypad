import cv2
import unittest
from fuckvkeypad import get_keymap


class FuckvKeypadTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_keymap(self):
        img = cv2.imread("test_assets/vKeypad.png")
        keymap = get_keymap(
            img, asset_path="test_assets/", data_path="test_assets/data.json"
        )
        self.assertEqual(
            keymap,
            [
                {"box": [0, 0, 55, 55], "key_code": 1},
                {"box": [58, 0, 113, 55], "key_code": 2},
                {"box": [116, 0, 171, 55], "key_code": 3},
                {"box": [0, 58, 55, 113], "key_code": 4},
                {"box": [58, 58, 113, 113], "key_code": 5},
                {"box": [116, 58, 171, 113], "key_code": 6},
                {"box": [0, 116, 55, 171], "key_code": 7},
                {"box": [58, 116, 113, 171], "key_code": 8},
                {"box": [116, 116, 171, 171], "key_code": 9},
                {"box": [58, 174, 113, 229], "key_code": 0},
            ],
        )

    def test_not_match_img_size(self):
        img = cv2.imread("test_assets/vKeypad.png")
        keymap = get_keymap(
            img, asset_path="test_assets/", data_path="test_assets/test_fail.json"
        )
        self.assertEqual(keymap, [])


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
