hrs = input("Enter Hours:")
h = float(hrs)
rtph = input("enter the rate per hour:")
rt = float(rtph)
if h > 40 :
  print('overtime')
  ovt = h-40
  print(ovt,'hrs')
  h = 40
else :
  print ("regular")
  h = h + 0
  ovt = 0
ptm = (h*rt) + (ovt*(rt*1.5))

print(ptm)