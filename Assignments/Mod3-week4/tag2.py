import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
count = input('Enter count: ')
position = input('Enter position: ')

# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# tags = soup('a')
# tag = tags[2]
# link = tag.get('href',None)
# print(link)

n = int(count)
while n > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[int(position) - 1]
    url = tag.get('href', None)
    print(n)
    print(url)
    n = n - 1
print("Blastoff!")  

# Retrieve all of the anchor tags

