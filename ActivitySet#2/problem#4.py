'''
#"""get string input"""
def get_cs():
    str=input('enter the shortcuts and its reps in form "word=sf" \n')
    return str

#"""convert connected string to list of strings"""
def cs_to_lot(cs,lst):
    word=cs.split(';')
    
    for exam in word:
      short=exam.split('=')
      tups(a,b)=(short[0],short[1])
      lst.append(tups)
    #for test in word:
        #lst.append(test)
    return lst

#"""convert list of strings to connected string"""
def lot_to_cs(lot):
    pass

def main():
    cs = get_cs()
    lot=list()
    lot = cs_to_lot(cs,lot)
    #print(lot)
    out=dict()
    cs=lot_to_cs(lot) 
    print(out.items())

def man():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
'''

#"""get string input"""
def get_cs():
    str=input('enter the shortcuts and its reps in form "word=sf" \n')
    return str

#"""convert connected string to list of strings"""
def cs_to_lot(cs,x):
    word=cs.split(';')
    for test in word:
        z=test.split('=')
        y=(z[0],z[1])
        x.append(y)
    return x

#"""convert list of strings to connected string"""
def lot_to_cs(lot):
    m=list()
    for i in lot:
        part="=".join(i)
        print(part)
        m.append(part)
    test=";".join(m)
    return test
        
def main():
    cs = get_cs()
    lot=list()
    lot = cs_to_lot(cs,lot)
    print(lot)
    #out=dict()
    cs=lot_to_cs(lot) 
    #print(out.items())
    #cs=lot_to_cs(lot)
    print(cs)

process=input('what process r u doing?')
if process == 'strsplit':
    main()
