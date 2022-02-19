import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyMain04.UI")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
        self.leMine.returnPressed.connect(self.btnClick)
        
    def btnClick(self):
        mine = ""
        com = ""
        result = ""
        
        mine = self.leMine.text()
        rnd = random.random()
        
        if rnd > 0.5:
            com = "홀"
        else :
            com = "짝"
            
        if (mine == "홀" and com == "짝") :
            result = "이김"
        else :
            result = "짐"            
        
        self.leCom.setText(com)
        self.leResult.setText(result)
        
    def keyPressEvent(self, event) :
        if event.key() == Qt.Key_Enter :
            self.btnClick()
            
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    