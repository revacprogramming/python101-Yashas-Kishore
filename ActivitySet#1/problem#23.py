import sqlite3

    #Read the filename or if null use the standard name
name = input("Enter file:")
if len(name) < 1 : name = "mbox.txt"
handle = open(name)

templist = list()
count = 0

    #Open database connection
conn = sqlite3.connect('CountingOrganizations.sqlite')
cur = conn.cursor()

    #Create table or delete its content
cur.execute('''CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)''')           
cur.execute('''DELETE FROM Counts''') 

    #Find all emails in the From lines
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
         #Get the domains
    words = line.split()
    domain = words[1].split("@")
         #Check if domain exist in the database         
    cur.execute('''SELECT count FROM Counts where org = ?''',(domain[1],))
    count = cur.fetchone()
         #If not create an entry
    if count is None: 
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?,1)''',(domain[1],))
    else :
              #If it does update the record
        cur.execute('''UPDATE Counts SET count = count + 1  WHERE org = ?''',(domain[1],))
         
conn.commit()

table = 'SELECT org, count FROM Counts ORDER BY count DESC'
for line in cur.execute(table): 
    print(str(line[0]), ":", str(line[1]))

conn.close()