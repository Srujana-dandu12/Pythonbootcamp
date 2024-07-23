#find max number in  a given list
#testcase1:
# 12 34 67 89
#o/p:89
my_list=list(map(int,input().split(" ")))
max=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
print(max)