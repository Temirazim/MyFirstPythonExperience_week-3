# Нужно создать класс который принимет модель ноутбука(Acer, Asus, ...) и возвращает полную комплектацию ноутбука со всеми характеристиками.
# В характеристики должны входить:
# Процессор
# Оперативная Память
# Видео карта
# Жёсткий Диск
# Материнская плата
# Размер экрана
# Для каждой характеристики создайте внутри класса функцию которая добавляет по одной характеристики к Dictionary.
# В итоге Ваш класс должен вернуть Dictionary в котором перечислены: 
# Модель Ноутбука и его Характеристики.

# class Lenovo:
#     def __init__ (self, 'процессор'= 'AMD_2020', 'Оперативная_карта' = '8gb'', 'Видео_карта' = '12', 'Жесткий_диск'= 'SSD-256gb'', 'Материнаская_плата' = '161', 'Размер_экрана' = '15')
#     self.'процессор'= 'AMD_2020' = 'процессор'= 'AMD_2020'
#     self.'Оперативная_карта'= '8gb' = 'Оперативная_карта'= '8gb'
#     self.'Видео_карта'= '12' = 'Видео_карта'= '12'
#     self.'Жесткий_диск'= 'SSD-256gb' = 'Жесткий_диск'= 'SSD-256gb'
#     self.'Материнаская_плата'= '161' = 'Материнаская_плата'= '161'
#     self.'Размер_экрана'= '15' = 'Размер_экрана'= '15'

#     def get_lenovo(self):
#         print(f{self.процессор,self.Оперативная_карта,self.Видео_карта,self.Жесткий_диск,self.Материнская_плата,self.Размер_экрана})
#Мой метод
# class Lenovo():
#     def __init__(self, processor, ram, video_card, jestkii_disk, display_size):
#         self.processor = processor
#         self.ram = ram
#         self.video_card = video_card
#         self.jestkii_disk = jestkii_disk
#         self.display_size = display_size
#     def __str__(self):
#         return f"processor: {self.processor}, ram: {self.ram},video_card: {self.video_card}, jestkii_disk: {self.jestkii_disk}, display_size: {self.display_size}"
# nout = Lenovo('16', '4gb', '10', '1000', '16*3')
# print(nout)



#Вариант Аймиры
# class Lenova:
#     def __init__(self, Процессор, ОперативнаяПамять, Видеокарта, ЖёсткийДиск, Материнскаяплата, Размерэкрана):
#         self.Процессор = Процессор
#         self.ОперативнаяПамять = ОперативнаяПамять
#         self.Видеокарта = Видеокарта
#         self.ЖёсткийДиск = ЖёсткийДиск
#         self.Материнскаяплата = Материнскаяплата
#         self.Размерэкрана = Размерэкрана
        
#     def get_Lenova_info(self):
#         print({'Процессор': self.Процессор, 'ОперативнаяПамять': self.ОперативнаяПамять, 'Видеокарта': self.Видеокарта, 'ЖёсткийДиск': self.ЖёсткийДиск, 'Материнскаяплата': self.Материнскаяплата, 'Размерэкрана': self.Размерэкрана})

# s = Lenova('AMD-0420', 12, 'GTX1050', 'SSD 256', '128', 16.5)
# s.get_Lenova_info()


#№2
# Нужно создать класс который принимет данные в формате dict. Эти данные, вы сможете взять из Classroom Data #1.
# Вам нужно создать 6 методов класса:
# Получить все ключи в TUPLE.
# Получить все значения в TUPLE.
# Получить все ключи в LIST.
# Получить все значения в LIST.
# Получить все ключи в SET.
# Получить все значения в SET.
# Ниже когда вы будете передавать Словарь классу он и вызывать из него любой метод Вы должны получать соответсвенно нужные типы данных.
# Example: my_class = Parser("DICT") | my_class.get_keys_tuple()

# №3
# Нужно создать класс который принимает Classroom Data #2 данные.
# И внутри класса создать несколько методов:
# Метод который вернёт все имена отелей.
# Метод который из собирает все name в один Tuple и locations в другой и возвращает dictionary c двумя ключами списками со всеми значениями.
#  3.Метод который добавит к каждому элементу в markers поле 
# status_id: 1

# Data #2:
# data = {
# "markers": [
# {
# "name": "Rixos The Palm Dubai",
# "position": [25.1212, 55.1535],
# },
# {
# "name": "Shangri-La Hotel",
# "location": [25.2084, 55.2719]
# },
# {
# "name": "Grand Hyatt",
# "location": [25.2285, 55.3273]


class Hotels():
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def mark1(self):
        return self.name
    def mark2(self):
        return tuple(self.name)
        return tuple(self.location)
        return f("'name': {self.name}\n'location': {self.location}")
        lst = []
        lst.append(f"'name': {self.name}\n'location': {self.location}")
        return lst
    # def ma
            
    
a = Hotels("Rixos The Palm Dubai", "[25.1212, 55.1535]")
b = Hotels("Shangri-La Hotel", [25.2084, 55.2719])
c = Hotels("Grand Hyatt", [25.2285, 55.3273])
print(a.mark1())
print(" ".join(a.mark2()))
print(b.mark1())
print(b.mark2())
print(c.mark1())
print(c.mark2())



    
