

def get_cs():
    """get string input"""
    str=input('enter the shortcuts and its reps in form "word=sf" \n')
    return str


def cs_to_dict(cs):
    word=cs.split(';')
    y=dict()
    for test in word:
        z=test.split('=')
        y[z[0]]=z[1]
        
    return y

def dict_to_cs(d):
    m=list()
    for i in d:
        x=i+d[i]
        m.append(x)
    test=";".join(m)
    return test


def main():

    
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
