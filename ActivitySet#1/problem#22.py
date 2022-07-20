import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_71940.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

    # Converts the json to a dictionary
tree = json.loads(data)

iterations = 0
total = 0

    #This tree has 2 nodes in the first level: "note" and "comments"
    #This loop is only for the 'comments'
for item in tree['comments']:

    iterations = iterations + 1
    total = total + int(item['count'])  
        
print("Count:",iterations)
print("Sum:",total)