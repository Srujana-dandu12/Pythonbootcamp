#write a program to print the count of the consonants in a string
str=input()
vowel="aeiou"
consonant="bcdfghjklmnpqrstvwxyz"
count=0
for i in (str):
    if(i in consonant):
        count+=1
print(count)