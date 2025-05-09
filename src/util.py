import urllib.request
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    VERBOSEGRAY = '\033[37m'


def fetch_password_from_url(url):
    try:
        return urllib.request.urlopen(url)
    except:
        return None

def clear():
    os.system('clear')

def header():
    print('''
==============================================================
	██╗    ██╗██╗███████╗██╗      ██████╗ ███████╗
	██║    ██║██║██╔════╝██║      ██╔══██╗██╔════╝
	██║ █╗ ██║██║█████╗  ██║█████╗██████╔╝████E╗
	██║███╗██║██║██╔══╝  ██║╚════╝██╔══██╗██╔══╝
	╚███╔███╔╝██║██║     ██║      ██████╔╝██║
	 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝      ╚═════╝ ╚═╝
==============================================================
    ''')