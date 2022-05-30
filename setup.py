import os
import pathlib
import subprocess
import sys

import pkg_resources
from pkg_resources import evaluate_marker


def check_os() -> str:
    """
    Check if OS is Linux, Windows or Mac
    """
    if sys.platform == "win32" or sys.platform == "cygwin":
        return "Windows"
    elif sys.platform == "linux":
        return "Linux"
    elif sys.platform == "darwin":
        return "Mac"
    else:
        return "Unknown"

def check_install_dependencies() -> None:
    """
    Check if all dependencies are installed
    """
    required = {"python-crontab"}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed 
    if missing and check_os() == "Linux":
        python = sys.executable
        subprocess.check_call([python, "-m", "pip", "install", *missing], stdout=subprocess.DEVNULL)

def import_crontab():
    """
    Import crontab module
    """
    try:
        import crontab
    except ImportError:
        print("Crontab module not found. Installing...")
        check_install_dependencies()
        import crontab

def add_crontab():
    """
    Add blocker crontab
    """
    cron = crontab.CronTab(user=True)
    cronjob = cron.new(command="python3 {(pathlib.Path(__file__).parent).__str__()}/gamblocker.py")
    cronjob.every_reboot()
    cron.write()

def remove_crontab():
    """
    Remove blocker crontab
    """
    cron = crontab.CronTab(user=True)
    job = cron.find_command("python3 {(pathlib.Path(__file__).parent).__str__()}/gamblocker.py")
    cron.remove(job)

def main():
    import_crontab()

    
if __name__ == "__main__":
    main()
