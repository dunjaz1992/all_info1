#Множетсвенное наследование - это когда класс наследуется от двух и более классов
#мро проблема - решение

# class Auto:
#     def play_music_at(self):
#         print('Music is playing')
#     def ride(self):
#         print('We are riding on the ground')
# class Plane:
#     def play_music_at(self):
#         print('Listenin Ed Sheeron')
#     def fly(self):
#         print('We are flying')
# class FutureAuto(Auto, Plane):
#     pass
# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_at()

#------------------
# Проблема ромба - когда поиск шел в родительский класс прежде чем искать у соседнего общего потомка (решена с помощью мро)
# MRO (Method Resolution Order) - механизм для корректного поиска родительских методов. Был создан для решения проблемы ромба, которая появилась после введения object в пайтон. поиск идет таким образом что если у родительских классов есть общий предок, то идет поиск в ширину 

# class Zero:
#     def say(self):
#         print('class zero')
# class First:
#     def say(Zero):
#         print('class First')
# class Second:
#     def say(Zero):
#         print('class Second')

# class Myclass(First, Second):
#     def say(self):
#         super().say()
#         print('class Myclass')

# obj = Myclass()
# obj.say()
# print(Myclass.mro())

#-------------------------------------
# class Z:
#     pass
# class Y:
#     pass
# class A(Z):
#     pass
# class B(Y):
#     pass
# class X(A, B): #1
#     pass
# print(X.mro())


# Проблема перекрестного наследования------------

# class Y:
#     pass
# class X:
#     pass
# class A(X, Y):
#     pass
# class B(Y, X):
#     pass
# class MyMro(type):
#     def mro(cls) -> list[type]:
#         return [cls, A, B, X, Y, object]
     
# class MyClass(A, B, metaclass=MyMro):
#     pass
# print(MyClass.mro())



