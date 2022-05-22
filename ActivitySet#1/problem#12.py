# Regular Expressions
# https://www.py4e.com/lessons/regex

import re
#regex_sum_42.txt =445833
#regex_sum_1544108.txt = 394548
file=input('enter the file name:')
fhand=open(file)
number=list()
for line in fhand:
    line=line.rstrip()
    nums = re.findall('[0-9]+',line)
    #if len(nums) != 1: continue
    for i in nums:
        num=int(i)
        number.append(num)
    
print(sum(number))