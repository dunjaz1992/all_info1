# ассоциация - принцип ООП в котором устанавливают два класса связанные с друг с другом. Связь обозначает, то что внутри одного объекта будет существовать другой объект от другого класса
# агрегация - слабая связь
# композиция - сильная связь

# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100

# class Iphone:
#     def __init__(self,color):
#         self.color = color
#         self.battery = Battery()
#         # Когда мы создаем внутри класса объект от другого класса - композиция

# a = Iphone('Black')
# a.battery._power -= 50
# print(a.battery._power)
# a.battery.charge()
# print(a.battery._power)
# del a
# # при удалении Iphone удаляется battery

# class Nokia:
#     def __init__(self,battery: Battery,color: str):
#         self.color = color
#         self.battery = battery
#         # когда объект создается из вне класса и передается внутрь - это агрегация

# battery = Battery()
# nokia1 = Nokia(battery, 'Gray')
# print(nokia1.battery._power)
# del nokia1
# # при удалении объекта Nokia, battery остается

# nokia2 = Nokia(battery,'Black')

# -------------------------------------------------
# Композиция
# class Wall:
#     def __init__(self,direction):
#         self.type = direction

#     def __str__(self) -> str:
#         return f'{self.type}'
    
# class Room:
#     def __init__(self) -> None:
#         self.west_wall = Wall('west')
#         self.east_wall = Wall('east')
#         self.south_wall = Wall('south')
#         self.north_wall = Wall('north')

# obj = Room()
# print(obj.east_wall)

# -------------------------------------------------
# Агрегация
# class Stream:
#     def __str__(self):
#         return 'Stream object'
    
# class Logger:
#     def __init__(self,stream=None):
#         self.stream = stream

#     def print_the_logs(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print('None stream')

# stream1 = Stream()
# logger1 = Logger(stream1)
# logger2 = Logger()
# logger3 = Logger(stream = Stream())
# logger1.print_the_logs()   
# logger2.print_the_logs()
# logger3.print_the_logs()

# --------------------------------------------------

# class Engine:
#     country = 'Germany'

#     def __init__(self,power):
#         self.power = power

#     def __str__(self) -> str:
#         return f'Power: {self.power}'
    
# class AudiCar:
#     brand = 'Audi'
#     country = 'Germany'

#     def __init__(self,model,power):
#         self.engine = Engine(power)
#         self.model = model

#     def __str__(self):
#         return f'{self.brand} {self.model}, Engine: {self.engine} -> Engine\'s country: {self.engine.country}'

# car = AudiCar('A8', 400)
# print(car)



















































































class A:
    def get_name(self):
        print('john')

class B:
    def __init__(self, a) -> None:
        self.a = a

# b = B()
# b.a.get_name()

a = A()
b = B(a)
b.a.get_name()
del b
print(a)