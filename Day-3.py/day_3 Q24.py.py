#find the missing numner in a given list
my_list=list(map(int,input().split()))
sum1=0
sum=0
for i in range(1,11):
    sum=sum+i
for i in range(len(my_list)):
    sum1=sum1+my_list[i]
missing_num=sum-sum1
print(missing_num)    