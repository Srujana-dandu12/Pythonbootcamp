#given string is like i/p:ABC and the o/p:EFG
str=input()
for i in (str):
    if(ord(i)>=65 or ord(i)<=97):
        print(chr(ord(i)+4),end="")
         