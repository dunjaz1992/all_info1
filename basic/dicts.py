''' =======  Тип данных словари dict()  ======='''

#{key: value}
# позволяет нам хранить любые обьекты, для доступа к которым используется ключ(key)

# изменяемый, итерируемый, неиндексируемый, упорядоченный тип данных


# {} -> литералы
# dict_ = {}
# print(type(dict_))

# dict_ = {'a': 'hello', 'b': 'world', 'c': 3}
# print(dict_['c'])

# ключи должны быть неизменяемым типом данных
# ключи должны быть уникальны
# значениями словаря могут быть любые типы данных

# dict_ = {1: {'a': 'one'}, 'hello': [1, 2, 3]}

# dict_ = {'a': 1, 'a': 2, 'a' 3}


''' === Создание словарей ==='''

# 1. {key: value}

# 2. dict()
# print(dict('hello'))  # Error
# print(dict([('key1', 'value1'), ('key2', 'value2')]))

# print(dict(['ad', 'bc', 'lk']))

# key1, value1 = 'ad'
# print(key1, value1)

# print(dict(a='hello', b = 'world'))

''' =====  Методы словарей  ====='''
 # .clear() --> очищает словарь --> {} пустой обьект
 
# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# dict_.clear()
# print(dict_)

# .copy() --> возвращает копию словаря
# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# dict_2 = dict_.copy()

# dict_2['hobby'] [0] = 'hi'
# print(dict_, dict_2)

# deepcopy
# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# from copy import deepcopy
# dict_2 = deepcopy(dict_)

# dict_2['hobby'] [0] = 'hi'
# print(dict_, dict_2)

# . fromkeys(seq, [value]) --> создает словарь с ключами из seq и значением value(value для все одинаковый, по умолчанию None)

# list_ = ['name', 'age', 'hobby']
# # dict_ = dict.fromkeys(list_)
# dict_ = dict.fromkeys(list_, 'a')
# print(dict_)

''' === Получение элементов из словаря ==='''

# 1. .get(key: [value]) --> возвращает значение по ключу key, а если такого ключа нет, не бросает ошибку(исключение), а возвращает value или None
# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# print(dict_.get('name2', 'not such key'))

# Изменение элементов словаря

# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# dict_['name'] = ['Sam'] #изменение значения
# dict_['address'] = 'Kievskaya25' # создание новой пары
# dict_['hobby'].append('run')
# print(dict_)


# .update(new_dict) --> добавляет новый словарь в наш словарь

# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# new_dict = {'address': 'Kievskaya 23'}
# dict_.update(new_dict)
# print(dict_)

# .setdefault(key, [default value]) --> работает точно так же как метод .get(), но если нет такого ключа он создаст новую пару key: defualt value

# 1. 
# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# print(dict_.setdefault('name', 'Sam'))

# 2. 
# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# print(dict_.setdefault('address', '34'))
# print(dict_)

# .keys() --> выводит все ключи в словаре

# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# print(dict_.keys())

# .values --> выводит все значения

# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# print(dict_.values())

# .items --> выводит и ключ и значение(пары) из словаря

# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# print(dict_.items())

# Удаление элемента в словаре
# .pop(key, [message]) --> удаляет пару ключ и значение, и возвращает значение. Если ключа нет возвращает message(по умолчанию бросает ошибку(исключение))

# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# print(dict_.pop('name'))
# print(dict_)

# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# print(dict_.pop('name2', 'Nooooo'))
# print(dict_)

# .popitem() --> удаляет и возвращает пару ключ значение, удаляет последнее добавленное

# dict_ = {'name' : 'John', 'age' : 25, 'hobby' : ['footbal', 'poker', 'sing']}
# print(dict_.popitem())
# print(dict_)



