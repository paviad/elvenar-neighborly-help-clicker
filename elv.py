import pyautogui


def main():
    keepPaging = True
    while keepPaging:
        buttonTop = 0
        keepLooking = True
        while keepLooking:

            # find a neighborly help button (either normal or golden), and click it
            helpLocation = pyautogui.locateOnScreen("help.bmp", region=(0, buttonTop, 1920, 1100))
            goldLocation = pyautogui.locateOnScreen("gold.bmp", region=(0, buttonTop, 1920, 1100))

            if helpLocation and goldLocation:
                buttonTop = min(helpLocation.top, goldLocation.top) + 1
                buttonLeft = helpLocation.left
            elif helpLocation:
                buttonTop = helpLocation.top + 1
                buttonLeft = helpLocation.left
            elif goldLocation:
                buttonTop = goldLocation.top + 1
                buttonLeft = goldLocation.left
            else:
                keepLooking = False
                break

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
