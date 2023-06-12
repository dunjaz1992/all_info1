from bs4 import BeautifulSoup
import requests
import csv

'''получает html разметку опрделенного сайта по url'''
def get_html(url: str) ->str:

    response = requests.get(url)
    return response.text
def get_soup(html: str)-> BeautifulSoup:
    '''Получает  html разметку и структурирует ее в bs '''
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_last_page(soup: BeautifulSoup) -> int:
    '''Функция которая возвращает последнюю страницу на сайте'''
    pages = soup.find('ul', class_='pagination').find_all('a', class_='page-link')
    last_page = pages[-1].get('data-page')
    return int(last_page)

def get_data(soup: BeautifulSoup) -> list:
    '''Функция парсер, получает нужные данные с сайта и возвращает в виде списка'''
    container = soup.find('div', class_='table-view-list')
    cars = container.find_all('div', class_='list-item')
    result = []
    for car in cars:
        name = car.find('h2', class_='name').text.strip()
        try:
            img = car.find('img', class_='lazy-image').get('data-src')
        except:
            img = 'No image!'
        price_div = car.find('div', class_='block price')
        price= price_div.find('p',).find('strong').text
        # desc1 = car.find('p', class_='year-miles').text.strip()
        # desc2 = car.find('p', class_='body-type').text.strip()
        # desc3 = car.find('p', class_='volume').text.strip()
        # description = f'{desc1} {desc2} {desc3}'
        ls = ['year-miles', 'body-type' ,'volume']
        desc = ','.join(car.find('p', class_=x).text.strip() for x in ls)
        data = {
            'name': name, 'desc': desc, 'price': price, 'img': img
        }
        result.append(data)
    return result
def prepare_csv() -> None:
    '''Функция которая подготавливает csv файл'''
    with open('cars.csv', 'w') as file:
        fieldnames = ['№', 'name', 'price', 'description', 'image URL']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
        '№': '№',
        'name': 'name',
        'price': 'price',
        'description': 'description',
        'image URL': 'image URL' 
        })

count = 1

def write_to_csv(data: dict) -> None:
    '''Записывает все данные в  csv файл'''
    with open('cars.csv', 'a') as file:
        fieldnames = ['№', 'name', 'description', 'price', 'image URL']
        writer = csv.DictWriter(file, fieldnames)
        global count
        for car in data:
            writer.writerow({
            '№': count,
            'name': car ['name'],
            'description': car ['desc'],
            'price': car ['price'],
            'image URL': car ['img']
            })
            count += 1

def main():  
    i = 1
    prepare_csv()

    while True:
        url = f'https://www.mashina.kg/search/all/?page={i}'
        html = (get_html(url))
        soup = get_soup(html)
        # print(get_data(soup))
        last_page = get_last_page(soup)
        data = get_data(soup)
        write_to_csv(data)
        print(f'Спарсили {i}/{last_page} страницу!')
        if i == 15:
            break
        i+=1
main()


