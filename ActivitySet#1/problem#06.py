# Loops & Iterators

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
