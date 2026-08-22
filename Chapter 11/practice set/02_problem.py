# Create a class 'pets' from a class 'Animals' and future create a class 'Dog' from 'pets'. Add method 'bark' to class 'Dog'
class Animals:
    pass

class pets(Animals):
    pass

class Dog(pets):
    @staticmethod
    def bark():
        print("Woof! Woof!")

d = Dog()
d.bark()