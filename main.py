from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re
from linkedin import Linkedin
from indeed import Indeed
from datetime import datetime

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("Welcome to LinkedIn Job Parser")
print("If you are done with parsing jobs, please type 'quit'")

# job = ""
# company = ""
# location = ""

# sample url = https://www.linkedin.com/jobs/view/2923884853

# HTML request to open URL
while True:
    url = input("Enter job url")

    if url == "quit":
        quit()

    html = urllib.request.urlopen(url, context=ctx).read()

    # lxml is the parser BeautifulSoup uses better use that way
    soup = BeautifulSoup(html,'lxml')

    if re.search("linkedin", url, re.I):
        Linkedin.parser(soup)

    elif re.search("indeed", url, re.I):
        Indeed.parser(soup)

        # Prints today's date
        date=datetime.today().strftime('%m/%d/%Y')

        print(date)
    else:
        print("It is not valid")