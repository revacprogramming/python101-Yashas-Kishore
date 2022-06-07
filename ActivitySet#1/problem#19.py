import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#https://web.whatsapp.com/
url=input('Enter:- ')
html = urlopen(url, context=ctx).read()
searches= BeautifulSoup(html, "html.parser")

tags=seaarch('a')
for tag in test:
    print('TAG: ',tag)
    if tag == span:
        print('url:',tag.get('span',None)+1)