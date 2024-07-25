#to demonstrate multi level inheritance
class Animal:
    def Speak():
        return"Animal is speaking"
class Dog(Animal):
    def Bark():
        return"bow..."
class Puppy(Dog):
    def puppy_speak():
        return"iam puppy"
obj3=Puppy
print(obj3.Speak())
print(obj3.Bark())
print(obj3.puppy_speak())
