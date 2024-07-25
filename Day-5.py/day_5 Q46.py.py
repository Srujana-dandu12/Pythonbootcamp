#to print sumof digits in a string using ascii
str=input()
sum=0
for i in (str):
    if(ord(i)>=48 and ord(i)<58):
        sum+=int(i)
print(sum)