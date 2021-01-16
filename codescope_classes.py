import codescope_variables as cs_vars
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QFileDialog, QDesktopWidget, QSplashScreen, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer


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
            if cs_vars.DEBUG:
                print(cs_vars.DIRECTORY)
            self.close()
            return cs_vars.DIRECTORY

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# Not used, replaced by startup_flash_splash
class SplashScreen(QWidget):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.splash = QSplashScreen(QPixmap('assets/codescope_logo.png'))
        self.b1 = self
        SplashScreen.resize(self, 5, 5)
        self.b1.flash_splash()

    def flash_splash(self):
        self.splash.show()
        QTimer.singleShot(2000, self.splash.close)
        self.close()
