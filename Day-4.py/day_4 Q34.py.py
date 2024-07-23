#swapping a number without using temparary variable
a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a,b)