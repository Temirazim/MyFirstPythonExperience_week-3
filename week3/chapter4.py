# 1)Student
# Создайте класс Student, конструктор которого имеет параметры name, lastname,

# department, year_of_entrance. Добавьте метод get_student_info, который

# возвращает имя, фамилию, год поступления и факультет в

# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:

# Программирование.”

# class Student():

#     def __init__(self, name, lastname, departament,year_of_entrance):
#         self.name=name  
#         self.lastname=lastname
#         self.departament=departament
#         self.year_of_entrance=year_of_entrance

#     def get_student_info(self):
#         print(f'Меня зовут {self.name} фамилия {self.lastname} окончил учебу {self.departament}на факультете  {self.year_of_entrance}')

# s= Student('вася','иванов',2017,'программирования')
# s.get_student_info()



# 2)Airplane
# Создайте новый класс Airplane. Создайте следующие характеристики (полей)

# объекAта:

# ● make (марка)

# ● model

# ● year

# ● max_speed

# ● odometer

# ● is_flying

# ﻿

# и методы имитирующих поведение самолета take off (взлет), fly (летать), land

# приземление). Метод take off должен изменить is_flying на True, а land на False. По

# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и

# изменять показания одометра (километраж). Создайте 1 объект класса и используйте

# все методы класса.
#Вариант ТИмура
# class Airplane():
#         '''Создание класса самолета'''
#     def __init__(self,make,model,year,max_speed,odometer):
#         '''Инициализация атрибутов самолёта'''
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = odometer
#         self.is_flying = False
#     def take_off(self,взлёт):
#         '''Взлёт самоелёта'''
#         self.is_flying = взлёт
#         print(f'Самолёт {self.make.title()} модель {self.model.title()} {self.year} года выпуска при команде {self.is_flying} взлетайте!')
#     def fly(self):
#         '''Самолёт летит'''
#         print(f'Общее расстояние полёта 52 000 км, при той же скорости {self.max_speed} км в час ,осталось лететь {self.odometer} км.')
#     def land(self,приземление):
#         '''Приземление самолёта'''
#         self.is_flying = приземление
#         print(f'Самолёт {self.make.title()} модель {self.model.title()} {self.year} года выпуска при команде {self.is_flying} разрешаю садиться!')

# airbus = Airplane('airbus','g-11-52','2002','1500','10000')  
# airbus.take_off(True)
# airbus.fly()
# airbus.land(False)


# #Вариант Азата
# class Airplane():
    
#     def __init__(self, make, model, year, max_speed):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = 0
#         self.is_flying = False

#     def take_off(self):
#         self.is_flying = True
#         message_take = f"{self.make} {self.model} was take off."
#         return message_take

#     def fly(self, km):
#         self.odometer += km
#         message_fly = f"{self.make} flew {self.odometer}km at a speed of {self.max_speed}km/h."
#         return message_fly

#     def land(self):
#         self.is_flying = False
#         self.odometer = 0
#         message_land = f"{self.make} has landed, it's odometer shows {self.odometer}km."
#         return message_land

# go = Airplane("Boeing", "747", "2019", 600)
# print(go.take_off())
# print(go.fly(500))
# print(go.fly(500))
# print(go.land())




# 3)Car
# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,

# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,

# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В

# самом начале проверьте, хватит ли вам бензина из расчета того, что машина

# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,

# то пусть этот метод добавляет эти километры к значению одометра, но не

# напрямую, а с помощью приватного метода __add_distance. Помимо этого

# пусть метод drive также отнимет потраченное количество бензина с помощью

# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s

# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill

# more!”

# class Car():
#     def init(self, make, model, year):
#         self.make = make
#         self.year = year
#         self.odometer = 0
#         self.fuel = 70

#     def __add_distance(self, distance):
#         self.odometer += distance
#         print(str(self.odometer) + ' km we traveled')

#     def drive(self, distance):
#         consumption = self.fuel * 10
#         if distance > consumption:
#             print('Need to fill the tank')
#         else:
#             Car.__add_distance(self, distance)
#             will_use = distance // 10
#             Car.__subtract_fuel(self, will_use)

