from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
