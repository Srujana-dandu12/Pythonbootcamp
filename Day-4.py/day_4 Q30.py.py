#Mr.x is trying to create a new password for instagram account there are 
#the require conditions for creating a new password
#case1:Min len is 8
#     Max len is 15
#case 2:only @,/is allowed in password
#case 4:only 'alpha' numerics are allowed
#you are supposed to print weak if length is exact 8
#medium -lengthis b/w  8 to 12
#strong - length is b/w 12 to 15
str=input()
count=0
len=len(str)
if(len(str)>=8 and len(str)<=15):
    print("password is allowed")
else:
    print("follow the conditions")