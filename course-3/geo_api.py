from urllib.request import urlopen
from urllib.parse import urlencode, urlparse
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/json'
address = input('Enter address:')
params = urlencode({'key': 42, 'address': address})

data = urlopen(url+'?'+params).read()
parsed_json = json.loads(data)

print(parsed_json['results'][0]['place_id'])
