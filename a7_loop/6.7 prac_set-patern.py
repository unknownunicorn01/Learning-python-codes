'''draw the patern in the python programing by using for loop
  *
 ***
*****'''
# i=5
# j=1
# while(i>=1 and j<=5):
#   print(f"{" "*i}{"*"*j}")
#   j+=2
#   i-=1

# #same code using for loop
# for i in range(1,6,2):
#   space=int((4-(i+1)/2))
#   print(f"{" "*space}{"*"*(i)}")


'''taking input from the user how many line peramif they want'''

line=int(input("enter the line of peramid you want"))
for i in range(1,line*2,2):
  print(f"{int((i+1)/2)}: {" "*int(((line*2)-i)/2)}{"*"*i}")


#code chat gpt gave
'''
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
  print(" " * (n - i) + "*" * (2 * i - 1))
  '''