#     def __subtract_fuel(self, will_use):
#         self.fuel -= will_use
#         print(str(self.fuel) + ' gasoline is none')


# my_car = Car('lada', 'kalina', 2004)
# my_car.drive(500)
# my_car.drive(50)

# class Car:
#      def __init__(self,make,model,year,odometer=0,fuel=70):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odometer=odometer
#         self.fuel=fuel
#     def __add_distanse():
#         self.odometer += distance
#         print(str(self.odometer) + ' km we traveled')

#     def drive(self,distanse_km = 75):
#         self.distance_km = distanse_km
#         if self.distance_km < 100:
#             print()


# 4)ContactList
# Создайте класс ContactList, который должен наследоваться от

# встроенного класса list. В нем должен быть реализован метод

# search_by_name, который должен принимать имя, и возвращать список

# всех совпадений. Замените all_contacts = [ ] на all_contacts =

# ContactList(). Создайте несколько контактов, используйте метод

# search_by_name.

# class List:

#     def __init__(self):
#         self.all_contacts = []

#     def search_by_name(self, *name):
#         for i in name:
#             self.all_contacts.append(i.title())
#         ss = [i for i in self.all_contacts if self.all_contacts.count(i) > 1]
#         sss = set(ss)
#         print("Список совпадений: ")
#         for a in sss:
#             print("\t",a)
# class ContactList(List):

#     def __init__(self):
#         super().__init__()
# my_contacts = ContactList()
# my_contacts.search_by_name("monkey","flowers","donkey","smile","donkey","monkey","books")


# 5)AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)
# ﻿

# ﻿

# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.

# Where soldier will fire from a gun and reload, and fire one more time.


# class Soldier:
#     def __init__(self,name):
#         self.name = name

# class Gun:
#     def __init__(self):
#         self.bullets = 35

#     def AK47(self):
#         print(f"\tSoldier {self.name.title()} scream 'A-ta-ta'")
#         print(f"\t\tAK47 did: ")
#         if self.bullets:
#             piy = 0
#             for x in range(self.bullets):
#                 piy += 1
#                 self.bullets -= 1
#                 print("\t\t\tti-gi-ti-gi-tish",piy)
#         else:
#             print(f"No bullets!")
#             self.patrons()

#     def patrons(self):
#         print(f"\t\t\tBullets left {self.bullets} pieces")

#     def reload(self):
#         self.bullets = 40
#         print(f"\t\t\tSoldier {self.name.title()} scream 'REALOAD!'")

# class Act_of_Shooting(Soldier,Gun):
#     def __init__(self,name):
#         Soldier.__init__(self,name)
#         Gun.__init__(self)
#         print(f"\t\t\tBullets: {self.bullets} pieces")

# Soldier = Act_of_Shooting("Peter")
# Soldier.AK47()


#6)Furniture:
# Household type, total area and furniture name list The new house has no furniture at all.
# Furniture has a name and area,
# of whichBed: 4 square meters,Wardrobe: 2 square meters,Table:
# 1.5 square meters
# Add the above three pieces of furniture to the house
# When printing a house, output is required: household type, total area, remaining area,
# furniture name list.


class House:
    def __init__(self, area, housholdType):
        self.area = area
        self.housholdType = housholdType
    def fur(self, bed = 4, wardrobe = 2, table = 1.5):
        self.bed = bed
        self.wardrobe = wardrobe
        self.table = table

    def remarea(self):
        self.remaining_area = self.area - self.bed - self.wardrobe - self.table
a = House(120, 'old_house')
print(a.__dict__)
print
    
    # print("Total area of apartment " + str(area))
# class New_house(house):
#     def __init__(self, bed, wardrobe, table):
#         House.__init__(self, area, housholdType)
#         self.bed = bed 
#         self.wardrobe = wardrobe
#         self.table = table
#     def count_area(self, bed, wardrobe, table):
#             self.total_area = bed + wardrobe + table

#     def final_output(self)



    







