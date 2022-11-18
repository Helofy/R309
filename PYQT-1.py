import sys
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,QLineEdit
app = QApplication(sys.argv)
root = QWidget()
grid =QVBoxLayout()
root.setLayout(grid)
texte1=QLineEdit("test")

grid.addWidget(texte1)

root.resize(500, 300)
root.setWindowTitle("Hello world!")
root.show()
if __name__ == '__main__':
    sys.exit(app.exec_())