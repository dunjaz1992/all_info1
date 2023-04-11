''' Списки, Методы списков. Цикл for. Кортеж'''

# список - изменяемый, индексируемый, упорядоченный, интерируемый. 
# [] -> литерылы (выражения, которыйе создабт объекты определенного типа данных)

# list_ = [1, 2, 3, 'hello', [1, 2, 3,], {1:'a'}]
# print(list_[0])
# print(list_[4][0])
# print(list_[5][1])

# names = input('Введите имена через пробел: ').lower().split()
# guest = input('Введите имена через пробел: ').lower()
# if guest in names:
    # print('Welcom')
# else:
    # print('Иди спать')


''' Создание списков '''
# 1. list(interable)
# a = 'hello'
# print(list(a))
#   range() -> возвращает последовательность элементов
# print(list(range(1, 10,)))

# 2. [] -> литералы
# list_ = []
# print(type(list_))
# list_ = [1] * 6
# print(list_)

# range([start], stop, [step]) -> возвращает послед-ть чисел, по уполчанию начинает с 0, последовательность каждый раз увеличивается на 1 и останавливается перед заданным числом (stop) 


''' Методы списков '''

# del -> удаление элементов
# list_ = [1, 2, 3]
# del list_[0]
# print(list_)


# .append() -> добавление элемента в конце списка
# list_ = [1, 2, 3]
# print(id(list_))
# list_.append('hello')
# print(list_)
# print(id(list_))


# .extend(element[interable]) -> расширяет список добавляя в конец все элементы списка
# list_ = [1, 2, 3]
# list_.extend('hello')
# list_.append([1, 2, 3])
# print(list_)


# .insert(index, element) -> добавляет элемент по индексу
# 
# list_ = [1, 2, 3]
# list_.insert(0, 9)
# print(list_)


# .index(element, [start], [end]) -> возвращает индекс элемента
# list_ = [1, 2, 3, 4, 5, 6, 7, 2 ,3, 4, 5, 1]
# print(list_.index(1, 4))


# .clear() -> очищает список полностью
# list_ = [1, 2, 3]
# list_.clear()
# print(list_)

# .count(element) -> считает кол-во вхождений element в списке
# list_ = [1, 2, 3, 3, 4, 3, 4, 3]
# print(list_.count(3))
    #print(len(list_)) # считает кол-во элементов в списке или длина списка


#.pop(index) -> удаляет и возвращает элемент по index, если индекс не указан, то удалит с конца
# list_ = [1, 2, 3]
# list_.pop()
# print(list_)

# list_ = [1, 2, 3]
# a = list_.pop(0)
# print(list_, a)


# .remove(elenet) -> удаляет первый элемент в списке
# list_ = [1, 2, 3]
# list_.remove(2)
# print(list_)


# .reverse() -> переворачивает список
# [::-1]
# list_ = [1, 2, 3]
# (list_.reverse())
# print(list_)


# # .sort() -> сортирует список (reverts=True -> в обратном порядке)
# list_ = [1, 2, 3, 4, 5, 2, 3, 2, 1, 2]
# list_.sort()
# print(list_)


# .copy() -> поверхностное копирпование
# new_list = list_.copy()
# print(new_list)


''' Цикл for '''
# цикл - это блок кода, который повторяется несколько раз

# for -> работает с интерируемыми объектами, заканчивается когда даходит до конца
# list_ = [1, 2, 3, 4, 5] ('hello')
# print(list_[0])
# for element in list_:
#     print(element) (element+1)


''' Tuple (Кортеж) '''
# tuple_ = (1, 2, 3)
# print(tuple('hello'))

# tuple_ = 1,
# print(type(tuple_))


''' Методы tuple '''

# .count(element) ->
# tuple_ = (1, 2, 3, 4, 1, 2, 1, 1, 1)
# print(tuple_.count(1))


# .index(element) -> врзвращает index element
# print(tuple_.index(2))

