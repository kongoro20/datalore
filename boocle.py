import time
import subprocess

time.sleep(1.5)
subprocess.run(["bash", "open.sh"])
time.sleep(1.5)
for i in range(100):
    subprocess.run(["python", "lore1.py"])
    time.sleep(1.5)
