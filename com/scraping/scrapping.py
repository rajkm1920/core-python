import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find(id="ResultsContainer")
# print(result.prettify())
job_elems = result.find_all('section', class_='card-content')

# for job_elem in job_elems:
    # print(job_elem, end='\n'*1)

# for job_elem in job_elems:
#     # Each job_elem is a new BeautifulSoup object.
#     # You can use the same methods on it as you did before.
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     print(title_elem)
#     print(company_elem)
#     print(location_elem)
#     print()

# for job_elem in job_elems:
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     # print(type(title_elem))
#     if None in (title_elem,company_elem,location_elem):
#         continue
#     print("Title : {}, company : {}, Location : {}, ".format(title_elem.text.strip(), company_elem.text.strip(), location_elem.text.strip()))

# python_jobs = job_elems.find_all('h2', string='Python')
# print(python_jobs)

