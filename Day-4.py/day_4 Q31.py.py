#to print a peak element in a given array
my_list=list(map(int,input().split(" ")))
for i in range(0,len(my_list)-1):
    if(my_list[i]>my_list[i+1] and my_list[i-1]):
        print(f"the peak element is{my_list[i]}")