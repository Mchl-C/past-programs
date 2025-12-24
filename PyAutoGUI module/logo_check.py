import pyautogui as p
import time

time.sleep(1)


logo_position = p.locateOnScreen('logo.png')
x, y = p.position()

if logo_position:
    print(f"Logo found at position: {logo_position}")
    p.moveTo(logo_position.left, logo_position.top)
    p.click(button="left")
    p.moveTo(900,700)
    p.click(button="left")
else:
    print("Logo not found")

'''
p.moveTo(850,700)
p.click()
p.scroll(-10, 900, 700)
''' 
