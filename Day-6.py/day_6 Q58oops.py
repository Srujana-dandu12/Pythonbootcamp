#to demonstrate single inheritence
class Animal:
    def Speak():
        return"Animal is speaking"
class Dog:
    def Bark():
        return"bow..."
obj1=Animal
obj2=Dog
print(obj1.Speak())
print(obj2.Bark())