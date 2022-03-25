from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# HTML request to open URL
url = input("Enter job url")
html = urllib.request.urlopen(url, context=ctx).read()

# lxml is the parser BeautifulSoup uses better use that way
soup = BeautifulSoup(html,'lxml')

# Printed contents of LinkedIn page
contents = open(f'indeed.txt', 'w', encoding="utf-8")
    
contents.write(str(soup.prettify()))