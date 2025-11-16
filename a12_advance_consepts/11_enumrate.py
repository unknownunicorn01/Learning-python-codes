l=[1,23,21,32,34,343]
'''
index=0
for item in l:
  print(f"The item at number of index {index} is {item}")
'''
#the above code work after we create two variables and assigning them value manually in index

#but using enumerate it will given them value by itself

for index, item in enumerate(l):
  print(f"The item at number of index {index} is {item}")
  #by this write can be reduced by one line and can do to improve you coding skills with advance python
