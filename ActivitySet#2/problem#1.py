

def add(a, b):
  p=int(a)
  q=int(b)
  c = p+q
  return c


def main():
    a = input('Enter 1st number? ') 
    b = input('Enter 2nd number? ')
    c = add(a, b)
    print('Sum of',a,'and',b,'is',c )

main()