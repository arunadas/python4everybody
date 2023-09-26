from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.dr-chuck.com/'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
print("######")
print(tags)
print("######")

<a href="https://www.si.umich.edu/" target="_blank">School of Information</a>,
<a href="https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1159280" target="_blank">
<img alt="Rate This Professor" src="/images/rate-my-professor.jpg" width="140"/></a>

for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)