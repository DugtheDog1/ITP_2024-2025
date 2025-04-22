orchard = [24,52,12,23,43,32,33,12,19,24,42,52,37,27,31,43,34,24]

#Apple count function
def countAppleTree(treeValue,basketValue):
     numOfApples = orchard[treeValue]
     basketValue = 0
     print("This is the number of apples for tree",treeValue + 1)
     while numOfApples > 0:
         print("There are",numOfApples,"apples on the tree and",basketValue,"number of apples in the basket")
         print("I pick one apple and put it in the basket")
         basketValue += 1
         numOfApples -= 1
         if numOfApples == 0:
             print("")

startBasketValue = 0
for z in range(len(orchard)):
     countAppleTree(z, startBasketValue)
     startBasketValue = startBasketValue + 1

#1/1 - Formatting
#1/1 - Comments
#2/3 - Content
#You didn't print the baskets out at the end.