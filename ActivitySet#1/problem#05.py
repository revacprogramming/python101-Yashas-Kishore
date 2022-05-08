# Functions


def computepay(hr, r):
    h = float(hr)
    
    rt = float(r)
    if h > 40 :
        # print('overtime')
        ovt = h-40
        h = 40
    else :
        # print ("regular")
        h = h + 0
        ovt = 0
    ptm = (h*rt) + (ovt*(rt*1.5))
    return(ptm)
hrs = input("Enter Hours:")
rtph = input("enter the rate per hour:")
p = computepay(hrs,rtph)
print("Pay", p)