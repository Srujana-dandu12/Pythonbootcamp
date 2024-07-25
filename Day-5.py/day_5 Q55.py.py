#reverse of a numerics in a given string
str=input()
str1=""
rev=0
check="0123456789"
for i in (str):
    if(i in check):
        str1.append(int(i))
    while int(str1)>0:
        r=str1%10
        rev=10*rev+r
        str1=str1/10
print(rev)