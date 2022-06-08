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