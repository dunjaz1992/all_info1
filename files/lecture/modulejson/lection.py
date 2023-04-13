# JSON - JavaScript Object Notation
# это единный текстовый формат данных, был создан для хранения и передачи данных между сервисами  
# <filename>.json # файл в формате JSON

# {
#     "id":1
#     "author": {
#     "name": "Ed Sheeron",
#     "age": 35
#     },
#     "title": "dont",
#     "feat": false
# }  --- это JSON

#!! js object == {key: value}
# py dict == {key: value}
# JSON == {key: value}

# Процессы Сериализации и Десериализации данных (конвертация)
# сериализация (запись данных в JSON) - это перевод из данных Python в  JSON формат.

# dump - записывает данные в файл формате JSON 
# dumps - записывает данные в текст формата JSON

# Десериализации  (чтение данных из JSON) - это процесс перевода из JSON в PY dict


# load  - это функция которая считывает данные из файла JSON
# loads  - это функция которая считывает данные из текста JSON
'''процесс  Сериализации'''

# import json
# dict_ = {
#     'name': 'John',
#     'status': True,
#     'wife': False,
#     'children': None
# }
# print(dict_, type(dict_))

# json_text = json.dumps(dict_)
# print()
# print(json_text, type(json_text))

# dict_ = {
#     'name': 'John',
#     'status': True,
#     'wife': False,
#     'children': None
# }
# print(dict_, type(dict_))
# with open('new.json', 'w') as file:
#     json.dump(dict_, file, indent=4) (indent eto probel )

'''процесс  Десериализации'''

# import json
# with open('new.json', 'r') as file:
#     json_data = file.read()
# print(json_data, type(json_data))
# dict_ = json.loads(json_data)
# print()
# print(dict_, type(dict_))

# import json

# with open('new.json', 'r') as file:
#     dict_= json.load(file)
#     print(dict_, type(dict_))

# from urllib.request import urlopen
# import json

# url = 'https://randomuser.me/api'
# json_data = urlopen(url)
# print(json_data, dir(json_data))
# dict_ = json.load(json_data)
# print(dict_)



