# class Human:
#     age = 0

#     def __init__(self, first_name, last_name, weight, nation):
#         self.name = f'{first_name} {last_name}'
#         self.weight = weight
#         self.nationality = nation
#     def birthday(self):
#         from random import randint
#         print(f'\nHabby birthday, {self.name}!!!!')
#         self.age +=1
#         self.weight += randint(3,7)

#     def show_info(self):
#         print(self.name, self.age, self.weight, self.nationality)
# human1 = Human('John', ' Snow', 3.3, 'American')
# human2 = Human('Abu-Bakr', 'Al-nasyr', 3.8, 'Arabic')

# human1.show_info()
# human2.show_info()
# print()
# print('After one year:')
# human1.birthday()
# human2.birthday()
# print()
# human1.show_info()
# human2.show_info()

#-----------------

# class Student:
#     univer = 'Harvard'

#     def __init__(self, name):
#         self.name = name
#         self.books = []
#         self.language = {}
#         self.knowledge = 0
#         self.is_ready_to_work = False

#     def add_points(self, points):
#         self.knowledge += points
#         if self.knowledge > 500 and not self.is_ready_to_work:
#                 self.is_ready_to_work = True
#                 print(f'{self.name} get 500 points!!!')

#     def read_books(self, book_name):
#          self.books.append(book_name)
#          self.add_points(50)
#     def do_project(self):
#          self.add_points(100)

#     def learn_new_language(self, language, percent):
#          if percent not in range(70, 101):
#             print('invalid points')
#          else:
#             self.language[language] = percent
#             self.add_points(percent)
            
# st1 = Student('John Snow')
# st2 = Student('Aizirek Akimbaeva')

# print(st1.name)
# print(st2.name)

# print(f'Before study {st1.name}:{st1.books} {st1.language, {st1.knowledge}}')
# print(f'Ready to work: {st1.is_ready_to_work}')

# st1.read_books('Game of Thrones')
# st1.read_books('Martin Eden')
# st1.read_books('Alghoritms and Data Structures')
# st1.read_books('Eugene Onegin')
# st1.do_project()
# st1.do_project()

# st1.learn_new_language('Python', 40)
# st1.learn_new_language('C++', 90)
# st1.do_project()


# print(f'After study {st1.name}:{ st1.books} {st1.language, {st1.knowledge}}')
# print(f'Ready to work: {st1.is_ready_to_work}')

#------------------


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def show_info(self):
#         return f'{self.brand} --> {self.model}'
    
#     def __str__(self):
#         return f'{self.brand} --> {self.model}'
    
# obj = Car('BWM', '7 series')
# print(obj)
# obj2 = Car('Lada', 'Sedan')
# print(obj2)
# print(obj.show_info())

#---------------
# import random


# class Sniper:
#     health = 100
#     def __init__(self, name):
#         self.name = name
#     def shoot(self, other):
#         other.health -= 20
#         print(f'---Атаковал--- {self}')
#         print(f'y {other} ostalos {other.health}')

#     def __str__(self) -> str:
#         return self.name
    

# sniper1 = Sniper('John Snow')
# sniper2 = Sniper('Sanzhar Mykyev')


# while sniper1.health and sniper2.health:
#     choice = random.randint(1, 2)
#     sniper1.shoot(sniper2) if choice ==1 else sniper2.shoot(sniper1)
# if sniper1.health:
#     print(f'{sniper1} won the game!')
# else:
#     print(f'{sniper2} wont the game!')
    
  

