from codescope_functions import file_check, insert_into_file, query_how2, capture_file
from splashscreen_test import *
import time
import global_variables as cs_vars


def main():
    print("Initializing CodeScope... ")

    startup()
    print("startup complete")
    capture_file()
    print("capture file complete ")

    while cs_vars.CS_RUNNING:

        cs_command = file_check()
        if cs_command == "":
            print("No proper commands found!")
        if cs_command != "":
            answer = query_how2(cs_command)
            insert_into_file(str(answer))
        time.sleep(0.5)


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
