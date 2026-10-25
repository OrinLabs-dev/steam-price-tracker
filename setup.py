#setup.py
import os
import sys
import winreg
import logging
LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'debug.log')

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s'
)
ERROR_LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'error_log.txt')

folder = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(folder, 'price_tracker.py')
pythonw = sys.executable.replace('python.exe', 'pythonw.exe')

run_command = f'"{pythonw}" "{script_path}"'


key = winreg.OpenKey(
    winreg.HKEY_CURRENT_USER, 
    r"Software\Microsoft\Windows\CurrentVersion\Run", 
    0, 
    winreg.KEY_SET_VALUE
)

winreg.SetValueEx(key, "SteamPriceTracker", 0, winreg.REG_SZ, run_command)
winreg.CloseKey(key)

print("Steam Price Tracker has been set up successfully! It will now run automatically on startup.")
