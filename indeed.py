class Indeed():

    def parser(soup):
        # Finds job title
        job_title = soup.find_all(class_='jobTitle')

        print(job_title)
