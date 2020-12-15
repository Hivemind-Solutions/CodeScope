import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen, QWidget
from PyQt5.QtCore import QTimer

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.b1 = self
        Window.resize(self, 5, 5)
        self.b1.flashSplash()

    def flashSplash(self):

        self.splash = QSplashScreen(QPixmap('/Users/alexanderhaislip/Projects/CodeScope/codescope_logo.png'))
        self.splash.show()
        QTimer.singleShot(2000, self.splash.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    QTimer.singleShot(1500, main.close)
    main.show()
    sys.exit(app.exec_())