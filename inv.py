from PIL import Image, ImageChops

import os
import pyautogui
import pytesseract


def img(path):
    return os.path.join("images", path)


def find(diff):
    for x in reversed(range(0, 1920)):
        for y in range(0, 1080):
            if diff.getpixel((x, y)) != (0, 0, 0):
                return (x, y)


def nextPage():
    nextPageLocation = pyautogui.locateOnScreen(img("nextpage.bmp"), minSearchTime=0.1, confidence=0.9)
    lastPageLocation = pyautogui.locateOnScreen(img("lastpage.bmp"), minSearchTime=0.1, confidence=0.9)

    if lastPageLocation or not nextPageLocation:
        return False

    print("Next page")

    pyautogui.click(nextPageLocation.left + 1, nextPageLocation.top + 1)
    # pyautogui.sleep(0.1)
    pyautogui.moveTo(nextPageLocation.left - 10, nextPageLocation.top + 1)

    return True


def main():
    pytesseract.pytesseract.tesseract_cmd = r"c:\program files\tesseract-ocr\tesseract.exe"  # need to install tesseract

    pyautogui.moveTo(200, 200)
    # pyautogui.sleep(0.1)

    summonings = pyautogui.locateOnScreen(img("summonings.bmp"), region=(0, 0, 1920, 1080), confidence=0.7)

    print(summonings)

    firstButtonLeft = summonings.left - 131
    firstButtonTop = summonings.top + 125
    buttonSize = 152

    file1 = open("myfile.csv", "w")

    page = 1

    keepPaging = True
    while keepPaging:

        ss1 = pyautogui.screenshot(region=(0, 0, 1920, 1080))
        print("took")

        for y in range(0, 2):
            for x in range(0, 4):
                buttonLeft = firstButtonLeft + x * buttonSize
                buttonTop = firstButtonTop + y * buttonSize
                # print(f'button at {x},{y}: {buttonLeft}, {buttonTop}')
                pyautogui.moveTo(firstButtonLeft, firstButtonTop - buttonSize / 2)
                # pyautogui.sleep(0.1)
                pyautogui.moveTo(buttonLeft, buttonTop)
                # pyautogui.sleep(0.1)
                pyautogui.moveTo(buttonLeft + 1, buttonTop)
                # pyautogui.sleep(0.1)
                ss2 = pyautogui.screenshot(region=(0, 0, 1920, 1080))
                diff = ImageChops.difference(ss1, ss2)
                (tx, ty) = find(diff)
                imga = ss2.crop(box=(tx - 505, ty, tx - 40, ty + 25))
                txt = pytesseract.image_to_string(imga)
                print(txt)
                # pyautogui.sleep(0.1)
                file1.write(f'{page},"{txt}"' + "\n")

        keepPaging = nextPage()
        page = page + 1

    file1.close()


main()
