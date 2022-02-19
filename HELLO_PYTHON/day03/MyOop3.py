class Animal:
    def __init__(self):
        self.myLife = 100
        self.myAge = 0
        
    def getAge(self):
        self.myAge += 1
        self.myLife -= 1
           
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.skil_lang = 1
    
    def exp(self, mama):
        self.skil_lang += mama    
    

if __name__=='__main__':
    hum = Human()
    print(hum.myAge)
    print(hum.myLife)
    print(hum.skil_lang)
    hum.getAge()
    hum.exp(100)
    print(hum.myAge)
    print(hum.myLife)
    print(hum.skil_lang)

