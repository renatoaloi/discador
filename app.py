from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit, QWidget, QLabel, QTextEdit, QDialog, QPushButton, QMessageBox
from robo import Robo
import sys

class Janela(QDialog):
    def __init__(self, **args):
        super(Janela, self).__init__(**args)
        self.setWindowTitle("Discador")
        self.__ui__()
        self.resize(300, 300)
        #self.setStyle('Windows')
        self.robo = Robo()

    def __ui__(self):
        self.setLayout(QGridLayout())
        # url
        self.layout().addWidget(QLabel("URL:"))
        self.url = QLineEdit()
        self.layout().addWidget(self.url)
        # texto de dados
        self.layout().addWidget(QLabel("Dados:"))
        self.text = QTextEdit()
        self.layout().addWidget(self.text)
        # botao 1
        button = QPushButton("Discar")
        button.clicked.connect(self.robo1)
        self.layout().addWidget(button)

    def robo1(self):
        self.robo.run_task(self.url.text(), self.text.toPlainText())
    
if __name__ == '__main__':
    app = QApplication([])
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())
