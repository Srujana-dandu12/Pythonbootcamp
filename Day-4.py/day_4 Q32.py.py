#to print a peak elements in a given array
my_list=list(map(int,input().split(" ")))
count=0
for i in range(0,len(my_list)-1):
    if(my_list[i]>my_list[i+1] and my_list[i-1]):
        print(my_list[i],end=" ")