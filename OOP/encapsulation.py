# Инкапсуляция: принцип ооп
# 1. языковая конструкция, которая помогает связать данные с методами для их обработки и управления. (связь между данными и методами которые управляют ими) (класс = капсула)
# 2. Механизм сокрытия, при помощи которого можно ограничить доступ одного компонента программы к другому 

'''модификатор доступа''' 
# Инкапсуляция как механизм сокрытия
# 3 уровня сокрытия данных:
    # 1. Публичный (public) - number, print_number
    # 2. Защищенный(_protected) - _number
    # 3. Приватный(__private) - __number

# Инкапсуляция как связь

# class Phone:
#     number = '+996555201120'
#     def print_number(self):
#         print(f'Мой номер: {Phone.number}')
#         print(f'Мой номер: {self.number}')


# my_phone = Phone()
# my_phone.print_number()

# Инкапсуляция как механизм сокрытия
# 3 уровня сокрытия данных:
    # 1. Публичный (public) - number, print_number
    # 2. Защищенный(_protected) - _number
    # 3. Приватный(__private) - __number

# class Car:
#     _country = 'Korea'
#     def __init__(self) -> None:
#         self.marka = 'Toyota' #public
#         self._model = '123' #_protected)
#         self.__color = 'Green'
# obj = Car()
# # print(dir(obj))
# print(obj._Car__color)
# print(obj._model)
# print(obj._country)


# class Phone:
#     username = 'John'
#     caller = 'Jamie'
#     count_of_calls = 15

#     def call(self):
#         print(f'{self.caller} pdjybn dfv')
#         question = input('Взять трубку(yes/no): ')
#         if question.lower().strip() == 'yes':
#             self.turn_on()
#         else:
#             print('сбросили трубку')


#     def increment_calls(self):
#         self.count_of_calls +=1

#     def turn_on(self):
#         self.increment_calls()
#         print('Allooo!')
#         print(f'Count of calls with {self.caller}: {self.count_of_calls}')

# john = Phone()
# print(john.username)
# john.call()
# john.call()
# john.call()
# john.call()

#------------------------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display_info(self):
#         print(f'My name is {self.name} and I am {self.age} years old!')

# obj = Person('John', 18)
# obj.display_info()
# obj.nationality = 'Kyrgyz'
# print(obj.nationality)
# obj.age = -18
# obj.display_info()
# obj.name = 55
# obj.display_info()

#---------------------------------------------
# getter $ setter
#  они нужны чтобы избежать прямого обращения к сокрытым атрибутам, при этом можно добавить логику валидации (проверки) данных которые будут утсановлены в атрибут


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def display_info(self):
#         print(f'My name is {self.__name} and I am {self.__age} years old!')
#     #getter
#     def name(self):
#         return self.__name
#     #setter
#     def set_name(self, name):
#         if not isinstance(name, str):
#             print('Name must be str object!!!')
#         else:
#             self.__name = name

#     #getter
#     def age(self):
#         return self.__age
#     #setter
#     def set_age(self, age):
#         if not isinstance(age, str) or not 0<= age <150:
#             print('Invalid value for age')
#         else:
#             self.__age = age

# obj = Person('John', 20)
# print(obj.name())
# obj.set_age(-18)
# obj.display_info()
# obj.set_name('Jazgul')
# obj.display_info()