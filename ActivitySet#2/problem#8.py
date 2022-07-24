
class Menu:
    """fill in class definition here"""
    def __init__(self) -> None:
        self.foods={}
        
        pass
    def __setitem__(self,item,price):
        self.foods[item]=price

    def __str__(self):
        s=""    
        for i in self.foods:
            s+=(f"{i}  {self.foods[i]}\n")
        return (s[:-1])

m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)
