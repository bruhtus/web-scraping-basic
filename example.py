import requests
from bs4 import BeautifulSoup

url = 'https://www.its.ac.id/matematika/en/lecturer-and-staff/list-of-lecturers/'

req = requests.get(url)
print(req.status_code)
#print(req.content)

soup = BeautifulSoup(req.content, 'html.parser')
print(f'soup.title.get_text()\n')
#print(soup.h3)
#print(soup.body)

lecturers_name = soup.find_all('h3', {'class':'vc_custom_heading'})

for name in lecturers_name:
    print(name.text, '\n') #to print all the bastard's name
