from itertools import count
import os

directory = "/Users/alexanderhaislip/Desktop"
shortcut_prefix = "~cs"
shortcut_suffix = "."
shortcut_Found = False


def install_how2():
    """checks for how2 installation or will install it if it is not found"""


def install_itertools():
    """checks for itertools installation or will install it if it is not found"""


def file_check():
    files = os.listdir(directory)
    print(files)

    """ with open('/Users/alexanderhaislip/Desktop/testproject') as f:
        if '/cs' in f.read():
            print("Command found!")
        else:
            print("No CodeScope commands found...")
"""

def translate():
    print("Translating command...")
    """after identifing the shorcut identifier it will take the text in between /cs and . to 
	convert it into how2 text in shortcut"""


def query():
    print("Finding answers...")
    """open new terminal session and paste how2 translation"""


def copy():
    print("Making things nice...")
    """copy code from terminal"""


def inject():
    print("Pooping an answer in your file")
    "injects copied texts to end of file"


def remove_shortcut():
    """removes the /cs command that was found"""
