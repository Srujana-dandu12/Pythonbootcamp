#given an space separated integer list finf the avg of elements present the even index.
my_list=list(map(int,input().split(" ")))
sum=0
avg=0
n=len(my_list)
for i in range (0,len(my_list)):
    if(i%2==0):
        sum=sum+my_list[i]       
        avg=sum/n
print(avg)        