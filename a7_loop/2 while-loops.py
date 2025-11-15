# i=1
# while(i<5):  #while loop is another way for looping
#   print("hellow python")
#   i+=1                          #another interesting way to drag a line down is by (alt+down)
#   #now the value of i is also changed and become 5
#   print(i)  #output 5
# '''it will chech the condition like in above example
# i is smaller then 5 so code is exicuted
# i is increseed by 1 in i+=1
# then it again went to while loop where it will run because
# i become 2 which is still smaller then 5
# and will continew until i=4
# '''

# #question run a while look which print number from 1 to 50
# i2=1
# while(i2<=50):  #it will chek the condition == it not true which mean code will not exicute so we use <=
#   print(i2)
#   i2+=1

#Que2. Write a program to print the items of the list
l1=["shikhar","yash","ayush","ravi","rahul",1,2,3,4,3.14]
print(l1[0])
i3=0
while(i3<len(l1)):  #we dont write <= because len will give length and we set i=0 and index always start with 0
  print(l1[i3])
  i3+=1

'''even better way to do for look(suggested by chat gpt)
for item in l1:
  print(item)'''