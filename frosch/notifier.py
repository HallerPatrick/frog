import platform
import os

def notify_os(title: str = "Ups", message: str = "Your python program crashed."):
    """Check current OS and run a notification subprocess"""
    current_platform = platform.system()

    if current_platform == "Darwin":
        command = mac_notify(title, message)
    elif current_platform == "Linux":
        command = linux_notify(title, message)
    elif current_platform == "Windows":
        command = windows_notify(title, message)
    else:
        return

    os.system(command)

def mac_notify(title: str, message: str) -> str:
    """Display notification for MacOS systems"""
    command = f'''osascript -e 'display notification "{message}" with title "{title}"' '''
    return command
    
def linux_notify(title: str, message: str) -> str:
    """Display notification for Linux systems"""
    # TODO: Test this
    command = f'''notify-send "{title}" "{message}"'''
    return command

def windows_notify(title: str, message: str) -> str:
    """Display notification for Windows systems"""
    # TODO: Test this
    # http://woshub.com/popup-notification-powershell/
    command = f'''$wshell = New-Object -ComObject Wscript.Shell
$Output = $wshell.Popup("{message}", 0, "{title}", 0)'''
    return command
