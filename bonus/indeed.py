class Indeed():

    def parser(soup):
        # Finds job title
        job_title = soup.find_all(class_="icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title")
        for job in job_title:
            print(job.text)
        
        company_title = soup.find_all(class_="icl-u-lg-mr--sm icl-u-xs-mr--xs")
        for company in company_title:
            print(company.text)

        
