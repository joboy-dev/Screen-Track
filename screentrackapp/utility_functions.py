import subprocess
import time
from datetime import datetime


# def get_window_icon(hwnd):
#     icon = win32gui.SendMessage(hwnd, win32con.WM_GETICON, win32con.ICON_SMALL)
    
#     if not icon:
#         icon = win32gui.SendMessage(hwnd, win32con.WM_GETICON, win32con.ICON_BIG)
#     if not icon:
#         icon = win32gui.GetClassLong(hwnd, win32con.GCL_HICONSM)
#     if not icon:
#         icon = win32gui.GetClassLong(hwnd, win32con.GCL_HICON)

#     return icon

# ----------------------------------------------------------------------

def get_year():
    '''Function to get current year'''
    return datetime.now().year


def get_open_apps():
    '''Function to get all open applications on the user system'''
    
    open_apps = []
        
    # Get all open applications by name
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        if line.rstrip():
            open_apps.append(line.decode().rstrip())
    
    return open_apps


def get_active_window_title():
    cmd = 'powershell "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait(\"%{TAB}\"); Start-Sleep -Milliseconds 500; [System.Windows.Forms.SendKeys]::SendWait(\"%{TAB}\"); Start-Sleep -Milliseconds 500; [System.Windows.Forms.SendKeys]::SendWait(\"%{F6}\"); Start-Sleep -Milliseconds 500; Add-Type -AssemblyName PresentationCore; (New-Object -TypeName System.Windows.Input.KeyConverter).ConvertTo([System.Windows.Input.Key]::Tab, [System.Windows.Input.Key]).ToString()"'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return proc.communicate()[0].decode().strip()


def calculate_active_time(window_start_time):
    return time.time() - window_start_time


def main():
    active_window_title = get_active_window_title()
    window_start_time = time.time()

    while True:
        time.sleep(1)  # Adjust the interval based on your requirements

        current_window_title = get_active_window_title()

        if current_window_title != active_window_title:
            active_time = calculate_active_time(window_start_time)
            print(f"Active Window: {active_window_title}, Active Time: {active_time} seconds")

            # Update the active window and reset the start time
            active_window_title = current_window_title
            window_start_time = time.time()