#to print nonrepeating letters in a string
str=input()
vowel="aeiou"
consonant="bcdfghjklmnpqrstvwxyz"
ans=""
for i in (str):
    if(i not in ans):
        ans+=i
print(ans)