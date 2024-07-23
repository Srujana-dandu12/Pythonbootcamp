#print the element in a particular index(cyclic manner)
#testcase1: k=3
#3 4 5 6 7 8 
#o/p: 6
#testcase2: k=5
# 10 20 30 40
#o/p: 20
my_list=list(map(int,input().split()))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])