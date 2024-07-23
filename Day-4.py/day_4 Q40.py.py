#print all the leap years in a given range
n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    if(i%400==0 or i%4==0 and i%100!=0):
        print(i,end=" ")