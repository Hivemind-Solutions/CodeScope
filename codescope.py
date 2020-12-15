from PyQt5.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout, QPushButton
from codescope_functions import file_check, insert_into_file, query, capture_file
from splashscreen_test import *


def startup():
    class Window(QWidget):

        def __init__(self):
            super(Window, self).__init__()

            self.splash = QSplashScreen(QPixmap('/Users/alexanderhaislip/Projects/CodeScope/codescope_logo.png'))
            self.b1 = self
            Window.resize(self, 5, 5)
            self.b1.flashSplash()

        def flashSplash(self):
            self.splash.show()
            QTimer.singleShot(2000, self.splash.close)

    app = QApplication(sys.argv)
    main = Window()
    QTimer.singleShot(1500, main.close)
    main.show()
    sys.exit(app.exec_())

def select_file():
    selectFile()


def main():
    print("Initializing CodeScope... ")

    CS_COMMAND = file_check()

    if CS_COMMAND == "":
        print("No proper commands found!")
        return

    ANSWER = query(CS_COMMAND)

    insert_into_file(str(ANSWER))


while True:
    if __name__ == '__main__':
        startup()
        capture_file()
        main()
