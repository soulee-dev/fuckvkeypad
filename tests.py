import cv2
import unittest
from fuckvkeypad import get_keypad_num_list


class FuckvKeypadTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_keymap(self):
        img = cv2.imread("test_assets/vKeypad.png")
        keymap = get_keypad_num_list(
            img, asset_path="test_assets/", data_path="test_assets/data.json"
        )
        self.assertEqual(keymap, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])

    def test_not_match_img_size(self):
        img = cv2.imread("test_assets/vKeypad.png")
        keymap = get_keypad_num_list(
            img, asset_path="test_assets/", data_path="test_assets/test_fail.json"
        )
        self.assertEqual(keymap, [])


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
