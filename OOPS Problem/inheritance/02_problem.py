# Create a class 'Pets' from class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'.

class Animals:
    def sound(self):
        print("Animals can make sound")

class Pets(Animals):
    pass

class Dog(Pets):
    def sound(self):
        super().sound()
        print("Dog Sound is Bark")

animal = Animals()
pets = Pets()
dog = Dog()

print("Animals Sound")
animal.sound()
print("Pets Sound")
pets.sound()
print("Dog Sound")
dog.sound()
