import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyMain02.UI")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.btn.clicked.connect(self.btnClick)
        
    def btnClick(self):
        # l = QLabel()
        # l.
        a = self.lbl.text()
        aa = int(a)
        aa -= 1
        self.lbl.setText(str(aa))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    