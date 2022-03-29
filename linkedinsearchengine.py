import jobportal
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Base job searching link
link = "https://www.linkedin.com/jobs/search/"

print("Welcome to LinkedIn Job Search Engine")
# The query function
def query():
    # Define search filter and search settings
    searchfilter = []
    searchsettings = ""

    # Define query and convert to URL format
    query = input("Search by title, skill or company")
    query = urllib.parse.quote(query)

    # If query exists then filter is appended as keywords=query
    if len(query) > 0:
        searchfilter.append("keywords="+query)

    # Job type filter
    jobtypeoption = "f_JT="
    jobtypeselection = 0

    # Allows user to type job types until max types reached and adds up ",", if N is typed then next question
    while jobtypeselection < 6:
        jobtype = input("What kind of job do you look? (F)ullTime, (P)arttime, (C)ontract, (T)emporary, (I)nternship, (V)olunteer, (N)o specific")
        if jobtype == "N":
            break
        jobtypeoption += jobtype+","
        jobtypeselection += 1
    jobtypeoption = jobtypeoption.rstrip(",")

    # If jobtype option is chosen then it is appended to search filter
    if len(jobtypeoption) > 5:
        searchfilter.append(jobtypeoption)
    # Now asks if it is onsite, hybrid or remote

    worktypeoption = "f_WT="
    worktypeselection = 0

    while worktypeselection < 3:
        worktype = input("What kind of job do you look? (1)On-site, (2)Remote, (3)Hybrid, (N)o specific")
        if worktype == "N":
            break
        worktypeoption += worktype+","
        worktypeselection += 1
    worktypeoption = worktypeoption.rstrip(",")

    # If worktype option is chosen then it is appended to search filter
    if len(worktypeoption) > 5:
        searchfilter.append(worktypeoption)

    # Now asks for location again converts to URL format
    location = ""
    location = input("City, state or zipcode")
    location = urllib.parse.quote(location)

    # If it is typed then filter is appended as location=location eg. location=Paris, Île-de-France, France
    if len(location) > 0:
        searchfilter.append("location="+location)

    if len(searchfilter) == 1:
        searchsettings = searchsettings+searchfilter[0]
    else:
        for i in range(0, len(searchfilter)):
            searchsettings = searchsettings+searchfilter[i]+"&"

    searchsettings = searchsettings.rstrip("&")

    return searchsettings

searchfunc = query()

# F = full time P = part-time C = contract T = temporary I = internship if user puts anything else then no f_JT query

# f_JT=I Only internship
# f_JT=F,P full time and part-time

# If there is at least one option then 
if len(searchfunc) > 0:
    link = link+"?"+searchfunc

try:
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html,'lxml')
    jobportal.LinkedinSearch.parser(soup)

except:
    print("No matching jobs found.")
    
