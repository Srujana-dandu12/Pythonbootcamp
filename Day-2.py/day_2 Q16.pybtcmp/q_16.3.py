my_list=list(map(int,input().split(" ")))
sum=0
avg=0
n=len(my_list)
for i in range (0,len(my_list)):
        sum=sum+my_list[i]       
        avg=sum/n
print(avg)      