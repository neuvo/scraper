import requests
import time
import os
from bs4 import BeautifulSoup
import logging
from requests.adapters import HTTPAdapter, Retry

inputted_dirname = input('Please enter the destination for the monster images: ')
if '/' in inputted_dirname and inputted_dirname[-1] != '/':
    inputted_dirname = inputted_dirname + '/'
elif '\\' in inputted_dirname and inputted_dirname[-1] != '\\':
    inputted_dirname = inputted_dirname + '\\'

destination = os.path.dirname(inputted_dirname)
start = input('Enter the ID of the first monster you wish to scrape (default: 1)')
if start is None or start == '':
    start = '1'

start = int(start)

if not os.path.exists(destination):
    print('Given path does not exist, creating...')
    os.makedirs(destination)
    print('Created ' + destination)

logging.basicConfig(level=logging.ERROR)

# source: @datashaman on https://stackoverflow.com/questions/23267409/how-to-implement-retry-mechanism-into-python-requests-library
s = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
s.mount('http://', HTTPAdapter(max_retries=retries))
count = 1
while True:
    print(f'grabbing monster {count}...')
    time.sleep(.5)
    monster_url = 'https://2e.aonprd.com/Monsters.aspx?ID=' + str(count)
    try:
        monster_req = s.get(monster_url)
        monster_soup = BeautifulSoup(monster_req.content, 'html.parser')
        img_element = monster_soup.find(name='img', attrs={'class': 'thumbnail'})
        if img_element is not None:
            monster_name = img_element['src'].split('\\')[-1]
            img_url = r'https://2e.aonprd.com/' + img_element.attrs['src']
            with open(os.path.join(destination, monster_name), 'wb') as f:
                f.write(requests.get(img_url).content)
    except Exception as e:
        print("error handling " + monster_url + ': ' + str(e))
        break
    print(f'Grabbed monster {count}')
    count += 1

