from models import Products, Category

def get_all_categories():
    return Category.select(Category.id, Category.title)


def get_all_products():
    return Products.select()


# categories = get_all_categories()
# print(categories)
# print(f'Все атегории в БД')
# for category in categories:
#     print(f'ID: {category.id} Title: {category.title}')

# products = get_all_products()
# print('Все продукты в БД')
# for x in products:
#     print(f'ID: {x.id}, Title: {x.title}, Price: {x.price}, Category: {x.category_id}')


category_computes = Category.get(Category.title=='airpods')
print(category_computes, category_computes.title)

for x in category_computes.products:
    print(f'ID: {x.id}, Title: {x.title}, Price: {x.price}, Category: {x.category_id.title}')


