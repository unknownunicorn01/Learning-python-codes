'''a spam message is define by the following keyword:
"make a lot of money", "buy now", "subscribe this", "click here".
write a program to detact this message 
'''
list1=["make a lot of money", "buy now", "subscribe this", "click here"]
mess=input("enter the message you want to send: ")
if((list1[0] in mess)==True or (list1[1] in mess)==True or (list1[2] in mess)==True or (list1[3] in mess)==True):
  print("this is a spam message")
else:
  print("you may proceed")



