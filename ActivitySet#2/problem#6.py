

class Menu:
    x=dict()
    def add(self, item, rate):
        self.item = item
        self.rate = rate
        self.x[item]=rate

    def show(self):
        for i in self.x:
            print(i,' ',self.x[i])
            

m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada", 20)

m.show()
