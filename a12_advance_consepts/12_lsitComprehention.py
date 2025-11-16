myList=[2,4,3,7,9,8]
'''
squareList=[]
for item in myList:
  squareList.append(item*item)

print(squareList)
'''
#in above we use for loop for appending the value of square for the value in myList
#we can do the same my using list comprihantion in more efficient way

squareList=[item*item for item in myList]
#it will also print the same but in efficient way
print(squareList)