import os
import subprocess
import re
import sys
import codescope_variables as cs_vars
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap
from codescope_classes import MainWindow
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QFileDialog, QSplashScreen
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
import tkinter as tk



# Displays splash screen for codescope.
def startup_flash_splash():
    
    root = tk.Tk()
    # show no frame
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))

    # take a .jpg picture you like, add text with a program like PhotoFiltre
    # (free from http://www.photofiltre.com) and save as a .gif image file
    image_file = os.path.exists("/Users/alexanderhaislip/Projects/CodeScope")
    #assert os.path.exists(image_file)
    # use Tkinter's PhotoImage for .gif files
    image =image_file
    canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="brown")
    canvas.create_image(width*0.8/2, height*0.8/2, image=image)
    canvas.pack()

    # show the splash screen for 5000 milliseconds then destroy
    root.after(5000, root.destroy)
    root.mainloop()

    # your console program can start here ...    


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