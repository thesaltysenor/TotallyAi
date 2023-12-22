import platform
import subprocess
import os

def get_system_info():
    print("System Information:")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")


def get_installed_apps():
    print("Installed Applications:")
    cmd = 'powershell "Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion"'
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    apps = result.stdout.decode()
    print(apps)


def is_app_running(app_name):
    cmd = f'powershell "Get-Process | Where-Object {{$_.MainWindowTitle -like \'*{app_name}*\'}}"'
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return "Running" if result.stdout else "Not Running"

def open_app(app_name):
    try:
        os.startfile(app_name)
    except Exception as e:
        print(f"Error opening {app_name}: {e}")


def main():
    get_system_info()
    get_installed_apps()

    while True:
        app_to_open = input("Enter the name of an app to open (or 'exit' to quit): ")
        if app_to_open.lower() == 'exit':
            break
        open_app(app_to_open)

if __name__ == "__main__":
    main()
 