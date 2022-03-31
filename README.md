# SaveYourJobs
An automation script for job parsing where you don't need to click the web page to see what is available.

How it works: Run main.py and just add up the URL. Based on what the job portal is, the script will give an output of job, company and location.
In future I plan to add more scripts for more job portals and offer an Excel creation.

So far: Added LinkedIn Search, LinkedIn Specific Posting and Indeed Specific Posting parsing options.

Update 26.03.2022: LinkedIn Search now gives links

Update 27.03.2022: linkedinsearchengine.py added. This script helps you search jobs in LinkedIn. For now there are only 3 parameters (Query, Location, Job Type) but more will be added.

Update 29.03.2022: Added work type option

Update 31.03.2022: Now jobs and links are stored as objects, instead of being printed. This is an important step while this script is converted to an UI-friendly HTML page.
