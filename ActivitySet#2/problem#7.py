class Menu:
    
    def __init__(self):
        self.items={}
        
    
    def __add__(self,item):
        self.items[item[0]] = item[1]
        return self

    def __str__(self):
        for k,v in self.items.items():
            print(k, v)
        
m = Menu()
# Hint: operator overloading special methods (__add__, __sub__, etc.)
m = m + ("idly" , 10) + ("vada" , 20)  

print(m)