list=["shikhar","rahul",5,3.14,True,"aditiya"]
list.append("ayush")  #add "ayush" a string at the last of the list
print(list)
list.insert(3,8)  #it will insert 8 at the 3rd index
print(list)  
list.remove("rahul")  #it will remove rahul from the list
print(list)
list.pop(3)  #it will pop value in the index 3
print(list)
print(list[0:4])  #it will print list from index 0 to 3


list2=[2,32,43,1,34,64,23,4]  # create a new list which only includes number because of sort methord
list2.sort()  # it will short list2 in decending order
print(list2)
list2.reverse()  #it will write list in reverse oder
                #so if you want to write list in accending order you just have to write it after sort list
print(list2)
