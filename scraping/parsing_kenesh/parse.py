import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Pool

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_1page_links(soup):
    links = []
    container = soup.find('div', class_='grid-deputs')
    items = container.find_all('div', class_='dep-item')
    for item in items:
        a = item.find('a').get('href')
        link = 'http://kenesh.kg' + a 
        links.append(link)
    return links

# url = 'http://kenesh.kg/ru/deputy/list/35?page=1'
# html = get_html(url)
# soup = get_soup(html)
# print(get_1page_links(soup))




def get_all_links():
    res = []
    for i in range(1, 6):
        url = f'http://kenesh.kg/ru/deputy/list/35?page={i}'
        html = get_html(url)
        soup = get_soup(html)
        page_links = get_1page_links(soup)
        res.extend(page_links)
    return res
# links = get_all_links()

# print(links, len(links))



def get_deps_data(link):
    html = get_html(link)
    soup = get_soup(html)
    name = soup.find('div', class_='deput-name').text
    info = ' '.join(soup.find('div', class_='deput-info').text.strip().split())
    bio = soup.find('div', class_='tab-content').text.strip()
    img = 'http://kenesh.kg' + soup.find('div', class_='deput-image').find('img').get('src').replace(' ', '%20')
    data = {'FIO': name, 'Info': info, 'Bio': bio, 'Image': img, 'Link to page': link}
    return data

    


def prepare_csv():
    with open('deputy.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['FIO', 'Info', 'Bio', 'Image', 'Link to page'])
def writer_to_csv(data):
    with open('deputy.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow([data['FIO'], data['Info'], data['Bio'], data['Image'], data['Link to page']])
        print(f'{data["FIO"]} - parsed!')
def make_all(link):
        data = get_deps_data(link)
        writer_to_csv(data)
def main():
    prepare_csv()
    links = get_all_links()
    # for link in links: последовательно
    #     data = get_deps_data(link)
    #     writer_to_csv(data)

    # паралельно (многопоточно)
    with Pool(40) as pool:
        pool.map(make_all, links)
if name == 'main':
    start = datetime.now()
    main()
    finish = datetime.now()
    print(f'Parsing takes: {finish - start} times!')