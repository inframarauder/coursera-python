from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
data = urlopen(url, context=ctx).read()

parsed_json = json.loads(data)

total = 0
for comment in parsed_json['comments']:
    total = total+int(comment['count'])

print(total)
