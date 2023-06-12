# функция полиморфизм -> len(): __len__
# метод полиморфизм ->  + (__ad__) 

# Полиморфизм  -- это способность функции (метода) использоваться для разных типов (классов)
# Широко распространенное определение: "один интерфейс - много реализация"
# list.pop
# set.pop
# dict.pop

#----------------------------------------------------
# class Cat:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f'It is cat. Cats name is {self.name}, age: {self.age}')
#     def make_sound(self):
#         print('Myaw Myaw')

# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f'It is dog. Dogs name is {self.name}, age: {self.age}')
#     def make_sound(self):
#         print('Bark Bark')


# cat = Cat('Garfild', 5)
# dog = Dog('Pluto', 3)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()

# from math import pi
# class Shape:
#     def __init__(self, name) -> None:
#         self.name = name
#     def are(self):
#         pass
#     def fact(self):
#         return f'я фигура в 2мерной плоскости {self.name}'
# class Square(Shape):
#     def __init__(self, lenght) -> None:
#         super().__init__('квадрат')
#         self.lenght = lenght

#     def are(self):
#         return self.lenght **2
    
#     def fact(self):
#         return super().fact() + '\nУ квадрата все стороны равны и углы равны 90 градусов'
# class Circle(Shape):
#     def __init__(self, radius) -> None:
#             super().__init__('окружность')
#             self.radius = radius 
#     def are(self):
#             return pi * self.radius ** 2
    
# a = Square(8)
# b = Circle(4)

# print(a.fact())
# print(a.are())
# print(b.fact())
# print(b.are())    

