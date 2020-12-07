from itertools import count
import os

# Set this to True if you want to debug, otherwise False
DEBUG = True

# DIRECTORY = "/Users/alexanderhaislip/Desktop"
DIRECTORY = "/Users/somasz/Desktop/alexCodeScope/csTest1.txt"
SHORTCUT_PREFIX = "/cs"
SHORTCUT_SUFFIX = "."
SHORTCUT_FOUND = False


def install_how2():
    """checks for how2 installation or will install it if it is not found"""


def install_itertools():
    """checks for itertools installation or will install it if it is not found"""


def file_check():
    # open file for reading
    fp = open(DIRECTORY, "r")

    # search for '~cs' command and return/print it
    for line in fp:
        if line.find(SHORTCUT_PREFIX) != -1:

            # Ensure there is a '.' (suffix) after prefix
            if line.find(SHORTCUT_SUFFIX) == -1:
                fp.close()
                print("WARNING: No suffix: '" + SHORTCUT_SUFFIX + "' command found, returning.")
                return ""
            fp.close()
            return line[len(SHORTCUT_PREFIX):line.index(SHORTCUT_SUFFIX)]

    fp.close()
    return "No prefix '" + SHORTCUT_PREFIX + "' command found."


# Parameter: strToInsert is the string you want inserted into file
def insert_into_file(strToInsert):
    # Why TF does this need to be declared but not DIRECTORY or anything else
    SHORTCUT_FOUND = False

    if not os.path.isfile(DIRECTORY):
        print("WARNING: '" + DIRECTORY + "' is not a valid file")
        return

    # Create new file to write to
    newFileCreated = DIRECTORY + ".temp"
    if DEBUG:
        print(newFileCreated)

    fileToWrite = open(newFileCreated, "w")
    fileToRead = open(DIRECTORY, "r")

    for line in fileToRead:
        curLineIndex = line.find(SHORTCUT_PREFIX)

        if curLineIndex != -1:
            # Insert strToInsert into file
            fileToWrite.write(line[0:curLineIndex])
            fileToWrite.write(strToInsert)

            # Check for SHORTCUT_SUFFIX
            curLineIndex = line.find(SHORTCUT_SUFFIX)
            if curLineIndex == -1:
                print("ERROR: File does not contain 'shortcut suffix': " + SHORTCUT_SUFFIX)
                fileToRead.close()
                fileToWrite.close()
                # TODO could also ask if user still wants to insert code here, even though there is no '.'
                # This would just be a supplemental feature
                return
            fileToWrite.write(line[curLineIndex + len(SHORTCUT_SUFFIX):])
            SHORTCUT_FOUND = True
        else:
            # Copy line to fileToWrite
            fileToWrite.write(line)

    # Close files
    fileToRead.close()
    fileToWrite.close()

    # Overwrite fileToRead (DIRECTORY) with fileToWrite (newFileCreated)
    if DEBUG and SHORTCUT_FOUND:
        response = input("Are you sure you want to replace: " + DIRECTORY + "? (y/n) ")
        if response.lower() == "y" or response.lower() == "yes":
            os.remove(DIRECTORY)
            os.rename(newFileCreated, DIRECTORY)
            print("File modified successfully.")
        else:
            print("Created '" + newFileCreated + "' file with desired insertions.")
    elif SHORTCUT_FOUND:
        os.remove(DIRECTORY)
        os.rename(newFileCreated, DIRECTORY)
        print("File modified successfully.")
    else:
        # TODO Could make better by checking entire file for 'cs' command and not doing anything if not found.
        # TODO OR: call file_check before this to ensure 'cs' command is intact
        os.remove(newFileCreated)
        print("No '" + SHORTCUT_PREFIX + "' command found. Finished.")


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
