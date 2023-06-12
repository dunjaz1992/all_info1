# PostgresSQL - это система управления БД(СУБД/DBMS)
# СУБД - это ряд программ и инструментов позволяющих создавать БД, управлять ею и манипулировать данными внутри(CRUD)

# Postgres - это сама база данных, она реляционная, то есть данные хранятся в виде таблиц, и таблицы имеют связи между собой
# SQL (Structured Query Language) - декларативный язык структурированных запросов, он применяется для создания и получения данных при помощи запросов

# ----------------------------------------------
# Команда для входа в бд через юзера postgres:
# brew postgres psql

# Команда для входа
# exit

#команда для входа в своего юзера
# psql

# команда для выхода 
# \q 

# создание пароля 
# ALTER USER 'username' WITH PASSWORD '1';

# изменение пароля 
# ALTER USER 'username' WITH PASSWORD '1';

# создание бд
# CREATE DATABASE 'name';

# \l - список всех бд

# \du - все юзеры

# \dt - все таблицы (нужно подключиться к бд заранее)

# \c 'name' - команда для подключения к бд

# psql -U <username> -d <dbname> - подключаемся под выбранным username к dbname


# drop role 'username' - удаляет юзера


'''Типы полей в Postgres'''

# Numeric types (числовые типы)

    # a. smallint(2 bytes) -> -32767 to 32767
    # b. integer(4 bytes) -> -2.147...mil to 2.147...mil
    # c. bigint(8 bytes) -> ... (infinity)
    # d. real(4 bytes) -> число с плавающей точкой, вещественные числа
    # e. double precision (8 bytes) -> real, но только с двойной точностью
    # f. serial(4 bytes) -> integer, auto-increment

# Charachter types (Символьные типы (строковые))

    # a. varchar(количество символов) -> если мы укажем 50 символов, а заполним только 10, то остальные будут свободны (max char 255)
    # b. char(количество символов) -> если мы укажем 50 символов, а заполним только 10, то остальные будут заполнены пробелами (max char 255)
    # c. text() - такой же строковый тип данных с неограниченным количеством символов

# Boolean Type
    # a. boolean(1 bytes) -> True/False

# date -> календарная дата (YYYY.MM.DD)
# location -> координатная точка (x,y) - (245, -12)
# enumerate types:
    # ('a','b','c')
    # CREATE TYPE <name> AS ENUM ('Happy', 'Sad', 'Mad');

# --------------------------------------------------------

# команда для создания таблицы
# CREATE TABLE <table name> (
    # <column> ,type>
# )

# команда для удаления всей таблицы
# DROP TABLE <name> - удаление таблицы

# CREATE TABLE films (
    # code char(5),
    # title varchar(100),
    # date date,
    # genre varchar(50),
    # budget integer,
    # country varchar(50),
    # id serial
# );

# Команда для добавления данных в таблицу
# INSERT INTO <tablename> [(columns)] VALUES (data), (data);

# Команда для получения данных
# SELECT (columns)/* FROM <table>;

# Команда для обновления данных
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>;

# Команда для удаления данных
# DELETE FROM <table> WHERE <column> = <value>;

'''3'''

# ORDER BY: Позволяет нам сортировать входящие данные по убыванию или возрастанию. ASQ (по возрастанию) и DESC (по убыванию)
# Cинтаксиз: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC];

# WHERE:  используется для фильрации по полям. Будут выводится только те данные которые соответствуют условию оператора WHERE
# Cинтаксиз: SELECT <row> FROM <tablename> WHERE <row> = 'чему-либо';

# BETWEEN: условие между
# SELECT * FROM products WHERE id BETWEEN 3 and 8

# LIKE: выводит результат который соответсвует введенному шаблону для строк.
# Чувствителен к регистру 

# ILIKE: тоже самое, только не зависит от регистра
# СИНТАКСИЗ: SELECT  <row> FROM <tablename> WHERE <row> LIKE/ILIKE 'чему-либо'



# AND: оператор и, для множественных условий
# IN: WHERE <row> in (1,2,3,4)
# LIMIT: ставит ограничение в кол-ве получаемых данных

''''''


# GROUP BY: Разделяет данные которые мы получаем в SELECT, при этом группируя их по определенному признаку. И теперь для каждой группы можно использовать функцию.

# HAVING: ставит условие при помощи которого данные отбираются в группировку

# Агрегатные функции: AVG(), COUNT(), MIN(), MAX(), SUM()



''''''
# Экспорт бд(дамп):
# pq_dump -U <username> -d 'dbname' > 'file.sql'

# Импорт:
# psql -U <username> -d <dbname> -f <filename>



'''СВЯЗИ МЕЖДУ ТАБЛИЦАМИ(relations)'''

# 1. Один к Одному (One to One) - человек и паспорт
#         в одну из таблиц добавляется поле fk и дается ограничение unique
# 2. Один ко Многим (One to Many) - человек и банковские карты
#         в таблицу много (банковские карты) добавляется поле fk
# 3. Много ко Многим (Many to Many) - студенты и преподы
#         создается вспомогательная третья таблица со связями

'''''Оганичения'''''
    # 1. NOT NULL - обязательно к заполнению
    # 2. UNIQUE - то что будут хранится только уникальные данные
    # 3. CHECK -> CHECK > 0 - ограничения проверки на условия
    # 4. PRIMARY KEY - для установки идентификатора данных в таблице
    # 5. FOREIGN KEY - для установки связей между таблицами
    # 6. ON DELETE - для установки поведения при удалении данных которые были связаны
    

'''JOIN'''

# Join: выборка данных из двух таблицб соединение таблиц
# LEFT JOIN: выборка будет содержать все строки из левой таблицы
# RIGHT JOIN: выборка будет содержать все строки из правой таблицы


# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1, orders o1 WHERE p1.id = o1.product_id;
#- Запрос сразу в две таблицы

# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum
# FROM products p1 JOIN order o1 ON p1.id = o1.produst_id;