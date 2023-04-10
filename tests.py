import cv2
import unittest
from fuckvkeypad import get_keypad_num_list


class FuckvKeypadTest(unittest.TestCase):
    def test_fuckvkeypad(self):
        img = cv2.imread("assets/vKeypad.png")
        keymap = get_keypad_num_list(img, asset_path="assets/", data_path="assets/data.json")
        self.assertEqual(keymap, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])


if __name__ == "__main__":
    unittest.main()
