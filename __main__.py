import pyautogui
pyautogui.FAILSAFE = True

with open("scripts.txt", "r+") as f:
	script = f.read().split(" ")
	pyautogui.moveTo(x=400,y=400)    # move mouse to the window
	pyautogui.dragTo(400,400, button='left')    # focus the window
	pyautogui.click(x=400,y=400)     # simulate left click
	for word in script:
		pyautogui.typewrite(word)
		pyautogui.typewrite(['enter'])
	f.close()

