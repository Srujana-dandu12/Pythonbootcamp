#to print LCM of a given numbers
a=int(input())
b=int(input())
c=a*b
while b!=0:
    a,b=b,a%b
    LCM=c//a
print("LCM of 2 numbers is :",LCM)