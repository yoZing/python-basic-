import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyMain05.UI")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        led1 = ""
        led2 = ""
        led3 = ""
        led4 = ""
        led5 = ""
        led6 = ""
        
        arr45 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                 41, 42, 43, 44, 45]
        
        arr6 = []
        
        while len(arr6) < 6 :
            rnd = int(random.random() * 45)
            
            if arr45[rnd] > 0 :
                arr6.append(arr45[rnd])
                arr45[rnd] = -1
            else :
                continue
        
        
        for i in range(len(arr6)) :
            for j in range(len(arr6)) :
                if arr6[i] < arr6[j] :
                    a = arr6[j]
                    arr6[j] = arr6[i]
                    arr6[i] = a

        led1 = arr6[0]
        led2 = arr6[1]
        led3 = arr6[2]
        led4 = arr6[3]
        led5 = arr6[4]
        led6 = arr6[5]             
        
        self.le1.setText(str(led1))
        self.le2.setText(str(led2))
        self.le3.setText(str(led3))
        self.le4.setText(str(led4))
        self.le5.setText(str(led5))
        self.le6.setText(str(led6))
        
    def keyPressEvent(self, e) :
        if e.key() == Qt.Key_Return :
            self.btnClick()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    