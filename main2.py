from bs4 import BeautifulSoup
import requests
import time

print('put some skill you are not familer with')
unfamilier_skill = input('>')
print(f'filtering out {unfamilier_skill}')
print('')
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in  enumerate(jobs):
        job_published_date = job.find('span', class_ = 'sim-posted').span.text
        
        if 'few' in job_published_date:
            company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ','').capitalize()
            skills = job.find('span', class_= 'srp-skills').text.replace(' ','').capitalize()
            more_info = job.header.h2.a['href'].capitalize()
            if unfamilier_skill not in skills:
            # print(skills)

            # print(company_name)


            # print(job_published_date)
            # print(f'''
            #     company name: {company_name}
            #     required skills: {skills}
            #     ''')
                with open(f'posts/{index}.txt', 'w') as f:
                    
                    f.write(f'company name : {company_name.strip()}\n')
                    f.write(f'required skills: {skills.strip()}\n')
                    f.write(f'more info: {more_info}\n')
                print(f'file saved: {index}')    

if __name__ =='__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minitutes...')
        time.sleep(time_wait*60)
        