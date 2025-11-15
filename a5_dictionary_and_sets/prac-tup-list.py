# l1=[1,2,3,4,5]
# list2=[l1[0]*l1[0],l1[1]*l1[1],l1[2]*l1[2],l1[3]*l1[3],l1[4]*l1[4]]
# print(list2)

# list3=list(x**2 for x in l1)
# print(list3)

# la=float(input("enter the value of the float: "))
# la1=int(input("enter teh value of the int: "))
# la2=input("enter the string value: ")
# set1={la,la1,la2}
# print(type(la))
# print(type(set1),set1)
# print(len(set1))


dictnary1={}   #we create an empty dictnary
name=input("enter the name of friend: ")
lang=input("enter the language they like: ")
dictnary1.update({name:lang})      #we update the dictnary and add the value in it
name=input("enter the name of friend: ")
lang=input("enter the language they like: ")
dictnary1.update({name:lang})
name=input("enter the name of friend: ")
lang=input("enter the language they like: ")
dictnary1.update({name:lang})
name=input("enter the name of friend: ")
lang=input("enter the language they like: ")
dictnary1.update({name:lang})
                                #just like this we add all the value in it by just two variable to take input
print(dictnary1)


'''we watched till '''