class Xi:
    def __init__(self):
        self.wealth = 10
        
    def myExport(self, quantity):
        self.wealth += quantity
        
    def hanhanryoung(self):
        print("못가져가")
        
    def myImport(self, quantity):
        self.wealth -= quantity        
        
class Baiden:
    def __init__(self):
        self.militaryPower = 10
        
    def makePower(self):
        self.militaryPower += 1
        
class TaeHyung(Xi, Baiden):
    def __init__(self):
        Xi.__init__(self)
        Baiden.__init__(self)
        
if __name__=='__main__':
    th = TaeHyung()
    print(th.wealth)
    print(th.militaryPower)
    th.myExport(10)
    th.makePower()
    print(th.wealth)
    print(th.militaryPower)
