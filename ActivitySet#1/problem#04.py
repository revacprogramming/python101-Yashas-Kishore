# Conditional Execution
'''




'''
'''
score = input("Enter Score: ")
sc = float(score)
if sc > 0.0 and sc < 1.0 :
    if sc >= 0.9:
        print('A')
    elif sc >= 0.8:
        print('B')
    elif sc  >= 0.7:
        print('C')
    elif sc >= 0.6:
        print('D')
    else:
        print('F')
else :
    print("enter valid marks within 0.0 to 1.0")
'''
score = input("Enter Score: ")
sc = float(score)
try :
    sc > 0.0 and sc < 1.0
    if sc >= 0.9:
        print('A')
    elif sc >= 0.8:
        print('B')
    elif sc >= 0.7:
        print('C')
    elif sc >= 0.6:
        print('D')
    else:
        print('F')
except :
    print("enter valid marks within 0.0 to 1.0")
  