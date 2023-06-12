# ООП - объектно-ориентированное програмирование

# Класс - это описание того, как должен выглядеть объект, то есть

# Объект -  это сущность, которую мы создаем от класса, у объекта есть собственные состояние свойств (данные) 
# Целью создание было связать данные с функциями, которые управляли этими жанными

# Свойствами(аттрибутами) - называют обычные переменные внутри класса, в которых хранятся данные объекта

# Методы - это обычные функции внутри класса, методы описывают поведение объекта (фуенкция внутри класса)

#  атрибут это присваивание
# ----------------------


# class Human:
#     age = 0
#     def __init__(self, first_name, last_name, job, citizenship):
#         self.name = first_name + '' + last_name
#         self.job = job
#         self.citizen = citizenship
#     def show_info(self):
        # return f'Name: {self.name}, Age: {self.age}, Job: {self.job}. Citizen: {self.citizen}'
    

# john = Human('John', 'Snow', 'King of North', 'Northernen')
# bilal = Human('Bilal', 'Lanistar', 'Programist', 'KR')

# # print(john, type(john))
# # print(dir(john))
# print(john.show_info())
# john.age = 24
# print(john.show_info())
# john.job = 'King of Westreos'
# print(john.show_info())
# print()
# print(bilal.show_info())

'''2 ex'''
# class Dog:
#     age = 0
#     ushi = True
#     def __init__(self, name, color) -> None:
# # ''' Это метод Инициализаторб именно здесь создаются аттрибуты обхекта'''
# # self - ссылка на объект который только что создался
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!')


#     def show_info(self):
#          print(f'Name: {self.name}, Age: {self.age}, Color: {self.color}. Ushi {self.ushi}')

# rex = Dog('Rex', 'black',)
# pluto = Dog('Pluto', 'brown')
# aktosh = Dog('Aktosh', 'gray')

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()
# print()

# rex.age = 2
# pluto.age = 3 
# aktosh.age = 5
# aktosh.ushi = False

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()
# rex.bark()
# pluto.bark()

# 3 ex

# class Human:
#     def __init__(self):
#         print('init worked')
#         self.p = 'p'
#         self.golod = 100
    
#     def eat(self, meal, doela=True):
#         print(f'{self.p} pokushala {meal}')
#         if doela:
#             self.golod -= 50
#         else:
#             self.golod -=25
# obj = Human()
# print(obj.p, obj.golod)
# obj.eat('burger', doela=False)
# print(obj.p, obj.golod)
# obj.eat('Kruasan')
# print(obj.p, obj.golod)


# 1 task-----------------------------------
# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def show_title(self):
#         return f'Название этой песни: {self.title}'
#     def show_author(self):
#         return f'Автор этой песни {self.author}'
#     def show_year(self):
#         return f'Эта песня вышла в{self.year} году'
    
#     def show_info(self):
#          print(f'Author: {self.author}, Title: {self.title}, Year: {self.year}')
# song = Song('Happy', 'Pharrel Williams', '2013')
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())


# print()




# 2 task-----------------------------

# class Circle: 
#         color='Синий' 
#         pi = 3.14 
#         def __init__(self,radius=int)->int: 
#                 self.radius = radius 
#         def get_area(self): 
#                 result = self.pi * self.radius **2 
#                 return result 
# circle = Circle(2) 
# circle.color = 'yellow' 
# print(circle.color) 
# print(circle.get_area())



# 3 task------------------
# class BankAccount: 
#         balance = 0 
#         def withdraw(self, amount):
#          self.balance -= amount 
#          print(f'Ваш баланс: {self.balance} сом') 
#         def deposit(self,amount): 
#              self.balance += amount 
#              print(f'Ваш баланс: {self.balance} сом') 
# account = BankAccount() 
# print(account.deposit(1000)) 
# print(account.withdraw(500)) 

