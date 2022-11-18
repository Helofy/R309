import MainWindow2
from PyQt5.QtWidgets import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow2.MainWindow2()
    window.show()
    app.exec_()