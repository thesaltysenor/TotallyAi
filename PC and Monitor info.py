import platform
import subprocess

from screeninfo import get_monitors

for monitor in get_monitors():
    print(f"Monitor {monitor.name}: {monitor.width}x{monitor.height}")


print(f"System: {platform.system()}")
print(f"Node Name: {platform.node()}")
print(f"Release: {platform.release()}")
print(f"Version: {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")

def get_installed_programs():
    cmd = 'powershell "Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName"'
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return result.stdout.decode()

print(get_installed_programs())