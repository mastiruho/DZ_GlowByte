from abc import ABC, abstractmethod
from queue import Queue


class Animal(ABC):
    # класс абстрактного животного
    # объект имеет protected атрибут name - кличка
    def __init__(self, name):
        self.__CheckName(name)
        self._name = name

    # метод класса, служащий для проверки того, что кличка является строкой
    @classmethod
    def __CheckName(cls, name):
        if type(name) is not str:
            raise TypeError('Кличка должна быть строкой')

    # абстрактный метод "издать звук"
    @abstractmethod
    def MakeNoise(self):
        pass

    # абстрактрый метод получения информации о животном
    @abstractmethod
    def GetFullInfo(self):
        pass

    # свойство кличка - метод get
    @property
    def name(self):
        return self._name


class PetAnimal(Animal):
    # класс домашнего животного
    # объект наследует name от Animal,
    # а также имеет private атрибут ownerName - имя хозяина
    def __init__(self, name, ownerName):
        super().__init__(name)
        self.__CheckOwnerName(ownerName)
        self.__ownerName = ownerName

    @classmethod
    def __CheckOwnerName(cls, ownerName):
        if type(ownerName) is not str:
            raise TypeError('Имя хозяина должно быть строкой')

    # свойство ownerName - имя хозяина, метод get
    @property
    def ownerName(self):
        return self.__ownerName

    # свойство ownerName - имя хозяина, метод set с проверкой типа
    @ownerName.setter
    def ownerName(self, value):
        self.__CheckOwnerName(value)
        self.__ownerName = value

    # переопределение метода MakeNoise класса Animal
    def MakeNoise(self):
        return f'''"{self._name}" издаёт звуки домашнего животного'''

    # переопределение метода GetFullInfo класса Animal
    def GetFullInfo(self):
        return f'''"{self._name}" - хозяин {self.__ownerName}'''


class WildAnimal(Animal):
    # класс дикого животного
    # объект наследует name от Animal,
    # а также имеет private атрибут animalType - вид животного
    # разрешенные виды хранятся во множестве animalTypes - атрибут класса
    animalTypes = {'волк', 'лиса', 'медведь'}

    def __init__(self, name, animalType):
        super().__init__(name)
        self.__CheckAnimalType(animalType)
        self.__animalType = animalType

    @classmethod
    def __CheckAnimalType(cls, animalType):
        if type(animalType) is not str:
            raise TypeError('Вид животного должен быть строкой')
        if animalType not in cls.animalTypes:
            raise ValueError(f'''{animalType} - такого вида животного нет''')

    @property
    def animalType(self):
        return self.__animalType

    # переопределение метода MakeNoise класса Animal
    def MakeNoise(self):
        return f'''"{self._name}" издаёт звуки дикого животного'''

    # переопределение метода GetFullInfo класса Animal
    def GetFullInfo(self):
        return f'''{self.__animalType} "{self._name}"'''


class Veterinarian:
    # класс ветеринара
    # объект имеет private атрибут name - имя
    def __init__(self, name):
        self.__CheckName(name)
        self.__name = name

    @classmethod
    def __CheckName(cls, name):
        if type(name) is not str:
            raise TypeError('Имя должна быть строкой')

    # метод класса для проверки того,
    # яляется ли переданный объект экземпляром класса Animal
    @classmethod
    def __CheckAnimal(cls, animal):
        if not isinstance(animal, Animal):
            raise TypeError(f'''"{animal}" не животное!''')

    # метод лечения животного
    def Heal(self, animal):
        self.__CheckAnimal(animal)
        print(f'''Ветеринар {self.__name} начал лечение {animal.GetFullInfo()}''')
        print(animal.MakeNoise())
        print(f'''Лечение "{animal.name}" закончилось''')


if __name__ == '__main__':
    q = Queue()  # очередь, хранящая различных животных
    pet = PetAnimal('Пушок', 'Катя')
    pet.ownerName = 'Катя Пушкова'
    q.put(pet)
    q.put(WildAnimal('Серый', 'волк'))
    q.put(PetAnimal('Барбос', 'Петя'))
    # q.put(10)
    vet = Veterinarian('Вася')

    while not q.empty():
        vet.Heal(q.get())
