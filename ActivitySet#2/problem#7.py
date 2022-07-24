class Menu:
    
    
    def __init__(self):
      self.foods={}
    
    
    def __add__(self,x):
      if(x[0] in self.foods):
        self.foods[x[0]]+=x[1]
      else:
        self.foods[x[0]]=x[1]
      return self


    def __str__(self):
      k=""
      for a in self.foods:
        k+=(f"{a}  {self.foods[a]}\n")
      return(k[:-1])



m = Menu()
m = m + ("idly", 10)+ ("vada",20) 

print(m)
