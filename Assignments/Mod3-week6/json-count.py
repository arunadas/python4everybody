import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) == 0 : break

    connection = urllib.request.urlopen(url, context=ctx)

    data = connection.read().decode()
    js = json.loads(data)
    sum = 0
    for u in js['comments']:
        sum += u['count']
    print("sum : ", sum)