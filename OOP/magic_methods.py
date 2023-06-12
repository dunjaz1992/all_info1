# magic methods (магические методы)
# dunder methods (double underscore)
# служебные методы
# Магия (фишка) заключается в том что эти методы запускаются без прямого обращения к ним. определенные методы могут отвечать за определенные операторы

# class A(int):
#     pass
# obj = A()
# print(dir(obj))

'''Магические методы, сравнение'''
# __eq__(self, other) -> 5 == 8
#                         5.__eq__(8)

# __en__ ->  !=
# __lt__ ->  <
# __gt__ ->  >
# __le__ ->  <=
# __ge__ ->  >=

# print('15' < 'ABC')
# print(ord('1'), ord('A'))
#--------------------------------------
# class Word(str):
#     def __new__(cls, obj):
#         # print(cls, '!!!!!!')
#         # print(obj, '@@@@@@')
#         obj = obj.replace(' ', '')
#         return super().__new__(cls, obj)
#     def __gt__(self, other) -> bool:
#         print('gt сработал')
#         print(self)
#         print(other)
#         return len(self) > len(other)
#     def __lt__(self, other) -> bool:
#         return len(self) <len(other)
#     def __eq__(self, other) -> bool:
#         return len(self) == len(other)

# obj1 = Word('    Hello   ME')
# obj2 = Word('   Wo  l  ve')
# print(obj1 > obj2)
# print(obj1 < obj2)
# print(obj1 == obj2)

#-----------------------------------------

''' + - * / // % ** '''

# + -> __ad__
# - -> __sub__
# * -> __mul__
# // -> __floordiv__
# / -> __truediv__
# % -> __mod__
# ** -> __pow__

#-------NADO PROVERIT-------------
# class Cifra:
#     def __new__(cls, *arq, **kwargs):
#         number = abs(number)
#         instance = super().__new__(cls)
#         instance
#         return cls(number)
#     def __init__(self,number):
#         self.number = number
#     def __add__(self, other):
#         print('add вызвана')
#         res = self.number + other.number
#         print(f'Result: {self.number} + {other.number} = {res}')

# value1 = Cifra(-117)
# value2 = Cifra(53)
# value1 + value2

#-----------------------------

# SINGLETON

# class Singleton:
#     _instance = None
#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#             return cls._instance
#     def __str__(self) -> str:
#         return str(id(self))
# a = Singleton()
# b = Singleton()
# print(a)
# print(b)
# print(a is b)


#-----------------------------------
'''дандер методы стракогого отображения объектов'''
# __str__
# __repr__

# class Base:
#     def __init__(self, stroka):
#         self.string = stroka

#     def __str__(self) -> str:
#         return f'Object: {self.string}'
#     def __repr__(self) -> str:
#         return "Base('Example')"
# obj = Base('Jazz')
# print(obj)
# print(repr(obj))
# obj2 = Base('2pac') 
# print(obj2) 
# obj3 = eval(repr(obj2))
# print(obj3)

# #--------------------------------
# class Kopilka:
#     def __init__(self):
#         self.total = 0
#         self.coins = []
#     def add_coin(self, coin):
#         self.total += coin
#         self.coins.append(coin)
#     def __len__(self):
#         return len(self.coins)
#     def __getitem__(self, index):
#         return self.coins[index - 1]

# obj = Kopilka()
# obj.add_coin(5)
# obj.add_coin(10)
# obj.add_coin(28)
# obj.add_coin(2)
# print(obj.total)
# print(obj.coins)
# print(len(obj))
# print(obj[1])
# print(obj[3])


