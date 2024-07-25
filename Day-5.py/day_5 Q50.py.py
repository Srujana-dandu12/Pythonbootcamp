#check how many vowels are there in a string
str=input()
vowel="aeiou"
count=0
for i in (str):
    if(i in vowel):
        count+=1
print(count)