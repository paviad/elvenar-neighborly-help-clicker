import pyautogui


def main():
    keepPaging = True
    while keepPaging:
        buttonTop = 0
        keepLooking = True
        while keepLooking:
            # find a neighborly help button (either normal or golden), and click it
            greenLocation = pyautogui.locateOnScreen("help.bmp", region=(0, buttonTop, 1920, 1100))
            goldLocation = pyautogui.locateOnScreen("gold.bmp", region=(0, buttonTop, 1920, 1100))

            if not greenLocation and not goldLocation:
                keepLooking = False
                break

            greenTop = greenLocation.top if greenLocation else 10000
            goldTop = goldLocation.top if goldLocation else 10000

            helpLocation = greenLocation if greenTop < goldTop else goldLocation

            buttonTop = helpLocation.top + 1
            buttonLeft = helpLocation.left

            print(f"Found at {buttonTop}")

            pyautogui.click(buttonLeft + 1, buttonTop + 1)
            pyautogui.sleep(0.5)

            mainhallLocation = pyautogui.locateOnScreen("mainhall.bmp")
            bldr1Location = pyautogui.locateOnScreen("bldr1.bmp")
            bldr2Location = pyautogui.locateOnScreen("bldr2.bmp")
            cultureLocation = pyautogui.locateOnScreen("culture.bmp")

            contribLoc = bldr1Location or bldr2Location or cultureLocation or mainhallLocation

            pyautogui.click(contribLoc.left, contribLoc.top)

            pyautogui.sleep(0.7)

            # check if some reward is available
            rewardLocation = pyautogui.locateOnScreen("reward.bmp")
            if rewardLocation:
                pyautogui.click(
                    rewardLocation.left + 10,
                    rewardLocation.top + rewardLocation.height - 10,
                )
                pyautogui.sleep(0.5)

            # check if already helper
            alreadyHelpedLocation = pyautogui.locateOnScreen("alreadyhelped.bmp")
            if alreadyHelpedLocation:
                pyautogui.click(
                    alreadyHelpedLocation.left + alreadyHelpedLocation.width / 2,
                    alreadyHelpedLocation.top + alreadyHelpedLocation.height - 5,
                )
                pyautogui.sleep(0.5)
                pyautogui.click(mainhallLocation.left, mainhallLocation.top)
                pyautogui.sleep(0.7)

        nextPageLocation = pyautogui.locateOnScreen("nextpage.bmp")
        lastPageLocation = pyautogui.locateOnScreen("lastpage.bmp")

        if lastPageLocation or not nextPageLocation:
            keepPaging = False
            break

        print("Next page")

        pyautogui.click(nextPageLocation.left + 1, nextPageLocation.top + 1)
        pyautogui.sleep(0.5)
        pyautogui.moveTo(nextPageLocation.left - 10, nextPageLocation.top + 1)


main()
