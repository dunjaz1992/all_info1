'''  обработка исключений'''

# ошибка -> проблема в синтаксисе (которые исправляем самостоятельно)
# 1. SyntaxError -> забыли поставить двоеточие, кавычки, точку, скобку и т.д.
# 2 = 8
# 2. IndentationError -> неправльный отступ
# hello = 9
# 3. TabError ->  неверная табуляция (смешивание пробелов и табов)

# исключение
# 1. NameError
# 2. IndexError
# 3. ZeroDivisionError
#    ArithmeticError
# 4. KeyError
# 5. ImpotError
# 6. ValueError
# 7. TypeError
# 8. AttributeError
# 9. BaseException ( прородитель)

NameError # исключение, которое выводит, когда обращаемя к несуществующему имени
# print(hello)
IndexError # выводит, когда обращаемя к несуществующему индексу

# list_[1, 2, 3]
# list_[100]
ZeroDivisionError # выводит при делении на ноль
# 5 / 0
# 5 // 0
#5 % 0
KeyError # выводит, когда обращаемя по несуществующему ключу
# dict_ = {'a': [1, 2, 3] 'b': 'hello'}
# dict_['c']
# dict_.pop('c')

ImportError # неправильный импорт
# from math import pi2

ValueError # выходит, когда пытаемся распаковать каку-то последовательность, где кол-во элементов и переменных не совпадают

# int( '12r')
# a, b, c = 'ab'

TypeError # когда мы пытаемся использовать метод не свойственный какому-то типу данных. или когда пытаемся передать больше аргументов чем требуется.

# [].append()
# for i in 25478:
#     print(i)
# 5 + '5'
# {[1, 2, 3]: 'hello'}
# input('hello', 1)
# [].append(1, 2)

AttributeError # когда обращаемся к несуществующему атрибуту или методу объекта
# {}.replace('a', '')
# 'hello'.splite()


'''===== обработка исключений====='''

# чтобы код не прекращал работы при некорректных данных

# try:
#     '''код, который может вызвать ошибку'''

# except(ошибка, которая может возникнуть):
#         '''код, который сработает, если в try возникла ошибка'''
# else: 
#         '''код, который отработает, если в try не возникла ошибка'''
# finally:
#         '''код, который отработает в любом случае'''

# try:
#     a = int(input('введите число '))
# except ValueError:
#     #print('f')
#     try:
#         a = int(input('введите только число '))
#     except ValueError:
#       print('все')

# try:
#     a = 2
#     b = 0
#     print(a/b)
# except ZeroDivisionError:
#     print('так нельзя')


# try:
#     while True:
#         print(0)
# except KeyboardInterrupt:
#         print('ctrl+c')  fbfb

# try:
#     num1 = int(input('1 '))
#     num2 = int(input('2 '))
#     print(num1/num2)
# except:
#     print('произошла ошибка')


# try:
#     dict_ = {key: key**2 for key in range(100) if a % 2 ==0}
#     print(dict_)
# except NameError:
#     a = 2
#     dict_ = {key: key**2 for key in range(100) if a % 2 ==0}
#     print(dict_)


# else в обработке исключений

# dict_ = {'a': 5, 'b': 10, 'c': 15, 'd':20}
# key_ = input('введите ключ ')
# try:
#     res = dict_[key_]
#     print(res)
# except Exception as e:
#     print(f'нет такого ключа{e}')
# else:
#     print('block else')

'''оператор finally в try except'''

# try:
#     res = a * 2
#     print(res)
# except Exception as e:
#     print(f'возникла {e.__class__}')
# finally:
#     a = 5
#     res = a * 2
#     print(res)

# raise ->  искуственно вызывает ошибку 

# n = int(input('Enter ut age: '))
# if n <= 0:
#     raise Exception (значение не может быть равно 0 или меньше нуля)
# res = n + 100
# print(res)

# try:
#     if 2 > 1:
#       raise Exception('f')
# except Exception:
#     print('Gde logika')

# try:
#     if 2 > 1:
#       raise ValueError('f')
# except Exception as e:
#     print(f'Gde logika{e.__class__}')
