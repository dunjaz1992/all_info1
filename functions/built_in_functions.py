''' встроенные функции'''
# print()
# len()
# input()
# divmod()
# id()
# range()

'''lambda''' # анониманая фунцкия (та же самая функция, только без имени)



# def func(a, b,): return a + b
# print(func(3, 5))
# lambda параметры: что функция должна возвращать 

# a = lambda a, b: a + b
# print(a(4, 6))

# x = lambda a, b, c: (a * b)%c
# print(x(2, 66, 7))

# x = lambda a, b, c: (a, b, c)
# print(x(2, 66, 7))

# get_keys = lambda dict_: dict_.keys()
# dct = {1: 'hello', 'a': 7, 'n': 9}
# print(get_keys(dct) )



# a = lambda list_: list_[-1]
# print(a([1, 2, 3, 4]))

# pow_ = lambda x: x ** 2
# print(pow_(9))
# map(func, iterables) -> она применяет funс к каждому эдементу итерируемого объекта

# map_ = map(int, ['1', '1', '2'])
# print(list(map_))

# a = range(10)
# print(list(a))
# int('1') -> 1
# int('2') -> 2
# int('3') -> 3

# list_ = [1, 2,3]

#  for i in list_:
#      int(i)

# def f(number):
#     return number ** 2
# a = map(f, list_)
# print(list(a))

# list_ = [1, -3, 100, -44]
# list_2 = list(map(lambda x: x < 0, list_))
# print(list_2)

# func = lambda num: num + 1
# res = []
# list_ = [1, 2, 3, 4, 5, 6]
# for i in list_:
#     res.append(func(i))
# print(res)

# filter(func, iterable) -> возвращает генератор из элементов итерируемого объекта, которые прошли фильр (проверку) 
# фильтрует если функция возвращает  True
# def filter_nums(number):
#     if number % 2 == 0:
#         return True
# res = list(filter(filter_nums, [1, 2, 3, 4, 5, 6]))
# print(res)



# res = list(filter(lambda number: number % 2 == 0, [1, 2, 3, 4, 5, 6, 8]))
# print(res)

# list_ = ['Эртай', 'Тима', 'Айкол', 'Нуркамила', 'Айбек']


# def startswith_vowel(name):
#     vowels = 'АЕЭУОИЯЮЕ'

#     return name.upper().startswith(tuple(vowels))

# res = list(filter(startswith_vowel, list_))
# print(res)

# reduce(func, iterable) -> нужно импортировать из библиотеки functools, возвращает один результат
from functools import reduce 
# (sum(), min(), max())
# reduce 
# list_ = [1, 2, 3, 4, 5, 6]
# res = reduce(lambda x, y: x + y, list_)

# print(res)



#print(min(list_))
# min_ = reduce(lambda small, x: small if (small < x) else x, list_)
# print(min_)
# def mul(num1, num2):
#     return num1 * num2

# list_ = [1, 2, 3, 4, 78, 6, 100, 5]
# res = list_[0]

# for i in list_[1:]:
#     res = mul(res, i)
# print(res)



'''enumerate(iterable, [start - число, по деволту 0])''' #-> генератор , где каждый элемент - tuple состоящий из числа и элемента
# нумерует элементы
# list_ = ['a', 'b', 'c', 'd']
# for i in enumerate(list_, 10):
#     print(i)

# (0, 'a')
# for a, b in enumerate(list_):
#     print('index - ', a, 'element- ', b )
# for i in enumerate(list_[1:]):
#     print(i)

'''zip(iterbale , iterbale -> *iterable) -> соединяет последовательности''' 
# list_ = [1, 2, 3, 4, 5, 6]
# list_2 = ['a', 'b', 'c', 'd', 'e', 'f']
#print(list(zip(list_,list_2)))
# print(dict(zip(list_,list_2)))


# list_ = [1, 2, 3, 4, 5, 6]
# list_2 = ['a', 'b', 'c']
# print(list(zip(list_, list_2)))


# lt = [1, 2, 3, 4, 5, 6]
# lt2 = [0, 0, 0, 0, 0, 0]
# lt3 = ['a', 'b', 'c', 'd']
# lt4 = [(1, 2), (3, 4)]
# print(list(zip(lt, lt2, lt3, lt4)))

'''изменить тип данных( задание)'''

# dict_ = {1:2, 2: 3, 3: 4, 4: 5}
# res = list(map(str, dict_.values()))
# dict_2 = dict(zip(dict_.keys(), res))
# print(dict_2)

'''при помощи map() изменить список (четное/неетное)'''




# list_ = [1, 2, 3, 4, 5, 6]
# def str_num(number):
#     if number % 2 == 0:
#         return 'четное'
#     else:
#         return 'нечетное'
    
# result = list(map(str_num, list_))
# print(result)

# 2 variant

# a = lambda number: 'четное' if number % 2 == 0 else 'нечетное'
# print(list(map(a, list_)))

# a = input('введите ')
# l = a.split()
# a, b = map(int, l)
# print(a, b)

'''new mentor'''

'''анонимная функция - lambda (обычная функция с одной особенностью, у нее нет имени) Принимает сколкьо угодно параметров, но всегда возвращает одно выражение
'''

# def hello():
#     return 'hello'
# print(hello())

# x = lambda: 'hello'
# print(x())


# x = lambda a, b, c: (a * b) % c
# print(x(5,5,5))

# x = (1, 2)
# x = lambda num1, num2, degree=None: (num1 * num2) ** degree if degree else num1 * num2
# print(x(2, 2, 3))
# print(x(5, 5))

# dict_ = {
#     'john': 500,
#     'tirion': 160_000,
#     'tom': 150,
#     'sanzhar': 20,
#     'ayana': 100_00,
# }
# print(dict_.items())
# new_dict = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
# print(new_dict)


'''map (function iterable) - принимает к каждому элементу внутри iterable функцию, которую мы ей передаем в function, закидывая в результат те данные, которые возвращает функция. В результате мы получаем mapobject (iterable) , в котором храгятся все наши данные.'''

# names = ['john', 'aria', 'baku', 'bakberdi', 'lilo']
# new_list = list(map(lambda x: f'hello, mr/mrs {x}', names))
# print(new_list)

# ls = ['str1', 'str2', 'str3']
# new_list = tuple(enumerate(ls))
# print(new_list)


