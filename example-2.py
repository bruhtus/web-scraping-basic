import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.olx.co.id/items/q-mobil-bekas'

req = requests.get(url)
print(req.status_code)

soup = BeautifulSoup(req.text, 'html.parser')
names = soup.find_all('span', {'class':'_2tW1I'})
names_dict = {'names': []}
for name in names:
    names_dict['names'].append(name.text)

#print(names_dict)

with open('./names-used-car.json', 'a+') as f:
    json.dump(names_dict, f, ensure_ascii=False, indent=4)

print('Done')
