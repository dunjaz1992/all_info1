# def add_one(x: int) -> int:
#     return x + 1


# def division(x: int, y: int) -> float:
#     if y == 0:
#         raise ZeroDivisionError
#     return x/y



# def add(x: int, y: int) -> int:
#     return x + y 

db = [
    {'name': 'Hello', 'password': hash('12345678')},
    {'name': 'World', 'passwodr': hash('helloword')} 
]
# print(db)
def in_database(name):
    for user in db :
        if user['name'] == name:
            return True
    return False
# print(in_database('Hello'))
def register (name, password1, password2):
    if in_database(name): 
        raise Exception('User with name exists')
    if password1 != password2:
        raise Exception('password is not same')
    if len(password1) < 7:
        raise Exception('too short password')
    user = {'name': name, 'password': hash (password1)}
    db.append(user)
    return ' You are registrated succesful!'
# print(register(name=input(), password=input(), password2=input()))

def login(name, password):
    if not in_database(name):
        raise Exception('пользо не найден')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception('пароль не верный')
        return 'welcome'
# print(login(name=input('введите имя: '), password=input('введите пароль: ')))






def main():
    print('welcome')
    while True:
        action =  input('reg: 1, login:2, quite: 2')
        if action == '3':
            break
        elif action == '1':
            name = input('vvedite imya: ')
            p1 = input('vvedite parol: ')
            p2 = input('vvedite podtverjdenie patolya: ')
            print(register(name, p1, p2))

        elif action == '2':
            name = input('vvedite imya: ')
            p1 = input('vvedite parol: ')
            print(login(name, p1))
        else:
            print('neverno')
main()