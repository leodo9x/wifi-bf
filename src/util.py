import urllib.request
import os
from enum import Enum

class Color(Enum):
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[37m'

    def __call__(self, text):
        return f"{self.value}{text}{Color.END.value}"

def fetch_from_url(url):
    try:
        return urllib.request.urlopen(url)
    except Exception as e:
        print(f"{Color.FAIL('Error')}: Failed to fetch from URL: {e}")
        return None

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_header():
    clear()
    print(Color.GREEN('''
==============================================================
	██╗    ██╗██╗███████╗██╗      ██████╗ ███████╗
	██║    ██║██║██╔════╝██║      ██╔══██╗██╔════╝
	██║ █╗ ██║██║█████╗  ██║█████╗██████╔╝█████╗
	██║███╗██║██║██╔══╝  ██║╚════╝██╔══██╗██╔══╝
	╚███╔███╔╝██║██║     ██║      ██████╔╝██║
	 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝      ╚═════╝ ╚═╝
==============================================================
    '''))