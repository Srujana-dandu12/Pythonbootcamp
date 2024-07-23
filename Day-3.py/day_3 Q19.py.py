#find the element present in k+Nth Index
#testcase1: k=3 N=2
# 3 6 8 4 6 1 2
#o/p->1
#test case2:k=3 N=4
#80 70 54 36 72
#o/p -> error
my_list=list(map(int,input().split(" ")))
k=int(input())
N=int(input())
len=len(my_list)
if(len<(k+N)):
    print("ERROR")
else:
    for i in range(0,len):
        print(my_list[k+N],end=" ")
        break
