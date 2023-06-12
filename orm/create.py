import peewee
from models import Category, Products
import random

def add_category(name):
    try:
        obj = Category(title=name.lower().strip())
        obj.save()
        print(f'Сохранили категорию {obj} - {obj.title}')
    except(peewee.IntegrityError, peewee.InternalError):
        print(f'{name.lower().strip()} - это категория уже существует')
# add_category('smartphones')
# add_category('   computes  ')
# add_category('Tablets')
# add_category('Airpods')
# add_category('Sony Playstion')
# add_category('Notebook  ')

def add_product(name, price, category_name):
    category_name = category_name.lower().strip()
    try:
        category = Category.get(title=category_name)
        print(category, category.title, category.created_at)
    except peewee.DoesNotExist:  
        print(f'Категории {category_name} не существует!')
    else:
        obj = Products(title=name, price=price, category_id=category)
        obj.save()
        print(f'Сохранили товар {obj} - {obj.title}')

add_product('Iphone 11',960,'notebook')
add_product('Iphone 12',1000,'smartphones')
add_product('HP',500,'airpods')
add_product('MAC',1230,'Sony Playstion')
add_product('Ipad',800,'tablets')


#--------------
# добавление новых данных

# add_category('cars')
# with open('files/cars.txt', 'r') as file:
#     ls = file.readlines()
#     print(ls)
#     for x in ls:
#         name = x.strip()
#         price = random.randint(5000, 20000)
#         add_product(name, price, 'cars')

# add_category('cars')
# with open('files/telefon.txt', 'r') as file:
#     ls = file.readlines()
#     print(ls)
#     for x in ls:
#         name = x.strip()
#         price = random.randint(200, 1200)
#         add_product(name, price, 'smartphones')