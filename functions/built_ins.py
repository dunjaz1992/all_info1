# zip (iterables) - она соединяет каждый элемент итерируемых обьектов между собой в тип данных tuple и возвращает итератор 

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]
# res = dict(zip(ls1, ls2))
# print(res)

# ls1 = [1, 2, 3, 4, 5]
# ls2 = [100, 200, 300, 400, 500, 600]
# ls3 = [10, 20, 30]
# res = list(zip(ls1, ls2, ls3))
# print(res)

# zip для создания словарей

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']
# data = {
#     'okt': ['bishkek_okt', 'Gorkogo 212', 'Vefa', 'Cisco', '10.555.0.12'],
#     '1may': ['bishkek_1may', 'Jibek-jolu', 'Belyi', 'Cisco', '10.666.0.12'],
#     'svrd': ['bishkek_svrd', 'Ahunbaeva 212', 'TC', 'Cisco', '10.777.0.12']
# }
# bishkek_data = {}
# for k in data:
#     bishkek_data[k] = dict(zip(d_keys, data[k]))
# print(bishkek_data)

#-----------------
# all(), any()
# all(iterable) -возвращает True, если все элементы итерируемого обьекта итина, иначе  False

# ls = [5, 6, 7, []]
# ip = '10.255.0.155' -> True
# ip1 = '10.255.0y.155' -> False

# result = all(x.isdigit() for x in ip1.split)('.')
# print(result)


# any - возвращает True, если хотя бы один элемент   итина

# ls = [1, 2,s))

# ignore = ['rm-rf', 'sudo', 'reset', 'poweroff']
# command = input('Vvedite komande: ')
# if any (x in command for x in ignore):
#     raise Exception('Block you!')
# print('OK!')


#------------------------------------------

# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# symblos = '_()=-@!#%'
# q_pass = int(input('Vvedite kol-vo paroley:'))

# result = {
#     f(choices(ascii_letters, k=15), choices(digits, k=6), choices(symblos, k=2))
#   for f in repeat(lambda x, y, z: ''.join(set(x+y+z)), q_pass)
  
# }

# print(result)
# print(f'Quantity of password: {len(result)}')
# from statistics import mean
# print(f'avarage len of password: {mean(len(x) for x in result)}')


# def func(a, b):
#   return a + b
#   print(5, 5)