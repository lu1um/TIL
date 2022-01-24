import sys
import subprocess

def __init__():
    try:
        import selenium
        import PyQt5
        import schedule
    except:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'selenium'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pyqt5'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'schedule'])
        return False
    return True
    
