'''  Декораторы  '''

# def f():
#     print('hello')
 
# print(type(f))
# a = f
# a()

'''   Функция высшего порядка -->  принимает как аргумент и/или возвращает функцию   '''

'''   Декоратор --> функции высшего порядка, позволяет обернуть другую функцию для расширения функционала (не изменяя код)   '''

# def a():
#     print(" i'm a function")

# def b(func):
#     print(f'hello, {func.name}')
#     func()
# b(a)

# def banchmark(func):
#     import time
#     start = time.time()
#     func()
#     finish = time.time()
#     print(f'Время выполнения функции:  {func.name}, заняло: {finish - start}')

# def loop():
#     i = 0
#     range_number = 100000
#     while i < range_number:
#         print(i)
#         i += 1

# def add():
#     ls = []
#     for i in range(100000):
#         ls.append(i)
    

# banchmark(loop)
# banchmark(add)

''' синтаксис декораторов '''

# def decorator_func(func):
#     def wrapper():
#         print('Функция обертки')
#         print('выполняем обертываемую функцию')
#         func()
#         print('выход из обертки')
#     return wrapper

# # @ --> синтаксический сахар

# # @decorator_func
# def say_hi():
#     print('hi')

# # say_hi()
# say_hi = decorator_func(say_hi)
# say_hi()


# def uppercase_decorator(func):
#     def wrapper():
#         return func().upper()
#     return wrapper()


# @uppercase_decorator
# def say_hi():
#     return 'hi'

# print(say_hi)

# @uppercase_decorator
# def a():
#     return 'fdsgsdgsd'
# print(a)


# def banchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         finish = time.time()
#         print(f'Время выполнения функции:  {func.name}, заняло: {finish - start}')
#     return wrapper

# @banchmark
# def loop():
#     i = 0
#     range_number = 100000
#     while i < range_number:
#         print(i)
#         i += 1

# @banchmark
# def add():
#     ls = []
#     for i in range(1000000):
#         ls.append(i)

# loop()
# add()



''' декораторы с аргументами '''
''' универсальная запись '''

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         print('hello')
    
#     return wrapper

# @decorator
# def func1(a, s, d, f, g, h):
#     print('py27')

# func1(1, 2, 3, 5, 8, 7)

# def smart(func):
#     def wrapper(q, w):
#         print('функция обертки')
#         if w == 0:
#             print('На ноль делить нельзя')
#             return None
#         return func(q, w)
#     return wrapper

# @smart
# def division(a,b):
#     return a/b

# print(division(2, 0))


''' декоратор для вызова функции определенного количества раз '''

# def benchmark(num):  
#     def inner_func(func):
#         def wrapper():
#             for i in range(num):
#                 func()
#         return wrapper
#     return inner_func

# @benchmark(5)
# def func():
#     print(1)

# func()



# def strong(func):
#     def wrapper(*args, **kwargs):
#         return '<strong>' + func() + "</strong>"

#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         return '<div>' + func() + '<div>'
#     return wrapper

# @div
# @strong
# def get():
#     return 'John Snow'

# print(get())

'''новый ментор'''

#Декораторы это функция которая позволяет без изменения кода функции расширить ее функционал

# def decorator(func):
#     print(func)
#     func()

# def hello():
#     print('hello stranger!')
# def john():
#     print('My name is John Snow! I am king of North!')    

# decorator(hello)
# print('!!!!!!')
# decorator(john)


# pythonic way  -> @
# синтаксический сахар

# def decorator(func):
#     def wrapper():
#         print(f'Мы вызвали функцию: {func._name_}')
#         func()
#         return wrapper
# @decorator    #@decorator -> decorator(hello)
    
# def hello():
#     print('hello stranger!')

# @decorator    
# def john():
#     print('My name is John Snow! I am king of North!') 

# hello()
# john()

# def benchmark(func):
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time()
#         func(*args, **kwargs)
#         finish = time.time() 
#         print(f'время выполнения функции: {func.__name__}, заняло: {finish - start}')
#     return wrapper

# @benchmark

# def loop():
#     i = 0
#     range_number = 1_000_000
#     while i < range_number:
#         i += 1
 
# @benchmark

# def add():
#     i = 0
#     ls = []
#     range_number = 1_000_000
#     while i < range_number:
#         ls.append(i)
#         i += 1
        
# loop() 
# add()

# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = '<bold>' + func(*args, **kwargs) + '</bold>'
#         return res
#     return wrapper
# @bold
# @div
# def str_(name):
#     return name

#     print(str_('John Snow'))

    

# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвала {func.__name__}(), \nона принела args: {args}, kwargs: {kwargs}')
#         original_result = func(*args, **kwargs)
#         print(f'Trace: вызвала {func.__name__}( \nона вернула : {original_result})')
#         return original_result
#     return wrapper

# @trace
# def say(name, address):
#     return f'{name} --> {address}'

# @trace
# def hello(name, last_name, country):
#     return f'Hello {name} {last_name} from {country}!'

# say('Sherlock Holms', 'Bakery street 221B')
# print()
# hello('Homer', 'Simpson', 'Canada')
