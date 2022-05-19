# Lists

#filename = "dataset/romeo.txt"
'''
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
'''
'''
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words=fh.split()
    for test in words:
        range(len(words)
        if test not in lst
              lst.append(test)
print(line.strip())
'''
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
  words=line.split()
  for test in words:
    if test not in lst:
      lst.append(test)
    else:
      continue
#print(line.strip())
lst.sort()
print(lst)
