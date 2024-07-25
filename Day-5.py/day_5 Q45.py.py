#tp remove (),{},[] in a  givengalgebraic expression 
str=input()
for i in (str):
    if(ord(i)==91 or ord(i)==93 or ord(i)==123 or  ord(i)==125 or ord(i)==40 or ord(i)==41):
         pass
    else:
         print(i,end=" ")