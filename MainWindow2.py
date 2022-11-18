from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
class MainWindow2(QMainWindow):
    def __init__(self):

        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        temp= QLabel("Température")
        self.__valtemp = QLineEdit("")
        self.__t1 = QLabel("C")
        bouton = QPushButton("Convertir")
        self.__chose=QComboBox()
        self.__chose.addItems(["C-> K","K-> C"])
        conv=QLabel("Conversion")
        self.__result=QLabel("")
        self.__t2=QLabel("K")

        grid.addWidget(temp,0,0,)
        grid.addWidget(self.__valtemp,0,1)
        grid.addWidget(self.__t1,0,2)
        grid.addWidget(bouton,1,1)
        grid.addWidget(self.__chose,1,2)
        grid.addWidget(conv,2,0)
        grid.addWidget(self.__result,2,1)
        grid.addWidget(self.__t2,2,2)

        self.__chose.activated.connect(self.Combobox)
        bouton.clicked.connect(self.conversion)

    def Combobox(self):
        if self.__chose.currentText() == 'C-> K':
                self.__t1.setText("C")
                self.__t2.setText("K")
        else:
                self.__t2.setText("C")
                self.__t1.setText("K")
    def conversion(self):
        x=float(self.__valtemp.text())
        if self.__t1.text() =='C':
            x+=273.15
            self.__result.setText(str(x))

        else:
            x-=273.15
            self.__result.setText(str(x))

