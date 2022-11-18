from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        lab = QLabel("Saisir votre nom")
        self.__prenom=QLabel("")
        self.__text = QLineEdit("")
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")

        grid.addWidget(lab,0,0)
        grid.addWidget(self.__text,1,0)
        grid.addWidget(ok,0,1)
        grid.addWidget(self.__prenom,2,0)
        grid.addWidget(quit,1,1)


        ok.clicked.connect(self._actionOk)
        quit.clicked.connect(self._actionQuitter)
        quit.clicked.connect(self._actionQuitter)

    def _actionOk(self):
        x=self.__text.text()
        self.__prenom.setText("Bonjour " + x +' !')




    def _actionQuitter(self):
        QCoreApplication.exit(0)