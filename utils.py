import sys, os
from datetime import datetime

def get_resource_path(filename):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(__file__), filename)

def today_str():
    return datetime.today().strftime("%d.%m.%y")
