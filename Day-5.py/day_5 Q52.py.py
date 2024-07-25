#write a program to print vowels and consonants separate in astring
str=input()
vowel="aeiou"
consonant="bcdfghjklmnpqrstvwxyz"
ans=""
for i in (str):
    if(i in consonant):
        ans+=i
for i in (str):
    if(i in vowel):
        ans+=i
print(ans)