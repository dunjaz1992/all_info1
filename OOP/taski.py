# class SmartPhones: 
#         def __init__(self, name, color, memory): 
#                 self.name = name 
#                 self.color = color 
#                 self.memory = memory
#                 self.battery = 0 
#         def __str__(self): 
#                 return f"{self.name} {self.memory}" 
#         def charge(self, number): 
#                 self.battery += number 
# class Iphone(SmartPhones): 
#         def __init__(self, name, color, memory, ios): 
#                 super().__init__(name, color, memory) 
#                 self.ios = ios 
#         def send_imessage(self, string):
#                 return f"sending {string} from {self.name} {self.memory}" 
# class Samsung(SmartPhones): 
#         def __init__(self, name, color, memory, android): 
#                 super().__init__(name, color, memory) 
#                 self.android = android 
#         def show_time(self): 
#                 import datetime 
#                 return datetime.datetime.now().time() 
# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7) 
# print(iphone7.send_imessage('hello')) 
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())






# class Dog:
#     def voice(self):
#         print('Гав')
# class Cat:
#     def voice(self):
#         print('Мяу')

# def to_pet(animal):
#     animal.voice()

# rex = Dog()
# barsik = Cat()

# to_pet(barsik)
# to_pet(rex)


# class CustomError(Exception):

#     def __init__(self, capitals_error: object):
#         self.message = capitals_error


# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def check_letters(str_):
#     if str_ == str_.upper():
#         return f'ВСЕ ОТЛИЧНО! {str_}' 
#     else: 
#         raise capitals_error
    
# print(check_letters("HELLO"))


# class Phone:
#     def __init__(self, imei, os) -> None:
#         self.__imei = imei
#         self.__os = os
#         self.__battery_level = 100
    
#     def battery_level(self):
#         if self.__battery_level <0.5:
#             raise Exception('Телефон разряжен')
#         print(f'Уровень заряда: {self.__battery_level}')
#         self.__battery_level -= 0.5
    
#     def get_info(self):
#         if self.__battery_level < 0.5:
#             raise Exception ('Телефон разряжен')
#         print(f'OS: {self.__os}, imei: {self.__imei}')
#         self.__battery_level -=0.5
    
#     def play_music(self):
#         if self.__battery_level <5:
#             raise Exception ('Телефон разряжен')
#         print('Слушаем Мирба')
#         self.__battery_level -=5
    
#     def video(self):
#         if self.__battery_level < 7:
#             raise Exception ('Телефон разряжен')
#         print('смотрим клип')
#         self.__battery_level -= 7
    
#     def charge_battery(self, sec):
#         from datetime import datetime, timedelta
#         from time import sleep
#         now = datetime.now
#         end_time = (now() + timedelta(seconds=sec)).strftime('%M%S')
#         while now().strftime('%M%S') != end_time:
#             sleep(1)
#             if self.__battery_level < 100:
#                 self.__battery_level +=1
#             print(f'Идет зарядка вашей батареи. Ваш уровень батареи: {self.__battery_level}')




# phone = Phone('123 12313 123', 'iOS 15')
# phone.battery_level()
# phone.battery_level()
# phone.get_info()
# phone.play_music()
# phone.play_music()
# phone.play_music()
# phone.video()
# phone.video()
# phone.video()
# phone.battery_level()
# phone.charge_battery(2)



# from datetime import datetime

# class CreateMixin:
#     def create(self, key: str, todo: str):
#         if key in self.todos:
#             return 'Задача под таким ключём уже существует'
#         todos = self.todos[key] = todo
#         return f'Создан todo'


# class DeleteMixin:
#     def delete(self, key: str):
#         if key in self.todos.keys():
#             self.todos.pop(key)
#             return 'Удалили название задачу'
#         return 'нет такого ключа'

# class UpdateMixin:
#     def update(self, key: str, todos: str):
#         if key in self.todos.keys():
#             todos = self.todos.update({key: todos})
#             return f'Обновлено'

# class ReadMixin:
#     def read(self):
#         return sorted(self.todos.items())


# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos: dict = {}

#     def set_deadline(self, deadline: str):
#         deadline = datetime.strftime(deadline, '%d/%m/%Y')
#         deadline_days = deadline - datetime.now()
#         return deadline_days.days()

# todo = ToDo()


# n = int(input("Enter number below 100: ")) 
# print('На лугу пасется ',end='' ) 
# if (n>100):
#     print("Incorrect number") 
# elif((n>10 and n<20) or (n%10 >= 5) or (n%10==0)): 
#     print(n,"коров") 
# elif(n%10==1 ): 
#     print(n,"корова") 
# elif(n%10 in range(2,5)): 
#     print(n,"коровы")

