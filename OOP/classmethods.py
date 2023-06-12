'''class methods, instance methods, static methods'''
# instance methods  - обычные методы, которые принимают первым аргументом self (ссылка на объект). Нужны они чтобы внутри метода мы могли работать с аттрибутами объекта, получать их или изменять

# class Test:
#     def instance_methods(self, a):
#         print('метод объекта')
#         print('первый аргумент:', self)
# obj = Test()
# obj.instance_methods(5) # если вызвать от объекта, то в self передается автоматически
# Test.instance_methods(obj, 5) # если вызвать у класса, то в self нужно передать объект вручную

# class methods - методы, которые принимают первым аргументом  cls (ссылка на класс) Они нужны для создания или изменения аттрибута класса и для манипуляций  классом внутри метода. Создается при помошью декоратора @classmethod

# class Test:
#     @classmethod
#     def class_method(cls, a):
#         print('метод объекта')
#         print('первый аргумент:', cls)

# obj = Test()
# print(Test, '!!!!')
# print()
# obj.class_method(5)
# print()
# Test.class_method()
# ----------------------------------
# class C:
#     counter = 0
#     def __init__(self):
#         self.a = 4
# obj_1 = C()
# obj_2 = C()
# obj_3 = C()

# print('obj_1', obj_1.counter)
# print('obj_2', obj_2.counter)
# print('obj_3', obj_3.counter)
# obj_1.counter += 1
# print()
# print('obj_1', obj_1.counter)
# print('obj_2', obj_2.counter)
# print('obj_3', obj_3.counter)

# C.counter += 33
# print('obj_1', obj_1.counter)
# print('obj_2', obj_2.counter)
# print('obj_3', obj_3.counter)
#---------------------------------------
# class C:
#     counter = 0
#     def __init__(self):
#         self._inc_counter()
#         self.a = 4
#     @classmethod
#     def _inc_counter(cls):
#         cls.counter += 1
# obj1 = C()
# obj2 = C()
# obj3 = C()
# print(obj3.counter)
# obj4 = C()
# print(obj1.counter)
# print(obj2.counter)
# print(obj3.counter)
# print(obj4.counter)


#--------------------------pizza

#-------------------------------

# class Person:
#     surname = 'Stark'
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
#     def info(self):
#         print(f'Name: {self.name}, {self.surname} -> Age: {self.age}')
#     @classmethod
#     def from_birth_year(cls, name, birth_day):
#         from datetime import date
#         age = date.today().year -birth_day
#         return cls(name, age)

# obj = Person('John', 24)
# obj.info()
# obj2 = Person('Sansa', 19)
# obj2.info()
# obj3 = Person.from_birth_year('Rob', 1996)
# obj3.info()

# from datetime import datetime, date
# a = datetime.now()
# print(a.strftime('%H:%M:%S'))

# staticmethods - это те методы в классе которые не принимают в качестве аргументов ни класс ни объект, так называемые методы которые не изменяют состояние

# class C:
#     @staticmethod
#     def static_methods(a):
#         print('Статик метод')
#         print(a)
# obj = C()
# obj.static_methods(5)
# C.static_methods(5)-------

#-------------------------

# class Cylinder:
#     def __init__(self, radius, height):
#         self.area = self.get_area(radius, height)
#     @staticmethod
#     def get_area(r, h):
#         from math import pi
#         circle = pi * r ** 2
#         side = pi * h * (r * 2)
#         area = circle * 2 + side
#         return round(area, 2 )
# obj = Cylinder(10, 7)
# print(f'Area: {obj.area}')

# obj1 = Cylinder(3, 12)
# print(f'Area: {obj1.area}')