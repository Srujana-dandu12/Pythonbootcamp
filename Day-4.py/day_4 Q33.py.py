#to print peak element if it present in the last position 
my_list=list(map(int,input().split(" ")))
count=0
for i in range(0,len(my_list)-1):
    if(my_list[i]>my_list[i+1] and my_list[i-1]):
        count=i
    if(my_list[-1]>my_list[-2] and my_list[-1]>count):
        count=len(my_list)-1
print(my_list[count])