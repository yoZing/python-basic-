class Animal:
    def __init__(self, myYear):
        print("생성자", myYear)
        self.myLife = 100
        self.myAge = myYear
        
    def getAge(self):
        self.myAge += 1
        self.myLife -= 1
        
    def __del__(self):
        print("소멸자", self.myAge)
        
print("MyOop", __name__)        
        
if __name__ == '__main__':
    ani1 = Animal(5)