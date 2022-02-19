import threading

def showNum():
    for i in range(1, 55203 + 1)  :
        print(i, end="")
        if i % 100 == 0 :
            print()

def showAscii():
    for i in range(1, 55203 + 1) :
        print(chr(i), end="")
        if i % 100 == 0 :
            print()
showNum()
showAscii()

t1 = threading.Thread(target=showNum)
t2 = threading.Thread(target=showAscii)
t1.start()
t2.start()