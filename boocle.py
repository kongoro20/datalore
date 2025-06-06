import time
import subprocess

# Wait 1.5 seconds before starting
time.sleep(1.5)

# Run lore1.py 100 times
for i in range(100):
    subprocess.run(["python", "lore1.py"])
    time.sleep(1.5)
