import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import Qt

form_class = uic.loadUiType("pyMain06.UI")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        a = "";
        result = "";
        
        a = self.le.text()
        aa = int(a)
        
        result += a + "단\n"
        
        for i in range(1, 9 + 1) :
            result += a + " x " + str(i) + " = " + str(aa * i) + "\n"
        
        result += "\n"
        self.te.setText(result)
        
    def keyPressEvent(self, event) :
        if event.key() == Qt.Key_Return :
            self.btnClick()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    