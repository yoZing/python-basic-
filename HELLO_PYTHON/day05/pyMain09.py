import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyMain09.UI")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
        self.pbCall.clicked.connect(self.myCall)
        self.pb1.clicked.connect(self.pbClick)
        self.pb2.clicked.connect(self.pbClick)
        self.pb3.clicked.connect(self.pbClick)
        self.pb4.clicked.connect(self.pbClick)
        self.pb5.clicked.connect(self.pbClick)
        self.pb6.clicked.connect(self.pbClick)
        self.pb7.clicked.connect(self.pbClick)
        self.pb8.clicked.connect(self.pbClick)
        self.pb9.clicked.connect(self.pbClick)
        self.pb0.clicked.connect(self.pbClick)
    
    def myCall(self):
        tel = self.le.text()
        QMessageBox.question(self, "calling", tel, QMessageBox.Yes, QMessageBox.NoButton)
        
    def pbClick(self):
        a = self.le.text()
        b = self.sender()
        bb = b.text()
        c = a + bb
        self.le.setText(c)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    