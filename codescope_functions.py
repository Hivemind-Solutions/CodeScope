import os
import subprocess
import re
import sys
import global_variables as cs_vars
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QFileDialog, QDesktopWidget


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
        path = QFileDialog.getOpenFileName(self, 'Select File ...', '')
        if path != ('', ''):
            cs_vars.DIRECTORY = path[0]
            print(cs_vars.DIRECTORY)
            self.close()
            return cs_vars.DIRECTORY

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
    # cs_vars.CS_RUNNING = False


def file_check():

    if not os.path.isfile(cs_vars.DIRECTORY):
        if cs_vars.DEBUG:
            print("WARNING: '" + cs_vars.DIRECTORY + "' is not a valid file")
        return ""

    # open file for reading
    fp = open(cs_vars.DIRECTORY, "r")
    # setting the cs_shortcut to a varible

    # search for '/cs' command and return/print it
    for line in fp:
        if line.find(cs_vars.SHORTCUT_PREFIX) != -1:

            # Ensure there is a '.' (suffix) after prefix
            if line.find(cs_vars.SHORTCUT_SUFFIX) == -1:
                fp.close()
                if cs_vars.DEBUG:
                    print("WARNING: No suffix: '" + cs_vars.SHORTCUT_SUFFIX + "' command found, returning.")
                return ""
            fp.close()
            CSCOMMAND = line[len(cs_vars.SHORTCUT_PREFIX):line.index(cs_vars.SHORTCUT_SUFFIX)]
            return CSCOMMAND

    fp.close()
    if cs_vars.DEBUG:
        print("No prefix '" + cs_vars.SHORTCUT_PREFIX + "' command found.")
    return ""


# Parameter: strToInsert is the string you want inserted into file
def insert_into_file(strToInsert):
    # Why TF does this need to be declared but not DIRECTORY or anything else
    # SHORTCUT_FOUND = False

    if not os.path.isfile(cs_vars.DIRECTORY):
        if cs_vars.DEBUG:
            print("WARNING: '" + cs_vars.DIRECTORY + "' is not a valid file")
        return

    # Create new file to write to
    newFileCreated = cs_vars.DIRECTORY + ".temp"
    if cs_vars.DEBUG:
        print(newFileCreated)

    fileToWrite = open(newFileCreated, "w")
    fileToRead = open(cs_vars.DIRECTORY, "r")

    for line in fileToRead:
        curLineIndex = line.find(cs_vars.SHORTCUT_PREFIX)

        if curLineIndex != -1:
            # Insert strToInsert into file
            fileToWrite.write(line[0:curLineIndex])
            fileToWrite.write(strToInsert)

            # Check for SHORTCUT_SUFFIX
            curLineIndex = line.find(cs_vars.SHORTCUT_SUFFIX)
            if curLineIndex == -1:
                if cs_vars.DEBUG:
                    print("ERROR: File does not contain 'shortcut suffix': " + cs_vars.SHORTCUT_SUFFIX)
                fileToRead.close()
                fileToWrite.close()
                return
            fileToWrite.write(line[curLineIndex + len(cs_vars.SHORTCUT_SUFFIX):] + "----------" + "\n")
            SHORTCUT_FOUND = True
        else:
            # Copy line to fileToWrite
            fileToWrite.write(line)

    # Close files
    fileToRead.close()
    fileToWrite.close()

    # Overwrite fileToRead (DIRECTORY) with fileToWrite (newFileCreated)
    if cs_vars.DEBUG and SHORTCUT_FOUND:

        RESPONSE = "yes"
        if RESPONSE == "yes":
            os.remove(cs_vars.DIRECTORY)
            os.rename(newFileCreated, cs_vars.DIRECTORY)
            if cs_vars.DEBUG:
                print("File modified successfully.")
        else:
            if cs_vars.DEBUG:
                print("Created '" + newFileCreated + "' file with desired insertions.")
    elif SHORTCUT_FOUND:
        os.remove(cs_vars.DIRECTORY)
        os.rename(newFileCreated, cs_vars.DIRECTORY)
        if cs_vars.DEBUG:
            print("File modified successfully.")
    else:
        # TODO Could make better by checking entire file for 'cs' command and not doing anything if not found.
        # TODO OR: call file_check before this to ensure 'cs' command is intact
        os.remove(newFileCreated)
        if cs_vars.DEBUG:
            print("No '" + cs_vars.SHORTCUT_PREFIX + "' command found. Finished.")


def query_how2(CS_COMMAND):
    FILE = os.path.basename(cs_vars.DIRECTORY)
    if cs_vars.DEBUG:
        print(FILE)
        print(cs_vars.DIRECTORY)
    # TODO removes 'C' drive name for windows, should not do that
    DIRECTORY_PATH = cs_vars.DIRECTORY.strip(str(FILE))
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
