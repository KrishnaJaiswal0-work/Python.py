class Animal:
   pass


class Pets(Animal):
    pass


class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow! Bow!")

a = Animal()
c = Dog()
c.bark()