x=input()
y=int(input())
apples=int(input())
bananas=int(input())
orange=int(input())
applescost=apples*15
bananascost=bananas*4
orangecost=orange*5
totalcost=0
totalcost=applescost+bananascost+orangecost
if(totalcost<y):
        print(f"{x} is not cheated by shopkeeper")
else:
     print(f"{x} is cheated by shop keeper")