# #     def __init__(self, bed, wardrobe, table):
# #         self.bed = bed
# #         self.wardrobe = wardrobe
# #         self.table = table
# #         self.totalfur = (bed + wardrobe + table)
# #     def gethouse(self):

        
# fun = House()
# print(fun.__dict__)



    # def __init__(self,furniture):
#         self.all_furniture = furniture
#         self.first_bed = all_furniture[0]
#         self.second_bed = all_furniture[1]
#         self.wardrope = all_furniture[2]
#         self.table = all_furniture[3]
#         self.chairs = all_furniture[4]
#         self.total_area = 0
#         self.type = " "

#     def count_area(self,b1,b2,wrd,tbl,chr):
#         self.total_area = b1 + b2 + wrd + tbl + chr

#     def final_output(self):
#         self.housholdType = "Full family"
#         self.remaining_area = self.area - self.total_area
#         return " ".join((str(self.remaining_area)," ".join(self.all_furniture)," ",self.type))

# all_furniture = ["First bed", "Second bed", "Wardrope","Table","Chair"]
# house = House(all_furniture)
# house.count_area(2,2,7,5,3)
# print(house.final_output())


# 7)Students room:

# Implement Students room using OOP:

# Copy
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

# class Student:
    
#     def __init__(self, name,age,profesion):
#         self.name = name
#         self.age = age
#         self.profesion = profesion


#     def output(self):
#         return "name: ",self.name, "age: ",str(self.age),"profession: ",self.profesion
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(" ".join(Steve.output()))
# print(" ".join(Johnny.output()))
# print(" ".join(Penny.output()))

#Another method
class Student():
    def __init__(self,name,age,major):
        self.name = name
        self.age = age 
        self.major = major
    
    def __repr__(self):
        return (f'\nname--{self.name}-age-{self.age}-major-{self.major}')

Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")

print(Penny)
print(Johnny)
print(Penny)



# 8)Dollar

# Create function dollarize() that takes Float and returns dollarized format:

# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Convert this function into useful class MoneyFmt. MoneyFmt contains single data value(the amount) and 4 methods.

# Copy
#     "init" //constructor initializes the data value
#     "update" //method replaces data value with new one
#     "repr" //methods returns Float valueclass Node(object):
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinaryTree(object):
#     def __init__(self,root):
#             self.root = Node(root)

#     def print_tree(self,traversal_type):
#         if traversal_type == "preorder":
#             return self.preorder_print(tree.root, " ")

#         elif traversal_type == "inorder":
#             return self.inorder_traversal(tree.root, " ")

#         elif traversal_type == "postorder":
#             return self.postorder_traversal(tree.root, " ")

#         else:
#             print("Traversal type " + str(traversal_type) + " is not supported. ")
#             return False


#     def preorder_print(self,start,traversal):
#         # """Root->Left->Right"""
#         if start:
#             traversal += (str(start.value) + "-")
#             traversal = self.preorder_print(start.left,traversal)
#             traversal = self.preorder_print(start.right,traversal)
#         return traversal
#     def inorder_traversal(self,start,traversal):
#         # """Left->Root->Right"""
#         if start:
#             traversal = self.inorder_traversal(start.left, traversal)
#             traversal += (str(start.value) + "-")
#             traversal = self.inorder_traversal(start.right, traversal)
#         return traversal
#     def postorder_traversal(self, start,traversal):
#         """Left->Right->Root"""
#         if start:
#             traversal = self.inorder_traversal(start.left, traversal)
#             traversal = self.inorder_traversal(start.right, traversal)
#             traversal += (str(start.value) + "-")
#         return traversal

# # 1-2-3-4-5-6-7-8
# # 4-2-5-1-6-3-7-8
# # 4-2-5-6-3-7-8-1
#   #             1
#   #             /\
#   #            2  3
#   #          /\   /\
#   #         4  5  6 7


# # Set up tree
# tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)
# tree.root.right.right.right = Node(8)

# # print(tree.print_tree("preorder"))
# # print(tree.print_tree("inorder"))
# print(tree.print_tree("postorder"))
#     "str" //method, that implements logic of dollarize() method

