# Tuples

#filename = "dataset/mbox-short.txt"

'''
 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
final=dict()
for line in handle:
    if line.startswith("From"):
        test=line
        if not test.startswith('From:'):
            tonote=test.split()
            hrs = tonote[5]
            spec=hrs.split(':')
            spec1=spec[0]
            final[spec1]=final.get(spec1,0)+1
                #if spec1 in final:
                    #final[spec1] = final[spec1] + 1
                #else:
                    #final[spec1] = 1
            

for k,v in sorted(final.items()):
    print(k,v)