
'''===Строки==='''

# строки -> неизменяемый тип данных, который представлянт собой последовательность символов , заключенных в кавычки
# id() -> возвращает номер ячейки памяти 

# a = '5'
# b = 5
# print(id((a)
# print(id((b)

# string = 'трока с одмнарными кавычкми'
# string2 = "строка с двойными кавыками"
# string3 = error
# stirng4 = "Don't"
# string5 = '"makers"'
# print(string4)
# sting6 = '''
# scdv
# sbsb
# '''
# print(string6)
# # len() -> возвращает кол-во символов в строке 
# print(len(string6))
# print(len(2123548)) #error

'''===Экранизация строк==='''

# '\символ'
# '\n' -> перенос на следующую строку 

# a = 'hello \nworld'
# print(a)
# '\t' -> табуляция 4 пробела (таб)
# a = 'hello \tworld'
# print(a)
# '\\' -> для отоброжения '\'
# a = 'hello\\'
# print(a) hello\
# '\'' -> для отоброжения '

# "\""  для отоброжения "
# '\r' -> возвращает каретки в начало строки

# print('makers \rlab') #labers
# '\v' -> перенос на новую строку со смещением в право на длину предыдущей
# print('hello\vworld')
# '\a' -> гудок встроенного в систему динамика
# print('hello\a')


# # конкатенация строк- склеивание строк
# a = 'hello'
# b = 'world'
# print(a+b) # hello world
# Дублирование строк
# print(a * 3) # hello hello hello

'''====Форматирование строк(динамические строки)==='''

# 1. %
# 2. .format()
# 3. f-строки

# name = input('введите имя: ')
# print('Hello, %s' %name)

# name = input('name: ')
# name2 = input('name2: ')
# print('hello, {}, {}'.format(name, name2))

# # 3 интерполяция 
# name = input('name: ')
# name2 = input('name2: ')
# print(f'hello {name}, {name2}')

# print(dir)('s')

'''=== Методы строк==='''
# методы - функции, к которым мы обращаемся через точку
# методы на is проверяют и возвращают True/False

# s.isdigit() ->  проверяет , стоит ли строки только из чисел (true, false)
# s.isalnum() -> проверяет , стоит ли строки только из букв и чисел
# s.isalpha() -> проверяет , стоит ли строки только из букв
# s.lower() -> проверяет , все символы в нижнем регистре 
# s.isupper() -> проверяет , все символы в верхнем регистре
# s.isspace() -> состоит ли строка из неотображаемых символов (пробел, '\n'  )


# .lower() -> переводит целую cтроку в нижний регистр 
# print('QQQ.lower()) #qqq

# .upper -> переводит  cтроку в верхний регистр 
# print('qqq'.upper()) #QQQ

# .swapcase() -> переводит символы в противополжный регистр 
# print('QQww'.swapcase()) #qqWW

# title() -> переводит первую букву каждого слова в верхний регистр
# print('hello world'.title()) # Hello World

# .capitalize -> переводит первый символ строки в верхний регистр 
# print('hello world'.capitalize()) # Hello world

# .strip() -> убирает пробелы в начале и в конце строки
# print('   hello world   '.strip()) # hello world

# .lstrip() -> убирает пробелы в начале 
# .rstrip() -> убирает пробелы в конце

# .replace(old, new, [count]) -> меняет old значение на new определнное кол-то раз count
# print('ha ha ha'.replace('ha', 'new', 2)) # new new ha
# .split(разделитель)-> делит строку по раздилетелю, возвращает список (массив)

# print('hello py27 hello'.split()) 
# a = "gfdbfb fbdfb dffdb"
# print(a.split())
# list_ = a.split()
# print(list_)


#  разделитель .join(iterable) -> соединяет в строку по разделителю
# # print('-->'.join(list_))

# .startswith(string) -> проверяет начинается ли наша строка с string
# a = 'hello world'
# print(a.startswith(Hello))
# .endswith(string) -> проверяет заканчивается ли строка на string
# print(a.endswith(World))
# .count(string) -> считает количество вхождении string в строке
# a = kkjjff
#ptint(a.count('kk'))


'''======== Индекс ========'''
# индекс - порядковый номер элемента
'hello'
#01234
#...-3-2-1

# a = 'hello world' 
# print(a[0])
# print(a[5])
# print(a[-1]) # последний элемент 

'''срезы'''
# a[start:stop:step]
# срезы по индексу -> нахождение подстроки, начиная от start и заканчивая до stop (stop не включительно), шаг - через какой элемент записывать

# print(a[0:2])
# print(a[:])
# print(a[5:])
# print(a[6::106890])

# a = 'hello world' #dlrow olleh
# print(a[::-1]) # переворачивает строку

# a = 'hello world'
# print(a[2:-1])
















