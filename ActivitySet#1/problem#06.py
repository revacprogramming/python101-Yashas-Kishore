# Loops & Iterators
'''
largest = none
smallest = none

while True:
  num = input("Enter a number: ")
  if num == "done":
    break
  try:
    x=int(num)
    if largest is none or largest<x:
      largest=x
    if smallest  is none or smallest>x:
      smallest=x
	except:
    print("invalid input")
        
      
print("Maximum is", largest)       
print("Minimum is",smallest)
'''
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    
    if num == "over":
        break
    try :
        a = int(num)
        
        if largest is None:
            largest = a
        elif largest>a :
            largest = largest
        else :
            largest=a
        if smallest is None:
            smallest= a
        elif smallest < a:
            smallest= smallest
        else:
            smallest= a      
   
       
    except:
        print ("Invalid input")
        
print("Maximum is", largest)
print("Minimum is",smallest)