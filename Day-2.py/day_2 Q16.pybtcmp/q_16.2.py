my_list=list(map(int,input().split(" ")))
sum=0
avg=0
count=0
for i in range (0,len(my_list)):
    if(i%2==0):
        sum=sum+my_list[i]  
        count+=1     
        avg=sum/count
print(avg)      