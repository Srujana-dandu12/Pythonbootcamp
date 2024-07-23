#check whether given number is armstrong or not
n=int(input())
x=n
y=n
count=0
while n>0:
    r=n%10
    count=count+1
    n=n//10
sum=0
while x>0:
    r=x%10
    sum=sum+(r**count)
    x=x//10
if sum==y:
    print(y,"is an armstrong number")
else:
    print(y,"is not an armstrong number")