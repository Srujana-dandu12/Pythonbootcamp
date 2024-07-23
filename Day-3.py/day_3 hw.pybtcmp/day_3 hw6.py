#sum of squares of odd digits and even digits in a number
n=int(input())
sum1=0
sum=0
while(n>0):
    r=n%10
    if(r%2>0):
        sum1=sum1+r**2
    else:
        sum=sum+r**2
    n=n//10
print(f"the sum of squares of odd digits in number {sum1}")
print(f"the sum of squares of even digits in number {sum}")