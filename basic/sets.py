''' ===== Множества set() ====='''

# изменяемый, неупорядоченный, неиндексируемый, итерируемый тип данных
# предназначен для хранения уникальных значений. Могут хранить в себе только неизменяемый тип данных, если используете tuple, то в них тоже должен храниться незменяемые типы данных

# set1 ={1, 2, 3, 3}
# print(set1)

# set2 = {(1, 2, 3), 1, 2, 3}
# print(set2)

# set3 = {1, True, 0, False, 0}
# print(set3) #{1, False}

''' Создание множеств '''
# 1. set()
# a = set([1, 2, 3, 4])
# print(a)

# a = set({'a': 1, 'b': 2})
# print(a)

# a = set('hello world')
# print(a)

# 2. {}

# set_ = {1, 2, 3, 'hello', (4, 5), None, True, False}
# print(set_)

''' ===== Методы множеств ====='''
'''добавление элементов'''

# .add(element)


# set_ = {1, 2, 3}
# # set_.add(4)
# set_.add('hello')
# set_.add((1, 2, 6))
# print(set_)

# .update(sequence) --> за раз может добавить несколько значений, не не повторяет имеющеися, передаем все итерируемые

# set_ = {1, 2, 3}
# set_.update('hello')
# set_.update([1, 2, 3, 4])
# set_.update({'a': 99, 'b': 97}, 'string')
# print(set_)

''' Методы для удаления элементов '''
# .clear() --> очищение всего множества

# .remove(element) --> удаляет элемент если такого элемента нет то выдает ошибку

# .discard(element) --> удаляет элемент, если такого элемента нет, ничего не происходит

# .pop() --> удаляет случайный элемент(по принципу fifo)

# set_ = {1, 2, 3, 4, 5}
# set_.clear()
# set_.remove(3)
# set_.discard(4)
# set_.pop()
# print(set_)

# set_a.difference(set_b) --> выводит элементы которые есть в set_a но нет в set_b

# set_a - set_b

# set_a = {1, 2, 3}
# set_b = {3, 4, 5, 6}
# # print(set_a.difference(set_b))
# print(set_a - set_b)


# set_a.symmetric_diffirence(set_b) --> Выводит уникальные элементы в обоих множетсвах
# set_a ^ set_b

# set_a = {1, 2, 3}
# set_b = {3, 4, 5, 6}
# print(set_a.symmetric_difference(set_b))
# print(set_a ^ set_b)


# set_a.intersection(set.b) --> выводит похожие элементы set_a и set_b
# set_a & set_b

# set_a = {1, 2, 3}
# set_b = {3, 4, 5, 6}
# print(set_a.intersection(set_b))
# print(set_a & set_b)


# set_a.union(set.b) --> соединяет set_a и set_b
# set_a | set_b

# set_a = {1, 2, 3}
# set_b = {3, 4, 5, 6}
# print(set_a.union(set_b))
# print(set_a | set_b)


# Домашнее задание

# .copy()
# .diffirence_update()
# .intersection_update()
# .symmetric_diffirence_update()

# .isdisjoint()
# .issubset()
# .issuperset()


# for --> бесконечный цикл
# list_ = [1, 2, 3, 4]
# for i in list_:
#     print(i)
#     list_.append(i)


# from itertools import repeat

# for _ in repeat(1):
#     pass


# address = "1.1.1.1"
# print(address.replace("1.1.1.1", "1[.]1[.]1[.]1"))

# address = "1.1.1.1"
# for i in address:
#     if i == '.':
#         i = '[.]'
#     a += i
# print(a)


# command = "G()()()()(al)"
# print(command.replace('(al)', 'al').replace('()', 'o'))



