'''области видимости и пространства имен'''

# 4 всего 
# 1  builtins (встроенная)
# print()
# len()
# abs()
# input()

# 2. Global(глобальное)-> все имена внутри файла
# a = 5
# b = 6

# 3. Enclose -> пространство находящийся между двумя пространствами (не всегда есть)

# 4. local (локальное) -> внутри функции

# print(dir(__builtins__)) -> возвращает список встроенных классов, объектов и функций


# a = 34
# b = 0

# print(globals())
# print(globals()['b'])
# print(b is globals()['b'])
# globals()['y'] = 'hello world'
# print(globals())
# print(y)

# v = 1
# def hello():
#     a = 'hello'
#     #print(a)
#     print(v)
#     print(locals())
#     print(globals())

# hello()

# def func(a, b):
#     x = 7
#     print(locals())
# func(3, 4)
# print(a, b) #Error

# print(locals())

# '''Enclose -> вложенность в функциях'''
# x = 'эт глобальная переменная'
# def some_func():
#     x = 'это Enclose переменная'
#     def some_funcs2():
#         x = 'это локальная переменная'
#         # print(x)
#     some_funcs2()
    # print(x)

# print(x)
# some_func()
'''порядок поиска переменных'''

# local -> enclose -> global -> builtins
# a = 8
# def funcs():
#     b = 'local'
#     return a + 100
# print(funcs())

# global -> позволяет менять значение глобальной переменной, находясь в локальной области видимости


# a = 8
# def funcs():
#     global a 
#     a += 100
#     return 'changed'
# print(funcs())
# print(a)

# count = 0
# def counter():
#     global count
#     print(count)
#     count += 1
# counter()
# counter()
# print(counter())

# a = 9

# def outer_func():
#     a = 10
#     def inner_func():
#         a = 8
#         print('inner', a)
#     inner_func()
#     print('outer' , a)
# outer_func()
# print(a)


'''nonlocal'''

# def counter(i):
#     count = 0
    


#     def add():
#         print(count)
#     add(+1)
# print(counter(10))



'''новый ментор'''

# 1 Область видимости и пространство имен scopes
# технология которая определяет контекст имени  (переменные)в рамках которого мы можем ее использовать 
#built ins(встроенная область видимости) print, len, max
#global (глобальная) - область одного файла
# enclosed(локальная либо замкнутая)  nonlocal()
#local(локальная) - область внутри одной функции

# x = 200
# def myFunc():
#     print(x)
#     a = 300
#     print(a)
# myFunc()
# print(x)
# # print(a)

# a = 10 #global
# print #built-in
# def hello():
#     a = 'hello world'
#     print(a, 'local inside in func!')
# hello()
# print(a)

# LEGB -local enclosed global built-in


#===========
# enclosed замкнутое пространство имен - локальное пространство, у которого есть внутренее (вложенное) локальное пространство

'''показывает кого видит по очереди'''
# x = 'global'
# print(x, '1')

# def enclosed(): # global
#     x = 'enclosed'
#     def local(): #local
#         x = 'local'
#         print(x, '3')
#     print(x, '2')
#     local()
#     print(x, '4')
# enclosed()
# print(x, 5)


# global позволяет изменять значения глобальной пременной находясь внутри локальной сети

#nonlocal позволяет изменять значения не локальной (замкнутой) переменной находясь внутри локальной сети

# var = 100
# def increment():
#     global var

#     var +=1 # var = var + 1
# print(var)
# increment()
# print(var)



# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num +=1
#         return num
#     return increment
# c = counter()
# print(c()) #1
# print(c()) #2
# print(c()) #3
# print(c()) #4
# print(c()) #5
# print(c()) #6
# print(c()) #7

'''список встроенных функций'''
# print(dir(__builtins__))
# print(len(dir(__builtins__)))

# globals - func которая возвращает все имена внутри глобальной видимости
# local - func которая возвращает все имена внутри глобальной видимости локальной


# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num +=1
#         return num
#     return increment
# c = counter()
# def showStats(heroes, mobs):
#     print()
#     print(f'John Snow ты убил: \n\tгероев: {heroes} \n\tмобов: {mobs}')
# counter_heroes = counter()
# counter_mobs = counter()
# heroes = 0
# mobs = 0
# print('Приветствую Вас, король севера John Snow, в Вестеросе!')
# while True:
#     print('тебе доступны следующие действия:')
#     print('1-убить героя, 2-убить моба, 3-статистика, 4-выйти из игры')
    
#     choice = input('введите что хотите сделать: ').strip()
#     if choice =='1':
#         heroes = counter_heroes()
#         print('Вы обезглавили Ланистера!')
#     elif choice =='2':
#         mobs = counter_mobs()
#         print('Вы убили Белого Ходака!')
#     elif choice =='3':
#         showStats(heroes, mobs)
#     elif choice =='4':
#         print('Пока пока! ждем еще раз!')
#         break