import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location: ')
    #address = "South Federal University"
    #address = "University of Chicago"

url = serviceurl + urllib.parse.urlencode({'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
    print("Place id",js["results"][0]["place_id"])

except:
    js = None  
    print('==== Failure To Retrieve ====')