from itertools import count
import os

# directory = "/Users/alexanderhaislip/Desktop"
directory = "/Users/somasz/Desktop/csTest1.txt"
shortcut_prefix = "~cs"
shortcut_suffix = "."
shortcut_Found = False


def install_how2():
    """checks for how2 installation or will install it if it is not found"""


def install_itertools():
    """checks for itertools installation or will install it if it is not found"""


def file_check():
    # open file for reading
    fp = open(directory, "r")

    # search for '~cs' command and return/print it
    for line in fp:
        if line.find(shortcut_prefix) != -1:
            fp.close()
            return line[0:line.index(shortcut_suffix)]

    fp.close()
    print("No " + shortcut_prefix + " command found")

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
