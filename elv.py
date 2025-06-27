import os
import pyautogui
from pyscreeze import Box


def img(path):
    return os.path.join("images", path)


# find a neighborly help button (either normal or golden), and click it
def clickHelpButton(buttonTop):
    print("1")
    greenLocation = pyautogui.locateOnScreen(
        img("help.bmp"), region=(0, buttonTop, 1920, 1100), minSearchTime=0.1, confidence=0.9
    )
    print("2")
    goldLocation = pyautogui.locateOnScreen(
        img("gold.bmp"), region=(0, buttonTop, 1920, 1100), minSearchTime=0.1, confidence=0.9
    )
    print("3")

    if not greenLocation and not goldLocation:
        return (False, None)
    print("4")

    greenTop = greenLocation.top if greenLocation else 10000
    print("5")
    goldTop = goldLocation.top if goldLocation else 10000
    print("6")

    helpLocation = greenLocation if greenTop < goldTop else goldLocation
    print("7")

    buttonTop = helpLocation.top + 1
    print("8")
    buttonLeft = helpLocation.left
    print("9")

    print(f"Found at {buttonTop}")

    pyautogui.click(buttonLeft + 1, buttonTop + 1)
    pyautogui.sleep(0.1)
    print("10")

    return (True, buttonTop)


# find contribute targets in this order of priority: builder -> culture -> main hall
def clickContribButton():
    pyautogui.screenshot("test.png")

    mainhallLocation = pyautogui.locateOnScreen(img("mainhall.bmp"), minSearchTime=0.1, confidence=0.9)
    cultureLocation = None
    bldrLocation = None

    if mainhallLocation.left == 954:
        print("mainhall only")
    elif mainhallLocation.left == 855:
        cultureLocation = Box(
            mainhallLocation.left + 197, mainhallLocation.top, mainhallLocation.width, mainhallLocation.height
        )
    else:
        bldrLocation = Box(
            mainhallLocation.left + 197, mainhallLocation.top, mainhallLocation.width, mainhallLocation.height
        )
        cultureLocation = Box(
            bldrLocation.left + 197, bldrLocation.top, bldrLocation.width, bldrLocation.height
        )

    # bldr1Location = pyautogui.locateOnScreen(img("bldr1.bmp"), minSearchTime=0.1, confidence=0.9)
    # bldr2Location = pyautogui.locateOnScreen(img("bldr2.bmp"), minSearchTime=0.1, confidence=0.9)
    # cultureLocation = pyautogui.locateOnScreen(img("culture.bmp"), minSearchTime=0.1, confidence=0.9)

    # contribLoc = bldr1Location or bldr2Location or cultureLocation or mainhallLocation
    contribLoc = bldrLocation or cultureLocation or mainhallLocation

    pyautogui.click(contribLoc.left, contribLoc.top)
    pyautogui.sleep(0.1)

    # check if already helped, if so, just contribute to main hall instead (always possible)
    alreadyHelpedLocation = pyautogui.locateOnScreen(img("alreadyhelped.bmp"), minSearchTime=0.1, confidence=0.9)
    if alreadyHelpedLocation:
        pyautogui.click(
            alreadyHelpedLocation.left + alreadyHelpedLocation.width / 2,
            alreadyHelpedLocation.top + alreadyHelpedLocation.height - 5,
        )
        pyautogui.sleep(0.1)
        pyautogui.click(mainhallLocation.left, mainhallLocation.top)
        pyautogui.sleep(0.1)


# check if some reward is available
def checkCollectReward():
    rewardLocation = pyautogui.locateOnScreen(img("reward.bmp"), minSearchTime=0.1, confidence=0.9)
    if rewardLocation:
        pyautogui.click(
            rewardLocation.left + 10,
            rewardLocation.top + rewardLocation.height - 10,
        )
        pyautogui.sleep(0.1)


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
    keepPaging = True

    while keepPaging:
        buttonTop = 0
        keepLooking = True
        while keepLooking:
            print("a")
            (keepLooking, buttonTop) = clickHelpButton(buttonTop)
            print("b")
            if not keepLooking:
                break

            print("c")
            clickContribButton()

            print("d")
            checkCollectReward()
            print("e")

        print("I")
        keepPaging = nextPage()
        print("II")


main()
