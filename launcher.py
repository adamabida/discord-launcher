
import os
import subprocess
import psutil
import time
from datetime import datetime
import ctypes

DISCORD_PATH = r"C:\Users\adama\AppData\Local\Discord\Update.exe"

def show_warning(message):
    ctypes.windll.user32.MessageBoxW(0, message, "Warning", 1)

def is_discord_running():
    for proc in psutil.process_iter(attrs=['name']):
        if "Discord" in proc.info['name']:
            return True
    return False


def get_allowed_start():
    day = datetime.now().weekday()
    if day <= 4 :   # Monday–Friday
        return 21  
    else:         
        return 0 
       

def launch_discord():
    subprocess.Popen([DISCORD_PATH, "--processStart", "Discord.exe"])

def main():
    now = datetime.now()
    AllOWED_END = 24
    ALLOWED_START = get_allowed_start()
    if ALLOWED_START <= now.hour < AllOWED_END :
        print('Opening')
        launch_discord()        
    else:
        show_warning("Maybe later. Discord is only available between "
                     f"{ALLOWED_START}:00 and {AllOWED_END}:00")

if __name__ == "__main__":
    main()
