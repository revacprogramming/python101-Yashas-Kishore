import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_71939.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

    #Converts the xml to a string
tree = ET.fromstring(data)

    #filters by .//count same as comments/comment/count
results = tree.findall('.//count')
iterations = 0
total = 0

    #Loop all items in the list
for item in results:

    iterations = iterations + 1
        
        #Gets the text value from the tag count
    total = total + int(item.text)    
        
print("Count:",iterations)
print("Sum:",total)