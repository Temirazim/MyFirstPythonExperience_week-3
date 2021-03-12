# 
# №1
# Создайте 4 функции: add(), substract(), multiply(), divide()
# которые будут принимать по 2 аргумента и возвращать результат:
# сложения, вычитания, умножения и деления. 

# def add(a, b):
#     result = (a+b)
#     print(result)
# add(12, 4)    
# def substract(a, b):
#     result = (a-b)
#     print(result)
# substract(15, 5)     
# def multiply(a, b = 2):
#     result = (a * b)
#     print(result)
# multiply(20)    
# def divide(a, b ):
#     result = (a / b )
#     print(result)
# divide(9, 3,)
# # №2
# Написать Функцию которая принимает предложение как аргумент, 
# считает количество букв и возвращает сколько символов он ввёл.
# НЕ ИСПОЛЬЗОВАТЬ функцию len()

# def word(a):
#     letter = 0
#     for i in a:
#         letter +=1
#     print(letter)
# word("what are you doing now")

#метод Кайрата
# Tent1703 Кайрат, [02.03.21 12:46]
# def word_sum(a):
#     c = 0
#     for x in a:
#         if ('a' <= x <= 'z') or ('A' <= x <= 'Z') or ('а' <= x <= 'я') or ('А' <= x <= 'Я'):
#             c += 1
#         else:
#             pass
#     print(c)

# a = input()
# word_sum(a)

# №3
# Напишите функцию которая принимает 2 Dictionary и добавляет втрорую Dictionary к первой.
# def dic(a, b):
#     a.update(b)
#     print(a)
# dic({1: "one", 2: "two", 3: "three"}, {4: "four", 5: "five"})




#№4
# Напишите функцию которая спрашивает у вас чтобы вы хотели заказать покушать и выпить.
# А затем записывает это всё в файл на рабочем столе menu.txt
# def menu():
#     menu = input("Добро пожаловать в наш космический ресторан! Что желаете выпить или покушать? ")

#     h = open("/home/azim/Desktop/restuarantgalaxy.txt",'w')
#     h.write(menu)
#     h.close()

# menu()


# №5
# Создайте функцию которая принимает слово и создаёт файл 
# с таким именем в той же директории, где был запущен Ваш .py файл.

# def anywords():
#     a = input("Please write your word: ")
#     b = open("word.txt", 'w')
#     b.write(a)
#     b.close()
# anywords()    

# №6
# Создайте 2 функции где одна функция вложена в другую. 
# Главная функция должна выводить на экран текст: "Я главная функция".
#  А вложенная функция должна выводить на экран: "Я вложенная функция."
# 
# 
# def func1(a):
#     global func2
#     def func2(b):
#         return b
#     return a
# print(func1("Я главная функция"))
# print(func2("А я вложенная функция"))

    
    

# №7
# Создайте функцию которая принмает тип данных dictionary, 
# но возвращает два Tuple в одном из них все ключи, 
# в другом только значения.

# def dictup(**k):
#     a = []
#     b = []
  
#     for key, value in k.items():
#         a.append(key)
#         b.append(value)   
#     print(tuple(a))
#     print(tuple(b))
# dictup( name = 'azim', level = 'begginer')    
#№8
# Напишите программу которая определяет ПРОСТЫЕ ЧИСЛА.
# Простое число - это число которое делится только на себя и на 1.
# simple_numbers = int(input("Введите любые числа для поиска простых чисел: "))
# for x in range(1,simple_numbers):
#         count = 0
#         delitel = 2
#         while delitel<simple_numbers:
#             if x % delitel == 0:
#                 count += 1
#             delitel += 1
#         if count == 0:
#              print (f'{simple_numbers} простое число')
# def numb():
# num = int(input("Please write any numbers: "))
# for i in range(num):
#     if num / num = 1 and num / 1 = num:
#         print(f"{num} - this is simple number")
#         break
#     else:
#         print("this is not simple number")

# №9
# Напишите функцию которая принимает 2 аргумента. 
# Эти аргументы могут быть любого типа данных но 
# функция должна Вам вернуть эти аргументы как тип данных List

# def twoargs(a, b):
#     list1 = []
#     list1.append(a)
#     list1.append(b)
#     print(list1)
# twoargs(911, 'support')    


#№10
# Напишите функцию которая спрашивает 
# у пользователя число и выводит ему на 
# экран именно столько строк самой себя как текст.

# pol = int(input("Ведите число: "))
# def polzov(a):
#     # print(a)
#     b = int(pol)
#     c = a[0]
#     while a < b:
#         print(str(a) == b)

# polzov('Super')

# def rep(f):
#     a = int(input('input number: '))
#     for x in range(a):
#         print(f == str(a))
# rep(False)        

#№11
# Создайте функцию которая принимает Имя пользователя и его зарплату
# и возвращает это строкой как: ИМЯ - ЗАРПЛАТА. 
# Если в функции не была указана зарплата - подставьте её сами. Значение по умолчанию - 5000.
# def imyazp(a, b, *k):
# def sallary(a, b = 5000):
#     a = input("ведите имя пользователья: ")
#     print(a, b)
# sallary('')    
# №12
# Напишите функцию которая спрашивает число N и генерирует
# вам List состоящий из N разных элементов.
import random
def lop():
    a = int(input("Ведите N-ое число: "))
    gen =[x for x in range(a)]
    b = []
    b.append(random.randint(str(gen)))
    print(b)
lop()    


