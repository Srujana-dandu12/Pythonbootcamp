#to print the sum of the digits given in a string
str=input()
sum=0
check="0123456789"
for i in (str):
    if(i in check):
        sum+=int(i)
print(sum)
