import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.Qt import QIcon, QSize

form_class = uic.loadUiType("myOmok03.UI")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flagWb = True
        self.flagEnd = False
        self.pb.clicked.connect(self.myReset)
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            ]
        self.pb2D = []
        
        
        for i in range(10):
            line = []
            for j in range(10):
                btn = QPushButton(self)
                btn.setText('')
                btn.setIcon(QIcon('0.png'))
                btn.setIconSize(QSize(40, 40))
                btn.setGeometry(40 * (j % 10), 40 * i, 40, 40)
                btn.setToolTip('{}, {}'.format(i, j))
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2D.append(line)
        
        self.myrender()
           
    def myrender(self):
        for i in range(10) :
            for j in range(10) :
                if self.arr2D[i][j] == 0 :
                    self.pb2D[i][j].setIcon(QIcon('0.png'))
                elif self.arr2D[i][j] == 1 :
                    self.pb2D[i][j].setIcon(QIcon('1.png'))
                elif self.arr2D[i][j] == 2 :
                    self.pb2D[i][j].setIcon(QIcon('2.png'))
                        
                
    def myclick(self):
        if self.flagEnd == True:
            return
        
        btn = self.sender()
        location = btn.toolTip().split(",")
        i = int(location[0])
        j = int(location[1])
        # 돌이 놓여져있는 지를 확인하는 로직
        if self.arr2D[i][j] > 0 :
            return
        stone = -1
        if self.flagWb :
            self.arr2D[i][j] = 1
            stone = 1
        else :
            self.arr2D[i][j] = 2
            stone = 2
        
        up = self.checkUp(i, j, stone)
        dw = self.checkDw(i, j, stone)
        
        le = self.checkLe(i, j, stone)
        ri = self.checkRi(i, j, stone)
        
        ul = self.checkUl(i, j, stone)
        dr = self.checkDr(i, j, stone)
        
        ur = self.checkUr(i, j, stone)
        dl = self.checkDl(i, j, stone)
        
        d1 = up + dw + 1 
        d2 = ur + dl + 1 
        d3 = le + ri + 1 
        d4 = ul + dr + 1 
        
        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            if self.flagWb == True:
                QMessageBox.information(self, '경기 결과', '흰돌 승리!')
            else :
                QMessageBox.information(self, '경기 결과', '검은돌 승리!')
            self.flagEnd = True    
            
        self.flagWb = not self.flagWb
        
        
        
        
    def checkDl(self, i, j, stone):
        cnt = 0
        try:
            while True :
                i += 1
                j -= 1
                if i < 0 or j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
        
    def checkUr(self, i, j, stone):
        cnt = 0
        try:
            while True :
                i -= 1
                j += 1
                if i < 0 or j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
        
    def checkDr(self, i, j, stone):
        cnt = 0
        try:
            while True :
                i += 1
                j += 1
                if i < 0 or j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
        
    def checkUl(self, i, j, stone):
        cnt = 0
        try:
            while True :
                i -= 1
                j -= 1
                if i < 0 or j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt    
        
    def checkRi(self, i, j, stone):
        cnt = 0
        try:
            while True :
                j += 1
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt    
        
    def checkLe(self, i, j, stone):
        cnt = 0
        try:
            while True :
                j -= 1
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
            
    def checkUp(self, i, j, stone):
        cnt = 0
        # 파이썬에 있는 오류 때문임. 배열 index에 음수를 넣으면 배열을 역순으로 읽는 문제
        try:
            while True :
                i -= 1
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
            
    def checkDw(self, i, j, stone):
        cnt = 0
        try:
            while True :
                i += 1
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except IndexError:
            return cnt
             
    def myReset(self):
        print("check")
        
        self.flagWb = True
        self.flagEnd = False
        
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            ]
        
        self.myrender()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()