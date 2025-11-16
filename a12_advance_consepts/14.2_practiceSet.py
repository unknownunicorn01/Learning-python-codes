'''create a list and add value it is, then print the value at place 3,5,7'''

l=[1,2,3,4,5,6,7,8]

for index, item in enumerate(l):
  if index==2 or index==4 or index == 6:
    print(f"The element in index {index} are {item}")