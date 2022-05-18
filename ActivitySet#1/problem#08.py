# Files

#filename = "dataset/mbox-short.txt"
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
avg=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    test=line.find(':')
    toadd=line[test+1 : ]
    fcopy=float(toadd)
    avg=avg+fcopy
    count=count+1
    #print(fcopy)
    #print(line)
result=avg/count
print("Average spam confidence:",result)

