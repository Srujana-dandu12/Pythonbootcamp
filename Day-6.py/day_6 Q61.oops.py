#overriding in polymorphism
class Animal:
    def Speak():
        return"Animal is speaking"
class Dog(Animal):
    def Speak():
        return"Dog is speaking"
class Puppy(Dog):
    def Speak():
        return"puppy is speaking"
obj3=Puppy
print(obj3.Speak())