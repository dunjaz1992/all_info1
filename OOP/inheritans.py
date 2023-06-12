# ------------принципы ООП:
# 1. Наследование
# 2. Инкапсуляция
# 3. Полиморфизм

# 4. Абстракция
# 5. Композиции
# 6. Агрегация

#--------------
# Наследование --> позволяет принимать родительские методы и атрибуты дочернему классу

# Родительский класс
# Дочерний класс

#--------------------
# class Animal:
#     def print_info(self):
#         print('I`m an Animal!')
# class Lion(Animal):
#     pass

# class Dog(Animal):
#     pass

# lion = Lion()
# lion.print_info()


#-------------------

# class Animal:
#     def say(self):
#         print(f'This animal name is: {self.name}: {self.golos}')
#     def eat(self):
#         print(f'{self.name} eats:{self.meal}')

# class Lion(Animal):
#     name = 'lion'
#     golos = 'roar'
#     meal = 'meat'
#     griva = True
#     def info(self):
#         print(f'{self.name} griva:{self.griva}')

# class Dog(Animal):
#     name = 'doglion'
#     golos = 'bark'
#     meal = 'meat'

# class Koal(Animal):
#     name = 'koal'
#     golos = 'roar'
#     meal = 'efkalit'

# rex = Dog()
# simba = Lion()
# julian = Koal()

# rex.say()
# rex.eat()
# print()
# simba.say()
# simba.eat()
# simba.info()
# print()
# julian.say()
# julian.eat()

#------------------- noutbook

# class Employee:
#     bonus = 1.5
#     def __init__(self, first_name, last_name, salary) -> None:
#         self.name = f'{first_name} {last_name}'
#         self.salary = salary
#     def get_info(self):
#         return f'FIO {self.name}, Salary: {self.salary}'
    
#     def give_increase(self):
#         self.salary *= self.bonus # salary = salary * bonus

#     def __str__(self) -> str:
#         return self.get_info()

# class Developer(Employee):
#     def __init__(self, first_name, last_name, salary, language):
#         super().__init__(first_name, last_name, salary)
#         self.lang = language

#     def get_info(self):
#         info = super().get_info()
#         info += f', Prog Lnguage: {self.lang}'
#         return info


# class Manager(Employee):
#     def __init__(self, first_name, last_name, salary, devs=[]):
#         super().__init__(first_name, last_name, salary)
#         self.devs = devs

#     def add_devs(self, developer):
#         self.devs.append(developer)

#     def show_dev(self):
#         return [x.get_info() for x in self.devs]
    
# dev1 = Developer('John', 'Snow', 1500, 'Python')
# dev2 = Developer('Steve', 'jobs', 3000, 'C++')
# dev3 = Developer('Jazgul', 'Ermamatova', 5000, 'Full-stack')
# dev4 = Developer('tirion', 'Lanister', 2000, 'JS')   

# man1 = Manager('Jamie', 'Lanister', 4000, [dev2, dev1])
# man2 = Manager('Meredit', 'Grye', 1500)

# print(f'Manager {man1.get_info()}, has {man1.show_dev()} developers!')
# print(f'Manager {man2.get_info()}, has {man2.show_dev()} developers!')


# 1 task-------------------------------
# class Class1:
#     def first(self):
#         pass
#     def second(self):
#         pass
# class Class2(Class1):
#     def third(self):
#         pass
#     def fourth(self):
#         pass
# obj = Class2() 
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()

#2 task-------------------------
# class A:
#     def method1(self):
#         print('Основной функционал')
# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')
# obj = B()
# obj.method1()

# 3 task----------------------------
# class MyString(str):
#     def __init__(self, string):
#         self.string = string

#     def append(self, new_string):
#         self.string += new_string

#     def pop(self):
#         last_letter = self.string[-1]
#         self.string = self.string[:-1]
#         return last_letter

#     def __str__(self) -> str:
#         return self.string


# example = MyString('String')
# example.append('hello')
# print(example)
# example.pop()
# print(example)        

#4 task------------------------
# class MyDict(dict): 
#     def get(self,key,default = 'Are you kidding?'): 
#         return dict.get(self,key,default) 
    
# obj_dict = MyDict({'some_title': 2})
# print(obj_dict.get('some'))


#5 task-----------------------
# class  Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(self.name, self.age)
# class Student(Person):
#     def faculty(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
# obj_student = Student()
# obj_student.display()
# obj_student.display.student()


# class Person:
#      def __init__(self, name, age): 
#       self.name = name 
#       self.age = age 
#      def display(self): 
#         info = f'name:{self.name}, age:{self.age}' 
#         return info
# class Student(Person): 
#     def __init__(self, name, age, faculty): 
#         super().__init__(name, age) 
#         self.faculty = faculty 
#     def display_student(self):
#            return super().display() + f', faculty:{self.faculty}'
# obj_student = Student('Rick', 21, 'science') 
# print(obj_student.display())
# print(obj_student.display_student())

