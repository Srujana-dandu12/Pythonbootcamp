#find min number in  a given list
#testcase1:
# 12 34 67 89
#o/p:12
my_list=list(map(int,input().split(" ")))
min=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<min):
        min=my_list[i]
print(min)