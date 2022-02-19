import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyMain03.UI")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.btn.clicked.connect(self.btnClick)
        
    def btnClick(self):
        a = self.le1.text()
        b = self.le2.text()
        
        aa = int(a)
        bb = int(b)
        
        c = aa - bb
        
        self.le3.setText(str(c))
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    