# Copy
# //The output will look like this:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567) 
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3



# class MoneyFmt:
#     def __init__(self,cash):
#         self.cash = cash

#     def update(self,cash):
#         self.cash = cash

#     def repr(self,cash):
#         self.cash = cash
#         self.cash = float(input("Enter your integer: "))

#     def str(self):
#         if self.cash >= 0:
#             return '${:,.2f}'.format(self.cash)
#         else:
#             return '-${:,.2f}'.format(-self.cash)


# cash_user = MoneyFmt(1546547835.84739)
# print(cash_user.str())
# cash_user.update(137635.795)
# print(cash_user.str())
# cash_user.repr(436346)
# print(cash_user.str())


# 9)Binary Search tree:
# https://www.getoutline.com/share/66b8b733-3e9b-4c72-938d-403ffa1d9f48

# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees﻿

# class Node(object):
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinaryTree(object):
#     def __init__(self,root):
#             self.root = Node(root)

#     def print_tree(self,traversal_type):
#         if traversal_type == "preorder":
#             return self.preorder_print(tree.root, " ")

#         elif traversal_type == "inorder":
#             return self.inorder_traversal(tree.root, " ")

#         elif traversal_type == "postorder":
#             return self.postorder_traversal(tree.root, " ")

#         else:
#             print("Traversal type " + str(traversal_type) + " is not supported. ")
#             return False


#     def preorder_print(self,start,traversal):
#         # """Root->Left->Right"""
#         if start:
#             traversal += (str(start.value) + "-")
#             traversal = self.preorder_print(start.left,traversal)
#             traversal = self.preorder_print(start.right,traversal)
#         return traversal
#     def inorder_traversal(self,start,traversal):
#         # """Left->Root->Right"""
#         if start:
#             traversal = self.inorder_traversal(start.left, traversal)
#             traversal += (str(start.value) + "-")
#             traversal = self.inorder_traversal(start.right, traversal)
#         return traversal
#     def postorder_traversal(self, start,traversal):
#         """Left->Right->Root"""
#         if start:
#             traversal = self.inorder_traversal(start.left, traversal)
#             traversal = self.inorder_traversal(start.right, traversal)
#             traversal += (str(start.value) + "-")
#         return traversal

# # 1-2-3-4-5-6-7-8
# # 4-2-5-1-6-3-7-8
# # 4-2-5-6-3-7-8-1
#   #             1
#   #             /\
#   #            2  3
#   #          /\   /\
#   #         4  5  6 7


# # Set up tree
# tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)
# tree.root.right.right.right = Node(8)

# # print(tree.print_tree("preorder"))
# # print(tree.print_tree("inorder"))
# print(tree.print_tree("postorder"))

# 10)Complex Numbers
# ﻿https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?h_r=internal-search﻿

# ﻿

# 11)Exception Decorator
# ﻿https://www.getoutline.com/share/48d8609f-dd80-4796-8a32-a62800abf1cd﻿

# ﻿

# 12)Logger Decorator:
# ﻿https://www.getoutline.com/share/63c5692f-51bb-4770-8047-566fac38bb95﻿

# ﻿

# 13)Recursive digit sum:
# ﻿https://www.hackerrank.com/challenges/recursive-digit-sum/problem﻿

# ﻿

# 14)Recursion: Davis Staircase(LRU cache)
# ﻿https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem﻿

# ﻿

# 15)Deck of Cards:
# Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:

# The Deck class should have a deal method to deal a single card from the deck
# After a card is dealt, it is removed from the deck.
# There should be a "mix" method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# Класс карты должен иметь масть (червы, бубны, трефы, пики) и ценность (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# NOTE: use random shuffle
# Copy
# from random import shuffle
# ﻿

# ﻿

# 16) Герой.

# ﻿

# Разработайте программу по следующему описанию.

# ﻿

# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня.

# ﻿

# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки.

# ﻿

# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде с более длинным списком, поднимается уровень.

# ﻿

# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.