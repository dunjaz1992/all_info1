'''Comprehension'''

# генерация последовательности в одну строку используя цикл (синтактический сахар)
# list, set, dict

'''Синтаксис'''

# result for element in iterable_object
# result for element in iterbale_object if filter

'''==== list comprehension===='''

# упрощенный подход к созданию списка,задействует цикл for и if-else 

# list_= []
# for i in range(11):
#     list_.append(i)
# print(list_)

# a = list((i for i in range(11)))
# print(a)

# list_ = [i for i in range(11)]
# print(list_)

# import time
# start_time = time.time()

# list_ = []
# for i in range(100):
#     list_.append(i)

# time1 = time.time() - start_time
# start_time = time.time()
# list_2 = [ i for i in range(1000)] 
# time2 = time.time() - start_time
# print(time1, time2)


# list_ = []
# for i in range(11):
#     if i % 2 == 0:
#         list_.append(i)
# print(list_)    
# list_2 = [i for i in range(11) if i % 2 == 0]

# list_= ['hello' for i in range(10)] 10 раз hello
# print(list_)
# print([input() for i in range(10)])
# на каждой итерации запрашивает ввод (input)

''' если в условии нужен else  то все условия пишется перед for'''

# list_ = [f'{i} нечетное' if i % 2 else f'{i}четное' for i in range(100)]
# print(list_)
# list_2 = [i for i in range(11) if not i % 2, ]

# list1 = [1, 'hello', 3, 'a', 4.0, 6, 8, 'hw']
# list_ = [f'{i} нечетное' if i % 2 else f'{i} четное' for i in list1 if type(i) == int or type(i) == float]
# print(list_)

'''set comprehension'''

# почти тоже самое что представление списков. Используютс {} скобки, не содержит дубликатов, не гарантируют сохранность элементов в порядке.
# list_ = [1, 2, 3, 4, 5, 6]
# set_ = {i for i in list_}
# print(list_)a

'''dict comprehension'''
# необходимо доп-но определить ключ
# dict_ = {i: i**2 for i in range(10)}
# print(dict_)

# dict_ = {}
# for i in range(10):
#     dict_.update({i: i ** 2})
# print(dict_)

# d = {'a': 2, 'b':3}
# a = {k: 'четное'if v % 2 == 0 else 'нечетное' for k, v in d.items()}
# print(a)

# a = {i: str(i) for i in range(1, 11)}
# print(a)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# a = {list1[i]: list2[i] for i in range(len(list2))}
# print(a)


'''вложенные comprehension'''

# dict_ = {i: list(range(1, i+1)) for i in range(1, 6)}
# print(dict_)

# dict_ = {i: [j for j in range(1, i+1)] for i in range(1, 6)}
# print(dict_)

# # list1 = [i: [j for j in range('hello world')] for i in range(10)]
# print([['hello wolrd' for i in range(5)] for j in range(10)])

# employees = {
#     'id1': {
#         'first name': 'Александр',
#         'last name' : 'Иванов',
#         'age': 30,
#         'job':'программист'
#             },
#     'id2': {
#         'first name': 'Ольга',
#         'last name' : 'Петрова',
#         'age': 35,
#         'job':'ML-engineer'
#     }}

# for info in employees.values():
#     for k, v in info.items():
#         if k == 'age':
#                 info[k] = float(v)
# print(employees)

# print({id_: {k: (float(v) if k == 'age' else v) for k, v in info.items()} for id_, info in employees.items()})
# {k: f(loat(v) if k = 'age' else v) for k, v in info.items()}

