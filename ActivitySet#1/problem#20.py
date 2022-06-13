import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
#def retr(tags):
    #for tag in tags:
        #print(tag.get('href', None))
'''       
for tag in tags:
    test=tag.get('href', None)
    html2 = urllib.request.urlopen(test, context=ctx).read()
    soup2=BeautifulSoup(html2, 'html.parser')
    troops = soup2('a')
    for troop in troops:
      print(troop.get('href', None))
#for tagg in tags:
    #retr(tagg)
'''
while True:
  tag = tags[3]
  html2 = urllib.request.urlopen(tag, context=ctx).read()
  soup2=BeautifulSoup(html2, 'html.parser')
  troops = soup2('a')
  