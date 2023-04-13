# работа с файлами
# каретка - указатель - курсор
# open (<путь до файла>)
# file = open (pwd ссылка) # абсолютный путь
# file = open ('files.py') # относительный путь (относительно той директрориив которой вы работаете)

# Режим работами с файлами
# 1: чтение -> r/r+ (read)
# 2: записи -> w/w +(write)
# 3: добавление -> a/a+ (append)
# b, x, t ---самостоятельно изучить---

# file = open('test.txt', 'r')
# print(file.read())
# file.close()

# file = open('test.txt')
# data = file.read()
# data = data.split('\n')
# print(data)
# file.close()

# контекстный менеджер 
# with open('test.txt') as file: # file = open('test.txt)
#     data = file.readline()
#     print(data)
#     print(file.readline())
#     print(file.readline())
#     print(file, 'inside')
# print(file.read(), 'outside')

# file.tell() -> возвращает индекс где находится каретка (курсор)
# file.seek(index) -> перемищает курсор на индекс который вы передали

# with open('test.txt', 'r') as file:
# #     print(file.readline().replace('\n', ''))
# #     print(file.tell())
# #     file.seek(0)
# #     print(file.readline().replace('\n', ''))
#     # data = file.read()
#     # index = data.index('\n')
#     # file.seek(index+1)
#     # print(file.readline().replace('\n', '')) убирает в конце строки
#     # print(file.readlines())
#     file.read()
#     print(file.tell)

# with open('test.txt' , 'r') as file:
    # print(file.readline())
    # print(file.readlines())
    #print( file.read(14))

# with open('test.txt', 'w') as file:
#     file.write('pervaya strochks!\n')
#     file.write('John Snow is Bastart of Ned Stark!\n')
#     file.write('This is lesson about files!\n')
#     file.seek(0)
#     data = ['Bilal is genuis!\n', 'Tima is goodboy\n'] 
#     file.writelines(data)

# with open('test.txt', 'w+') as file:
#     file.write('Jazzzzz!')
#     file.seek(0)
#     print(file.read())

# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
# import re

# def get_imei_code(Image):
#     string = pytesseract.image_to_string(Image)
#     print(string, type(string))
#     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
#     print(list_of_imei)
#     with open('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)

# Image = 'imei.jpg'
# get_imei_code(Image)