# from views import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin
# import json

# class Product(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
#     def save(self):
#         with open('data.json', 'w') as file:
#             json.dump(self.objects, file, indent = 4)
#         return 'Saved!'
    

# class Comments(CreateMixin,ReadMixin,DeleteMixin):
#     pass


# smartphones = Product()
# print(smartphones.post(title = 'Redmi Note 10', description = 'The best phone for own price!', qty = 10, price = 250))
# print(smartphones.post(title = 'Redmi Note 20', description = 'Flagman of redmi phones!', qty = 5, price = 500))
# print(smartphones.post(title = 'Iphone 14 Pro Max', description = 'New cool and super phones!', qty = 5, price = 1300))
# print(smartphones.post(title = 'Sumsung S22 Ultra', description = 'The best phone for android lovers!', qty = 3, price = 1000))
# print(smartphones.post(title = 'IPHONE 13 PRO MAX', description = 'The best phone!', qty = 15, price = 1000))
# print()
# print()
# print(smartphones.list())
# print()
# print(smartphones.detail(4))
# print(smartphones.detail(15))
# print()
# print(smartphones.patch(1, title = 'Redmi Note 9'))
# print()
# print(smartphones.list())
# print()
# print(smartphones.delete(-1))
# print(smartphones.delete(1))
# print(smartphones.save())