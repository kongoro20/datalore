import pyautogui
import random
import time
import subprocess
import string
import sys

time.sleep(3)

def random_click_in_area(top_left, bottom_right):
    """Perform a random click within a rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)

# New Step: Detect the tab button using 'tab_button.png'
try:
    tab_button_location = pyautogui.locateCenterOnScreen('tab_button.png', confidence=0.8)
    if tab_button_location is not None:
        print("Tab button detected, clicking at (1342, 125)...")
        pyautogui.click(1339, 175)
        time.sleep(2)
    else:
        print("Tab button not detected, proceeding to Step 1...")
except Exception as e:
    print(f"Error detecting tab button: {e}")
    print("Proceeding to Step 1...")

time.sleep(2)

pyautogui.click(468, 81)
time.sleep(0.5)
pyautogui.write('https://datalore.jetbrains.com/notebooks')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(8)
subprocess.run(['python3', 'nootebook.py'])
time.sleep(1)
subprocess.run(['python3', 'ready.py'])
time.sleep(10)
random_click_in_area((194, 178), (213, 182))
time.sleep(random.uniform(0.5, 1))
random_click_in_area((193, 487), (343, 493))
time.sleep(random.uniform(0.5, 1))
time.sleep(6)
subprocess.run(['python3', 'write.py'])
time.sleep(5)
subprocess.run(['python3', 'terminate.py'])
time.sleep(4)

pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyautogui.hotkey('ctrl', 'shift', 'tab')
time.sleep(1)
pyautogui.hotkey('ctrl', 'w')
time.sleep(70) 

