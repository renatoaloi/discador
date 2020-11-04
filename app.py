from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, QTextEdit, QDialog, QPushButton, QMessageBox
from robo import Robo
import sys

class Janela(QDialog):
    def __init__(self, **args):
        super(Janela, self).__init__(**args)
        self.setWindowTitle("Discador")
        self.__ui__()
        self.resize(300, 400)
        self.robo = Robo()

    def __ui__(self):
        self.setLayout(QGridLayout())
        # botao 1
        button = QPushButton("Robo 1")
        button.clicked.connect(self.robo1)
        self.layout().addWidget(button)

    def robo1(self):
        self.robo.run_task()
    
if __name__ == '__main__':
    app = QApplication([])
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())
