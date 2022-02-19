import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyMain08.UI")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        a = ""
        b = ""
        result = ""
        
        a = self.leFirst.text()
        b = self.leLast.text()
        
        aa = int(a)
        bb = int(b)
        
        for i in range(aa, bb + 1) :
            result += self.drawStar(i)
        
        self.te.setText(result)
        
    def drawStar(self, count):
        result = ""
        
        for i in range(count):
            result += "*"
        result += "\n"
        return result    
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    