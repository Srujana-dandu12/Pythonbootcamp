#sum of all elements in an array
my_list=list(map(int,input().split(" ")))
sum=0
for i in range(len(my_list)):
    sum=sum+my_list[i]
print(sum)