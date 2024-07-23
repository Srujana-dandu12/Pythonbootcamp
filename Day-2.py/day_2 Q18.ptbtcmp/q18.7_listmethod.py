my_list=list(map(int,input().split(" ")))
print("enter 1 to append")
print("enter 2 to pop")
print("enter 3 to sort")
print("enter 4 to find the length")
choice=int(input())
if(choice==1):
    my_list.append(89)
    print(*my_list)
elif(choice==2):
    my_list.pop(2)
    print(*my_list)
elif(choice==3):
    my_list.sort()
    print(*my_list)
else:
    print(f"good morning!The length of the list is {len(my_list)}")    

    
