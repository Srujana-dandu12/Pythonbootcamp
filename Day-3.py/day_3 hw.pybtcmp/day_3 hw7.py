#palindrome
n=int(input())
x=n
rev=""
while(n>0):
    r=n%10
    rev=rev+str(r)
    n=n//10
    ans=int(rev)
print(rev)
if(ans==x):
    print("palindrome")
else:
    print("not a palindrome")