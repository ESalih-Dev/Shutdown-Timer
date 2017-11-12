import os
import time

sleep = 0
while True:
    try:
        sleep = float(input("How many mins to shutdown?\n"))
        break
    except Exception:
        print("Please input a number.\n")

sleep = sleep*60
time.sleep(sleep)
os.popen("C:\Windows\System32\shutdown.exe -s -t 00")
        

