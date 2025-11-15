#take imput from the user to write 7 fruits name in you list
list=[]
la1=input("enter fruit 1: ")
list.append(la1)
la2=input("enter fruit 2: ")
list.append(la2)
la3=input("enter fruit 3: ")
list.append(la3)
la4=input("enter fruit 4: ")
list.append(la4)
la5=input("enter fruit 5: ")
list.append(la5)
la6=input("enter fruit 6: ")
list.append(la6)
la7=input("enter fruit 7: ")
list.append(la7)

print(list)

#enter the marks of student and sort them in decending order
list2=[]
lb1=int(input("enter marks of student 1: "))
list2.append(lb1)
lb2=int(input("enter marks of student 2: "))
list2.append(lb2)
lb3=int(input("enter marks of student 3: "))
list2.append(lb3)
lb4=int(input("enter marks of student 4: "))
list2.append(lb4)
lb5=int(input("enter marks of student 5: "))
list2.append(lb5)
lb6=int(input("enter marks of student 6: "))
list2.append(lb6)
lb7=int(input("enter marks of student 7: "))
list2.append(lb7)


print(list2)
list2.sort()
list2.reverse()
print("sorted list:",list2)

#take 4 number in the list and add them
list3=[3,2,8,4]
print(sum(list3))