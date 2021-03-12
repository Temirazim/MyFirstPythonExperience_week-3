# №1
# Создайте класс Factory и внутри создайте 2 метода:
# Метод engine который возвращает строку "Двигатель создан"
# Метод bridge который возвращает строку "Ходовая часть создана"

# №2
# Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory. В классе Toyota создайте методы wheels и windows.
# Метод wheels возвращает строку "Колёса готовы"
# Метод windows возвращает строку "Стёкла готовы"
# Из класса Toyota вызовите все методы, методы вернут вам строки(объекты)
# Результат каждого метода вставьте в лист

# class Factory:
  
#     def __init__(self, engine, bridge):
#         self._engine = engine
#         self._bridge = bridge
    
#     def engine(self):
#         return self._engine

#     def bridge(self):
#         return self._bridge

# a = Factory('Двигатель создан', 'Ходовая часть создана')

# print(a.engine())
# print(a.bridge())
 
# class Tayota(Factory):
#     def __init__(self, engine, bridge, wheels, windows):
#         super(Tayota, self).__init__(engine, bridge)
#         self._wheels = wheels
#         self._windows = windows
#     def wheels(self):
#         return self._wheels
#     def windows(self):
#         return self._windows
# b = Tayota('Двигатель создан', 'Ходовая часть создана',"колеса готовы", "стекла готовы")

# print(b.wheels())
# print(b.windows())



# №3
# Создайте Класс Zoo.
# Инициализируйте класс в объект.
# К объекту Zoo добавьте атрибут animal_1 и присвойте ему значение "Тигр"
# К объекту Zoo добавьте атрибут animal_2 и присвойте ему значение "Бегемот"
# К объекту Zoo добавьте атрибут animal_3 и присвойте ему значение "Жираф"
# В объекте Zoo измените значение атрибута animal_1 и присвойте ему значение "Лев".
# К объекту Zoo добавьте атрибут animal_4 и присвойте ему list состоящий из animal_2 и animal_3
# В объекте Zoo измените значение атрибута animal_3 и присвойте ему значение "Змея".

class Zoo:
    def __init__(self, animal_1 = "tiger", animal_2 = "begemot", animal_3 = "giraff"):
        self.animal_1 = animal_1
        self.animal_2 = animal_2
        self.animal_3 = animal_3
        self.animal_1 = 'lion'
        self.animal_4 = [animal_2, animal_3]
        self.animal_3 = 'snake'
       
anim = Zoo()
print(anim.__dict__)


