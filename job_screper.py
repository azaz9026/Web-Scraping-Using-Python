# fetch the HTML contact of the webpage : requests
import requests
from bs4 import BeautifulSoup
import time


known_skills = input('Porovide your  familiar skills :- ')

known_skills = known_skills.split(',')

def scrap_jobs():

    #fetch the HTML contact of the webpage : requests

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Data+Science%22&txtKeywords=%22Data+Science%22&txtLocation=').text

    # print(html_text)


    # scrape the data  to fetch  the results : BeautifulSoup

    soup = BeautifulSoup(html_text, 'lxml')
    # print(soup)



    jobs  = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        skills = job.find('span', class_='srp-skills').text.replace(' ', '').strip().split(',')
        date_posted = job.find('span', class_='sim-posted').text.strip() 

        if 'few' in data_posted and set(known_skills) & set(skills):
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','').strip()
            jd = job.hesder.h2.a['href']
            print(f'''
            company name : {company_name}
            skills : {skills}
            date posted : {date_posted}
            jd : {jd}
            ''')
            print('##############################################################')
        
  

if __name__ == '__main__':
    scrap_jobs()
    print("waiting for 5 seconds")
    time.sleep(5)