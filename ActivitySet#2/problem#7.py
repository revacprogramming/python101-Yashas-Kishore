

class Menu:
    
    def __init__(self):
        self.items={}
        
    
    def __add__(self,item,rate):
        self.item = item
        self.rate = rate
        self.items[self.item]=self.rate


    def show(self):
        for i in self.x:
            print(i,' ',self.x[i])


m = Menu()
m = m + ("idly" , 10) + ("vada" , 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

print(m)  # should print the menu properly
