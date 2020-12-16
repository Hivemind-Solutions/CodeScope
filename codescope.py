from PyQt5.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout, QPushButton
from codescope_functions import file_check, insert_into_file, query_how2, capture_file
from splashscreen_test import *
import os


def main():
    print("Initializing CodeScope... ")

    startup()
    print("startup complete")
    capture_file()
    print("capture file complete ")

    while True:

        CS_COMMAND = file_check()
        if CS_COMMAND == "":
            print("No proper commands found!")
        if CS_COMMAND != "":
            ANSWER = query_how2(CS_COMMAND)
            insert_into_file(str(ANSWER))


def startup():
    class Window(QWidget):

        def __init__(self):
            super(Window, self).__init__()
            self.splash = QSplashScreen(QPixmap("codescope_logo.png"))
            self.b1 = self
            Window.resize(self, 5, 5)
            self.b1.flashSplash()

        def flashSplash(self):
            self.splash.show()
            QTimer.singleShot(2000, self.splash.close)
            self.close()

    app = QApplication(sys.argv)
    main = Window()
    QTimer.singleShot(1500, main.close)
    main.show()
    app.exec_()


if __name__ == '__main__':
    main()
