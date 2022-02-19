import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyMain07.UI")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        self.leMine.returnPressed.connect(self.btnClick)
        
    def btnClick(self):
        a = ""
        com = ""
        result = ""
        
        a = self.leMine.text()
        
        rnd = random.random()
        
        if rnd > 0.66:
            com = "가위"
        elif rnd > 0.33:
            com = "바위"
        else:
            com = "보"
        
        self.leCom.setText(com);    
            
        if a == "가위" and com == "바위" :
            result = "컴 승리"
        if a == "가위" and com == "보" :
            result = "나 승리"
        if a == "가위" and com == "가위" :
            result = "무승부"
        if a == "바위" and com == "보" :
            result = "컴 승리"
        if a == "바위" and com == "가위" :
            result = "나 승리"
        if a == "바위" and com == "바위" :
            result = "무승부"
        if a == "보" and com == "가위" :
            result = "컴 승리"
        if a == "보" and com == "바위" :
            result = "나 승리"
        if a == "보" and com == "보" :
            result = "무승부"              
        
        self.leResult.setText(result);      
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    