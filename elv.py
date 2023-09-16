import os
import pyautogui


def img(path):
    return os.path.join('images', path)


# find a neighborly help button (either normal or golden), and click it
def clickHelpButton(buttonTop):
    greenLocation = pyautogui.locateOnScreen(img("help.bmp"), region=(0, buttonTop, 1920, 1100))
    goldLocation = pyautogui.locateOnScreen(img("gold.bmp"), region=(0, buttonTop, 1920, 1100))

    if not greenLocation and not goldLocation:
        return (False, None)

    greenTop = greenLocation.top if greenLocation else 10000
    goldTop = goldLocation.top if goldLocation else 10000

    helpLocation = greenLocation if greenTop < goldTop else goldLocation

    buttonTop = helpLocation.top + 1
    buttonLeft = helpLocation.left

    print(f"Found at {buttonTop}")

    pyautogui.click(buttonLeft + 1, buttonTop + 1)
    pyautogui.sleep(0.2)

    return (True, buttonTop)


# find contribute targets in this order of priority: builder -> culture -> main hall
def clickContribButton():
    mainhallLocation = pyautogui.locateOnScreen(img("mainhall.bmp"))
    bldr1Location = pyautogui.locateOnScreen(img("bldr1.bmp"))
    bldr2Location = pyautogui.locateOnScreen(img("bldr2.bmp"))
    cultureLocation = pyautogui.locateOnScreen(img("culture.bmp"))

    contribLoc = bldr1Location or bldr2Location or cultureLocation or mainhallLocation

    pyautogui.click(contribLoc.left, contribLoc.top)
    pyautogui.sleep(0.7)

    # check if already helped, if so, just contribute to main hall instead (always possible)
    alreadyHelpedLocation = pyautogui.locateOnScreen(img("alreadyhelped.bmp"))
    if alreadyHelpedLocation:
        pyautogui.click(
            alreadyHelpedLocation.left + alreadyHelpedLocation.width / 2,
            alreadyHelpedLocation.top + alreadyHelpedLocation.height - 5,
        )
        pyautogui.sleep(0.5)
        pyautogui.click(mainhallLocation.left, mainhallLocation.top)
        pyautogui.sleep(0.7)


# check if some reward is available
def checkCollectReward():
    rewardLocation = pyautogui.locateOnScreen(img("reward.bmp"))
    if rewardLocation:
        pyautogui.click(
            rewardLocation.left + 10,
            rewardLocation.top + rewardLocation.height - 10,
        )
        pyautogui.sleep(0.5)


def nextPage():
    nextPageLocation = pyautogui.locateOnScreen(img("nextpage.bmp"))
    lastPageLocation = pyautogui.locateOnScreen(img("lastpage.bmp"))

    if lastPageLocation or not nextPageLocation:
        return False

    print("Next page")

    pyautogui.click(nextPageLocation.left + 1, nextPageLocation.top + 1)
    pyautogui.sleep(0.5)
    pyautogui.moveTo(nextPageLocation.left - 10, nextPageLocation.top + 1)

    return True


def main():
    keepPaging = True
    while keepPaging:
        buttonTop = 0
        keepLooking = True
        while keepLooking:
            (keepLooking, buttonTop) = clickHelpButton(buttonTop)
            if not keepLooking:
                break

            clickContribButton()

            checkCollectReward()

        keepPaging = nextPage()


main()