# 4 task--------------
# class Taxi:
#         def __init__(self, name, cost, cost_km):
#          self.name = name
#          self.cost = cost
#          self.cost_km = cost_km
#         def get_total_cost(self, km):
#          self.cost = self.cost_km * km + self.cost
#          return f'Такси {self.name}, стоимость поездки: {self.cost} сом'
# taxi1 = Taxi(name='Namba',cost=29, cost_km=15) 
# taxi2 = Taxi(name='Yandex',cost=25, cost_km=17) 
# taxi3 = Taxi(name='Jorgo',cost=28, cost_km=15)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))

# 5 TASK-------------------------
# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')
# contact = Phone('John', 'Snow', '+996707707707')
# contact.get_info()



# 6 task----------------------------
# class Salary:
#         percent = 8 
#         def __init__(self, salary, experience): 
#          self.salary = salary 
#          self.experience = experience
#         def count_percent(self): 
#          return self.salary * self.percent / 100 * self.experience 
# obj = Salary(10000, 10) 
# print(obj.count_percent())


# 7 task--------------
# class Nobel:
#         from datetime import datetime
#         a = datetime.now()
#         def __init__(self, category, year, winner):
#          self.category = category
#          self.year = year
#          self.winner = winner
#         def get_year(self):
#          res = self.a.year - self.year 
#          return f'выиграл {res} лет назад'
    
# winner1 = Nobel(category='Литература', year=1971, winner='Пабло Неруда')
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())
# winner2 = Nobel(category='Литература', year=1994, winner='Кэндзабуро Оэ')
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())


# 8 task----------------
# class Password:
#     def __init__(self, password):
#         self.password = password
#     def __str__(self):
#           return '*' * len(self.password)
#     def validate(self):
#           if len(self.password) == 8 and len(self.password) < 15:
#                 return f'Password should be longer than 8, and less than 15'
#           elif not any(map(lambda i: i.isdigit(), self.password)): 
#                 return f'Password should contain numbers too' 
#           elif not any(map(lambda i: i.isalpha(), self.password)): 
#                 return f'Password should contain letters as well' 
#           elif any(map(lambda i: i in ['@', '#', '&', '$', '%', '!', '~', '*'], self.password)): 
#                 return f'Your password should have some symbols'
#           else:
#                 return f'Ваш пароль сохранен.'
          
# password = Password('asd!@12341') 
# print(password.validate()) 
# print(password)

# 9 task---------------------

# class Math:
#     def __init__(self, number):
#         self.number = number
#     def get_factorial(self):
#         self.fact = 1
#         for i in range(1, self.number+1):
#          self.fact = self.fact * i
#     def get_sum(self):
#         sum = 0
#         while (self.number != 0):
#          sum = sum + self.number % 10
#          self.number = self.number // 10
#          return sum
#     def get_mul_table(self):
#         for i in range(1, 10):
#            return i * self.number

# math1 = Math(11)
# print(math1.get_factorial())
# print(math1.get_sum())
# print(math1.get_mul_table())
# print(math1)


# class Math: 
#         def __init__(self, number) -> None: 
#                 self.num = number 
                
#         def get_factorial(self): 
#                 import math 
#                 return math.factorial(self.num) 
        
#         def get_sum(self): 
#                 return sum([int(x) for x in str(self.num)]) 
        
#         def get_mul_table(self): 
#                 res = '' 
#                 for x in range(1, 11): 
#                         res = res + f'{self.num} x {x} = {self.num * x}\n' 
#                 return res 
        
# obj = Math(11) 
# print(obj.get_factorial()) 
# print(obj.get_sum()) 
# print(obj.get_mul_table())

#10 task--------------------------------
# class ToDo:
#     instances = {}

#     def __init__(self, str_) -> None:
#         self.str_ = str_

#     def give_priority(self, priority):
#         self.priority = priority
#         self.instances[priority] = self.str_
#         return self.instances
    
#     def list_of_tasks(self):
#         list_ = [x for x in self.instances.items()]
#         return sorted(list_)
    
# user = ToDo('Go to shop')
# print(user.give_priority(2))
# print(user.list_of_tasks())


