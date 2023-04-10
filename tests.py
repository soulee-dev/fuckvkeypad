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
                {"1": [0, 0, 55, 55]},
                {"2": [58, 0, 113, 55]},
                {"3": [116, 0, 171, 55]},
                {"4": [0, 58, 55, 113]},
                {"5": [58, 58, 113, 113]},
                {"6": [116, 58, 171, 113]},
                {"7": [0, 116, 55, 171]},
                {"8": [58, 116, 113, 171]},
                {"9": [116, 116, 171, 171]},
                {"0": [58, 174, 113, 229]},
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
