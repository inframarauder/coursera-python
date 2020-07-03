from urllib.request import urlopen
from xml.etree import ElementTree as ET
import ssl

# ignore ssl errors:
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url:')
xml = urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)
counts = tree.findall('.//count')

total = 0
for count in counts:
    total = total + int(count.text)

print(total)
