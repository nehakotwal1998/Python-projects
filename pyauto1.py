import pyautogui
import time 

time.sleep(5)
distance=400

while distance>0:
	pyautogui.dragrel(distance,0,duartion=0.5)#right
	distance=distance-50

	pyautogui.dragrel(0,distance,duartion=0.5)#down
	pyautogui.dragrel(-distance,0,duartion=0.5)#left

	distance=distance-50

	pyautogui.dragrel(0,-distance,duartion=0.5)#up