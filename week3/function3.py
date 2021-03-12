# №1
# Написать lambda которая принимает 3 параметра и умножает 
# все параметры между собой. Функция должна вернуть строку: 
# "Объём бассейна " и значение которое получилось.

# a = (lambda x, y, z: f"объем бассейна в литрах {x*y*z}") (10, 5, 4 ) 
# print(a)

# №2
# Написать lambda которая получает сколько дней ПРОШЛО
# с нового года как параметр и говорит пользователю 
# сколько дней ОСТАЛОСЬ до нового года.

# date = (lambda a, b, c: f"сколько прошло с нового года в днях {a - b}\nсколько осталось до нового года в днях {a-c}") (365, 303, 62)
# print(date )

# №3
# Напишите программу которая выводит только нечётные числа с помощью рекурсии.
# def odd(number):
#     print(number)
#     if number % 2 == 0:
#         return number
#     else:
#         odd(number+2)
# odd(1)
#примеры 
# def rec(x):
#     if x < 4:
#         print(x)
#         rec(x+1)
#         return x
# rec(1)

# def main(number):
#     print(number)
#     main(number - 10)

# main(252)
# 
# 
# 
# №4
# Напишите функцию которая принимает SET и 
# рекурсивно удаляет оттуда по одному элементу при запуске.

# def set1(a):
#     print(a)
#     a.pop()
#     set1(a)
# set1({'1','2','3','4','5'})    

# №5
# Напишите функцию которая генерирует 100 рандомных чисел в диапазоне от 10 до 50 и возвращает их в листе. 
# Напишите ДЕКОРАТОР для этой функции которая удалит все дубликаты в первой функции и вернёт всё так же лист.
# import random
# def gen(tor):
#     a = []
#     for x in tor():
#         if x not in a:
#             a.append(x)
#     print(a)
# @gen
# def fool():
#     f = []
#     for i in range(100):
#         s = random.randint(10,50)
#         f.append(s)
#     return f
  
# import random
# def kk(kuff):
#     n = []
#     for x in kuff():
#         if x not in n:
#             n.append(x)
#     print(n)
# @kk
# def gg():
#     l = []
#     for i in range(100):
#         a = random.randint(10,50)
#         l.append(a)
#     return l

# №6
# Напишите функцию которая спрашивает у пользователя login и password. 
# Напишите декоратор который шифрует эти данные и возвращает вам зашифрованные данные. 
# (Можете воспользоваться функцией ord и char, можете загуглить...)
#метод Кайрата 
def log_pass(func):
    a = input('Login: ')
    b = input('Password: ')
    func(a, b)


@log_pass
def shifr(a,b):
    i = 0
    for x in a:
        print(i + ord(x))
        break
    e = 0
    for y in b:
        print(e + ord(y)) 
        break
# def decrypt(message):
#     newS=''
#     for car in message:
#         newS=newS+chr(ord(car)-2)
#     return newS


# print(decrypt('jgnnq"yqtnf'))
#метод Тимура
# def p_l(l):
#     i = 0
#     for x in l():
#         i = i + ord(x)
#     print(i) 
# @p_l
# def l_p():
#     a = input('Напишите log и пароль: ')
#     return a

# №7
# Создайте lambda функцию которая принимает одно число и возвращает это число умноженное на 1.185. 
# Вам дан список [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453] пройдите 
# по списку и примените функцию к каждому числу.

# b = [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
# for i in b:
#     c = (lambda x: x * i  ) (1.185)
#     print(round(c))
