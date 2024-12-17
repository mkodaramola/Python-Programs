import subprocess
from time import sleep
import winsound
import re


def get_name(device_info):
    match = re.search(r"Name:\s+(.+)", device_info)
    if match:
        return match.group(1).strip()
    return None


my_search = 'MyDevice'

while True:
    try:
        result = subprocess.check_output(['powershell', 'Get-BluetoothDevice'], stderr=subprocess.DEVNULL)
        result = result.decode('ascii').replace("\r", "")
        devices = result.split("\n")
        print(devices)
        devices = [device for device in devices if "Name" in device]
        for device in devices:
            name = get_name(device)
            if name and name.lower() == my_search.lower():
                winsound.Beep(2500, 1000)
                break

        sleep(2)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        break
