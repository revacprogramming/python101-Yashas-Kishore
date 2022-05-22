def input_two_numbers():
  x = input('input? ')
  y=x.split()
  g=y[0]
  h=y[1]
  return g,h


def add(a, b):
  u=int(a)
  v=int(b)
  p= u+v
  return p

def output(a, b, sum):
  print(a,'+',b, 'is',sum)

def main():
  a, b = input_two_numbers()
  sum = add(a, b)
  output(a, b, sum)

__name__= input('what r u doing? ')
if __name__ == 'addition':
  main()
