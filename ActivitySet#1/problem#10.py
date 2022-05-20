# Dictionaries

#filename = "dataset/mbox-short.txt"
'''
 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
fname = input("Enter file name: ")
fh = open(fname)
count = dict()
for line in fh:
    if line.startswith("From"):
        words=line.split()
        test=words[1]
        for test in words:
            if test in count:
                count[test] = count[test] + 1
            else:
                count[words[1]] = 1
        
#print(line.strip())
for k,v in count.items():
    print(k,v)
#print(count.keys())
#print(count.values())