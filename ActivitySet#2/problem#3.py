



#"""get string input"""
def get_cs():
    str=input('enter the shortcuts and its reps in form "word=sf" \n')
    return str

#"""convert connected string to list of strings"""
def cs_to_lot(cs,lst):
    word=cs.split(';')
    for test in word:
        lst.append(test)
    return lst

def main():
    cs = get_cs()
    lot=list()
    lot = cs_to_lot(cs,lot)
    #print(lot)
    #out=dict()
    #for test in lot:
     #   short=test.split('=')
      #  out[short[0]] = short[1]
    print(lot)

process=input('what process r u doing? \n')
if process == 'strsplit':
    main()