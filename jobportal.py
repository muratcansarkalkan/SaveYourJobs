class Indeed():

    def parser(soup):
        # Finds job title
        job_title = soup.find_all(class_="icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title")
        for job in job_title:
            print(job.text)
        
        company_title = soup.find_all(class_="icl-u-lg-mr--sm icl-u-xs-mr--xs")
        for company in company_title:
            print(company.text)

class Linkedin():

    def parser(soup):
        # Finds job title
        job_title = soup.find_all('h1', class_="top-card-layout__title topcard__title")

        for job in job_title:
            # Gives str
            job = job.text

        # Finds company
        company_title = soup.find_all('a', class_="topcard__org-name-link topcard__flavor--black-link")

        for company in company_title:
            # Gives str
            company = company.text.lstrip().rstrip()

        # Finds country
        country_title = soup.find_all('span', class_="sub-nav-cta__meta-text")

        for country in country_title:
            # Splits the location from "Istanbul, Turkey" to a list
            location = country.text.split(", ")
            # Gives str
            location = location[-1]
            
        print(company, job, location)
