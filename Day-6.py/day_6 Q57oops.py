class Myclass:
   # def __init__(self,a,b):
      #  self.a=a
        #self.b=b
    def add(a,b):
        return a+b
    def sub(a,b):
        return abs(a-b)
    def mul(a,b):
        return a*b
    def mod(a,b):
        return a%b
    def divide(a,b):
        return a/b
obj1=Myclass
obj2=Myclass
obj3=Myclass
obj4=Myclass
obj5=Myclass
print(obj1.add(2,5))
print(obj2.sub(6,3))
print(obj3.mul(2,5))
print(obj4.mod(4,2))
print(obj5.divide(3,6))
