'''===Циклы==='''
# while -> цикл, который работает пока условие верно True

# while True:
#     print('hello')
'''опасность в создании бесконечного цикла'''

# counter = 0
# while counter <= 11:
#     print(counter)
#     counter = counter + 1
# while False: # никогда не заработает
    # print('hello')    

# counter = 10
# while counter > 0:
#     print(counter)
#     counter = counter - 1
    
# a = 0 # не работает вообще bool(0) -> False
#     while a:
#     print('hello')

# a = 4578522256621
# summa = 0
# for i in str (a):
#     summa = summa + int(i)
#     print(summa)

# a = '1sdvdv2vd2fv2dfv2dfv2dfv2'
# summa = 0
# for i in a:
#     if i.isdigit():
#      summa = summa + int(i)
#      print(summa)


# i = 0
# summa = 0
# a = str(4578522256621)
# while i < len(a):
#     # print(str(a)[i])
#     summa = summa + int((a[i]))
#     i = i + 1
#     print(summa)

# for i in[]: работать не будет
#  print('0')

# при итерации словаря - получаем только ключи

# dict_.keys() -> прохождение по ключам
# dict_ = {'a': 1, 'b':2, 'c': 3, 'd': 4}
# for i in dict_.keys():
#     print(i)

# ict_.values() -> прохождение по значеним
# dict_ = {'a': 1, 'b':2, 'c': 3, 'd': 4}
# for i in dict_.values():
#     print(i)

''' распаковываем tuple на две переменные'''

# dict_ = {'a': 1, 'b':2, 'c': 3, 'd': 4}
# for k, v in dict_.items():
#     print(k)
#     print(v)

'''получает tuple из ключа и значения'''
# dict_ = {'a': 1, 'b':2, 'c': 3, 'd': 4}
# for i in dict_.items():
#     print(i)


# dict_ = {'a': 1, 'b':2, 'c': 3, 'd': 4}
# for i in dict_:
#     # print(dict_[i])

'''===Ключевые слова в циклах==='''
# break -> полностью выйти из цикла. досрочно прерывает цикл
# continue -> переход к слеующей итерации
# Оператор continue начинает следующий проход цикла, миную оставшееся тело цикла

# for i in range(11):
#     if i == 4:
#         continue
#     print(i)

# for i in range(11):
#     print(i)
#     if i == 4:
#         break

# for i in range(11):
   
#     if i == 4:
#         break
#     print(i)



'''=== Оператор pass==='''
'''ничего не делает . фактически заглушка для обьетов  pass == ...'''

# for i in range(11):
#     if i == 4:
#         pass
#     print(i)


'''=== else==='''
#  слово else, применяется в циклах for и while -> проверяет, был ли произведен выход из цикла без оператора break (естественным образом) Код внутри else отработает, если не сработал break
# i = 0
# while i <= 10:
#     if i == 5:
#         pass
#     print(i)
#     i += 1
# else:
#     print('hello')

'''TELEGRAM'''
''' ===== Циклы ===== '''

# while --> цикл, который работает пока условие верно True

# while True:
    # print('hello')

''' опасность в создании бесконечного цикла '''

# counter = 0
# while counter <= 11:
#     print(counter)
#     counter = counter + 1

# while False:
#     print('hello') # никогда не заработает 


# counter = 10
# while counter >= 1:
#     print(counter)
#     counter = counter - 1


# a = 0 # не будет работать bool(0) --> False
# while a:
#     print('hello')

# a = 5464575686768
# summa = 0
# for i in str(a):
#     summa = summa + int(i)
#     print(summa)



# a = input()
# l = len(s)
# integ = []
# i = 0
# while i < l:
#     s_int = ''
#     a = s[i]
#     while '0' <= a <= '9':
#         s_int += a
#         i += 1
#         if i < l:
#             a = s[i]
#         else:
#             break
#     i += 1
#     if s_int != '':
#         integ.append(int(s_int))
# print(sum(integ))

# a = '1k423kb523k562kjq24kjk24ln5'
# summa = 0
# for i in a:
#     if i.isdigit():
#         summa = summa + int(i)
# print(summa)

# i = 0
# summa = 0
# a = str(5464564574574221)
# while i < len(str(a)):
#     summa = summa + int((a)[i])
#     i = i +1
# print(summa)

# при итерации словаря получаем только ключи
# dict_ = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4}
# for i in dict_:
#     print(i)

# прохождение по ключам
# dict_ = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4}
# for i in dict_.keys():
#     print(i)

# прохождение по значениям
# dict_ = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4}
# for i in dict_.values():
#     print(i)

# прохождение по ключам и значениям
# dict_ = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4}
# for i in dict_.items():
#     print(i)

# получаем(распаковываем) из tuple по 2 переменные
# dict_ = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4}
# for k, v  in dict_.items():
#     print(k)
#     print(v)


# dict_ = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4}
# for i in dict_:
#     print(dict_ [i])

''' получает tuple  '''
# for a, b, c in [(1, 2, 3), (5, 6, 7)]: 
#     print(a, b, c)

'''===== Ключевые слова в циклах ====='''

# break --> полностью выйти из цикла (прерывает цикл досрочно)

# continue --> перейти к следующей операции(итерации) в цикле
# Оператор continue начинает следующий проход цикла, миную оставшееся тело цикла

# for i in range(11):
#     if i == 4:
#         continue
#     print(i)

# for i in range(11):
#     print(i)
#     if i == 4:
#         break

# i = 0
# while i <10:
#     i += 1
#     if i == 3:
#         continue
#     elif i == 7:
#         break
#     print(i)


''' ==== else ===='''

# слово else, применяется в циклах for и while --> проверяет был ли произведен выход из цикла без инструкции оператора break ("естественным образом") 
# Код внутри else отработает если не сработал break

# i = 0
# while i <= 10:
#     if i == 5:
#         pass
#     print(i)
#     i += 1
# else:
#     print('hello')    



''' ===== Оператор pass ====== '''

# ничего не делает(заглушка)  pass == ...

# for i in range(11):
#     if i == 4:
#         pass
#     print(i)