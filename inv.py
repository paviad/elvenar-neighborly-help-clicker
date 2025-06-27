from PIL import Image, ImageChops

import os
import pyautogui
from pyscreeze import Box
import pytesseract


def img(path):
    return os.path.join("images", path)


def find(diff, region, buttonLeft, buttonTop):
    x = (buttonLeft - region.left) + 152
    y = buttonTop - region.top
    while y >= 0:
        if diff.getpixel((x, y)) == (0, 0, 0):
            break
        y -= 1

    y += 7

    x -= 1
    while x >= 0:
        if diff.getpixel((x, y)) == (0, 0, 0):
            break
        x -= 1

    x += 1
    y -= 6

    blx = x + 10
    bly = y + 10

    while blx < diff.width:
        if diff.getpixel((blx, y + 10)) == (0, 0, 0):
            break
        blx += 1

    while bly < diff.height:
        if diff.getpixel((x + 10, bly)) == (0, 0, 0):
            break
        bly += 1

    return (x, y, blx, bly)


def nextPage():
    nextPageLocation = pyautogui.locateOnScreen(img("nextpage.bmp"), minSearchTime=0.1, confidence=0.9)
    lastPageLocation = pyautogui.locateOnScreen(img("lastpage.bmp"), minSearchTime=0.1, confidence=0.9)

    if lastPageLocation or not nextPageLocation:
        return False

    print("Next page")

    pyautogui.click(nextPageLocation.left + 4, nextPageLocation.top + 4)
    pyautogui.sleep(0.1)
    pyautogui.moveTo(nextPageLocation.left - 10, nextPageLocation.top + 1)

    return True


def main():
    pyautogui.useImageNotFoundException(False)

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

    regionOfInterest = Box(0, 0, 1920, 1080)  # region of the screen to take screenshots

    while keepPaging:

        pyautogui.sleep(1.0)
        ss1 = pyautogui.screenshot(region=regionOfInterest)
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
                pyautogui.sleep(1.0)
                ss2 = pyautogui.screenshot(region=regionOfInterest)
                # ss2.save(f"page{page}_button{x}_{y}_after.png")
                diff = ImageChops.difference(ss1, ss2)
                # diff.save(f"page{page}_button{x}_{y}_diff.png")
                (dLeft, dTop, dRight, dBottom) = find(diff, regionOfInterest, buttonLeft, buttonTop)
                imga = ss2.crop(box=(dLeft + 9, dTop + 8, dLeft + 449, dTop + 24))
                # imga.save(f"page{page}_button{x}_{y}.png")
                txt = pytesseract.image_to_string(imga)
                txt = txt.strip()
                print(txt)
                # pyautogui.sleep(0.1)
                file1.write(f'{page},"{txt}"' + "\n")
                file1.flush()

        keepPaging = nextPage()
        page = page + 1

    file1.close()


main()
