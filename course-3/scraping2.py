from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input('Enter count:'))
pos = int(input('Enter position:'))

i = 1
while i <= count:
    a_tags = soup.find_all('a')
    link = a_tags[pos-1].get('href', None)
    print(link)
    html = urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    i = i+1
