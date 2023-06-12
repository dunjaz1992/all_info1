from models import Products, Category


# query = Products.update(price=1_000_000).where(Products.id==4)
# print(query, '!!!!!')
# query.execute()

# query = Products.update(title='Hanamana').where(Products.id==4)
# print(query, '!!!!!')
# query.execute()



# Удаление данных

# product = Products.get(Products.id==4)
# print(product, product.id)
# product.delete_instance()
# print(product)

query = Category.delete().where(Category.id==2)
query.execute()