import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):  # --------------
        super(MainWindow, self).__init__(parent)  # |
        self.setWindowTitle("CodeScope")  # |
        btn = QPushButton("Select File ...")  # |---- Just initialization
        layout = QVBoxLayout()  # |
        layout.addWidget(btn)  # |
        widget = QWidget()  # |
        widget.setLayout(layout)  # |
        self.setCentralWidget(widget)  # -------------

        btn.clicked.connect(self.open)  # connect clicked to self.open()
        self.show()

    def open(self):
        path = QFileDialog.getOpenFileName(self, 'Select File ...', '',
                                           'All Files (*.*)')
        if path != ('', ''):
            print("File path : " + path[0])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
0
