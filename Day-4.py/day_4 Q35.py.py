#to print GCD of a given numbers
a=int(input())
b=int(input())
while b!=0:
    a,b=b,a%b
print("GCD of 2 numbers is :",a)