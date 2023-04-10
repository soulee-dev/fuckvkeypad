# 🖕⌨️ fuckvkeypad
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Lint](https://github.com/soulee-dev/FuckVkeyPad/actions/workflows/black.yml/badge.svg)](https://github.com/soulee-dev/FuckVkeyPad/actions/workflows/black.yml)
[![codecov](https://codecov.io/gh/soulee-dev/FuckVkeyPad/branch/main/graph/badge.svg?token=V3MK4N5X5X)](https://codecov.io/gh/soulee-dev/FuckVkeyPad)

금융, 정부 웹사이트등에 널리 쓰이는 보안 프로그램인 가상키보드(vKeyboard)를 우회합니다

미리 캡쳐된 이미지와 유사도를 분석하는 방식으로 우회가 이루어집니다

# 사용 방법
## vKeypad-Studio
[사용 방법 영상 - YouTube](https://www.youtube.com/watch?v=4kE4m3oMGX8)
1. 가상키보드 이미지를 준비합니다
2. Figma에서 가상 키보드 이미지를 업로드 합니다
3. Figma에서 사각형으로 가상 키보드 각각의 키를 덮어줍니다
4. Figma에서 svg 파일로 Export 합니다
5. 터미널에서 ``vkeypad-studio [이미지 파일] [svg 파일]`` 을 입력합니다
6. 새로 뜬 창에서, 이미지에 해당되는 키보드 키를 눌러줍니다
7. assets 폴더 속 사진들과, data.json을 따로 보관 해둡니다

## fuckvkeypad
```python
import cv2
from fuckvkeypad import get_keymap

img = cv2.imread("test_assets/vKeypad.png")
keymap = get_keymap(
    img, asset_path="test_assets/", data_path="test_assets/data.json"
)

print(keymap)
```
```shell
> ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] 
```

# Special Thanks
이 라이브러리는 [simple_bank_korea](https://github.com/Beomi/simple_bank_korea)에서 영감을 받아 제작하였습니다