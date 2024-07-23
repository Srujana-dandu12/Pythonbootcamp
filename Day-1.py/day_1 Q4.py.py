x=input()
y=int(input())
print("enter no.of apples")
apples=int(input())
print("enter no.of banans")
bananas=int(input())
print("enter no.of oranges")
orange=int(input())
cost_apple=15
cost_banana=4
cost_orange=5
totalcost=0
totalcost=applescost+bananascost+orangecost
if(totalcost<y):
        print(f"{x} is not cheated by shopkeeper")
else:
     print(f"{x} is cheated by shop keeper")