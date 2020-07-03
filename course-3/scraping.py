from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def print_sum(soup):
    cols = soup.find_all(attrs={"class": "comments"})
    col_sum = 0
    for col in cols:
        col_sum += int(col.text)
    print(col_sum)


url = input('Enter url:')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print_sum(soup)
