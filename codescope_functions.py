import os
import subprocess
import re
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QFileDialog, QDesktopWidget

DEBUG = True
DIRECTORY = ""
SHORTCUT_PREFIX = "/cs"
SHORTCUT_SUFFIX = "."
SHORTCUT_FOUND = False
TYPESCRIPT_NAME = "typescript"


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("CodeScope")
        btn = QPushButton("Select File ...")
        layout = QVBoxLayout()
        layout.addWidget(btn)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        btn.clicked.connect(self.open)
        self.show()

    def open(self):
        global DIRECTORY
        path = QFileDialog.getOpenFileName(self, 'Select File ...', '')
        if path != ('', ''):
            DIRECTORY = path[0]
            print(DIRECTORY)
            self.close()
            return DIRECTORY

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def capture_file():
    app = QApplication(sys.argv)
    m = MainWindow()
    m.center()
    m.show()
    app.exec_()

def file_check():
    # open file for reading
    fp = open(DIRECTORY, "r")
    # setting the cs_shortcut to a varible

    # search for '/cs' command and return/print it
    for line in fp:
        if line.find(SHORTCUT_PREFIX) != -1:

            # Ensure there is a '.' (suffix) after prefix
            if line.find(SHORTCUT_SUFFIX) == -1:
                fp.close()
                print("WARNING: No suffix: '" + SHORTCUT_SUFFIX + "' command found, returning.")
                return ""
            fp.close()
            CSCOMMAND = line[len(SHORTCUT_PREFIX):line.index(SHORTCUT_SUFFIX)]
            return CSCOMMAND

    fp.close()
    print("No prefix '" + SHORTCUT_PREFIX + "' command found.")
    return ""


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
                return
            fileToWrite.write(line[curLineIndex + len(SHORTCUT_SUFFIX):] + "----------" + "\n")
            SHORTCUT_FOUND = True
        else:
            # Copy line to fileToWrite
            fileToWrite.write(line)

    # Close files
    fileToRead.close()
    fileToWrite.close()

    # Overwrite fileToRead (DIRECTORY) with fileToWrite (newFileCreated)
    if DEBUG and SHORTCUT_FOUND:

        RESPONSE = "yes"
        if RESPONSE == "yes":
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


def query_how2(CS_COMMAND):
    FILE = os.path.basename(DIRECTORY)
    DIRECTORY_PATH = DIRECTORY.strip(FILE + "")
    DIRECTORY_PATH = DIRECTORY_PATH[:-1]
    print(DIRECTORY_PATH)
    if CS_COMMAND != "":
        print("Finding answers...")
    os.system("cd " + DIRECTORY_PATH)
    RESULT = subprocess.run(["how2", CS_COMMAND], capture_output=True, text=True).stdout

    RESULT = re.sub('You should use the option', '', RESULT)
    re.sub('to specify the language.', '', RESULT)
    RESULT = re.sub('Press SPACE for more choices, any other key to quit.', '', RESULT)
    print(RESULT)
    return RESULT
