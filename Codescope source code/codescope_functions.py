import os
import subprocess
import re
import sys
import codescope_variables as cs_vars
from PyQt5.QtWidgets import QApplication, QLabel, QSplashScreen
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap
from codescope_classes import MainWindow, SplashScreen
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

# Displays splash screen for codescope.
def startup():
    app = QApplication(sys.argv)
    splash_win = SplashScreen()
    QTimer.singleShot(1500, splash_win.close)
    splash_win.show()
    app.exec_()


def startup_flash_splash():
    app = QApplication(sys.argv)
    layout = QVBoxLayout()
    b1 = QPushButton('Display screensaver')
    layout.addWidget(QPushButton('Display screensaver'))


    splash = QSplashScreen(QPixmap('assets/codescope_logo.png'))

        # By default, SplashScreen will be in the center of the screen.
        # You can move it to a specific location if you want:
        # self.splash.move(10,10)

    splash.show()

        # Close SplashScreen after 2 seconds (2000 ms)
    QTimer.singleShot(2000, app.quit)
    app.exec_()
    return


# Creates GUI for select file after splash screen.
def capture_file():
    app = QApplication(sys.argv)
    m = MainWindow()
    m.center()
    m.show()
    app.exec_()
    # TODO when select file window is closed
    # cs_vars.CS_RUNNING = False


# Checks the selected file and ensures the codescope command is correct.
# Returns string to search in codescope command, otherwise return empty string.
def file_check():
    cs_command = ""

    if not os.path.isfile(cs_vars.DIRECTORY):
        if cs_vars.DEBUG:
            print("WARNING: '" + cs_vars.DIRECTORY + "' is not a valid file")
        return cs_command

    # open file for reading
    fp = open(cs_vars.DIRECTORY, "r")
    # setting the cs_shortcut to a variable

    # search for '/cs' command and return/print it
    for line in fp:
        if line.find(cs_vars.SHORTCUT_PREFIX) != -1:
            # Ensure there is a '.' (suffix) after prefix
            if line.find(cs_vars.SHORTCUT_SUFFIX) == -1:
                fp.close()
                if cs_vars.DEBUG:
                    print("WARNING: No suffix: '" + cs_vars.SHORTCUT_SUFFIX + "' command found, returning.")
                return cs_command
            fp.close()
            cs_command = line[len(cs_vars.SHORTCUT_PREFIX):line.index(cs_vars.SHORTCUT_SUFFIX)]
            return cs_command

    fp.close()
    if cs_vars.DEBUG:
        print("No prefix '" + cs_vars.SHORTCUT_PREFIX + "' command found.")
    return cs_command


# Inserts the specified string into the file at the codescope command location.
# Parameter: str_to_insert is the string you want inserted into file
def insert_into_file(str_to_insert):
    # Ensure directory is valid
    if not os.path.isfile(cs_vars.DIRECTORY):
        if cs_vars.DEBUG:
            print("WARNING: '" + cs_vars.DIRECTORY + "' is not a valid file")
        return

    # Create new file to write to
    new_file_created = cs_vars.DIRECTORY + ".temp"
    if cs_vars.DEBUG:
        print(new_file_created)

    file_to_write = open(new_file_created, "w")
    file_to_read = open(cs_vars.DIRECTORY, "r")

    # Go through file line by line to find where to insert
    for line in file_to_read:
        cur_line_index = line.find(cs_vars.SHORTCUT_PREFIX)

        if cur_line_index != -1:
            # Insert strToInsert into file
            file_to_write.write(line[0:cur_line_index])
            file_to_write.write(str_to_insert)

            # Check for SHORTCUT_SUFFIX
            cur_line_index = line.find(cs_vars.SHORTCUT_SUFFIX)
            if cur_line_index == -1:
                if cs_vars.DEBUG:
                    print("WARNING: File does not contain 'shortcut suffix': " + cs_vars.SHORTCUT_SUFFIX)
                file_to_read.close()
                file_to_write.close()
                return
            file_to_write.write(line[cur_line_index + len(cs_vars.SHORTCUT_SUFFIX):] + "----------" + "\n")
            cs_vars.SHORTCUT_FOUND = True
        else:
            # Copy line to file_to_write
            file_to_write.write(line)

    # Close files
    file_to_read.close()
    file_to_write.close()

    # Overwrite file_to_read (DIRECTORY) with file_to_write (new_file_created)
    if cs_vars.DEBUG and cs_vars.SHORTCUT_FOUND:
        response = "yes"
        if response == "yes":
            os.remove(cs_vars.DIRECTORY)
            os.rename(new_file_created, cs_vars.DIRECTORY)
            if cs_vars.DEBUG:
                print("File modified successfully.")
        else:
            if cs_vars.DEBUG:
                print("Created '" + new_file_created + "' file with desired insertions.")
    elif cs_vars.SHORTCUT_FOUND:
        os.remove(cs_vars.DIRECTORY)
        os.rename(new_file_created, cs_vars.DIRECTORY)
        if cs_vars.DEBUG:
            print("File modified successfully.")
    else:
        # No
        os.remove(new_file_created)
        if cs_vars.DEBUG:
            print("No '" + cs_vars.SHORTCUT_PREFIX + "' command found. Finished.")


# Queries the how2 API to find result for command.
def query_how2(cs_command):
    FILE = os.path.basename(cs_vars.DIRECTORY)
    if cs_vars.DEBUG:
        print(FILE)
        print(cs_vars.DIRECTORY)
    DIRECTORY_PATH = cs_vars.DIRECTORY.replace(str(FILE), '')
    print(DIRECTORY_PATH)

    if cs_command != "":
        print("Finding answers...")
    os.system("cd " + DIRECTORY_PATH)
    RESULT = subprocess.run(["how2", cs_command], capture_output=True, text=True).stdout

    RESULT = re.sub('You should use the option', '', RESULT)
    re.sub('to specify the language.', '', RESULT)
    RESULT = re.sub('Press SPACE for more choices, any other key to quit.', '', RESULT)

    if cs_vars.DEBUG:
        print(RESULT)
    return RESULT