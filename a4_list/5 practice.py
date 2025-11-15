# write a list to store 7 fruit from the user

l0=input("enter 1st fruit the you want: ")
l1=input("enter 2nd fruit the you want: ")
l2=input("enter 3rd fruit the you want: ")
l3=input("enter 4th fruit the you want: ")
l4=input("enter 5th fruit the you want: ")
l5=input("enter 6th fruit the you want: ")
l6=input("enter 7th fruit the you want: ")

li=[l0,l1,l2,l3,l4,l5,l6]
print("fruits entered by the user are: \n",li)


#wrtie a program to accpet marks of the studend and display it on the screen
laS1=input("enter the name of the student1: ")
la1=input("enter the marks of student 1: ")
laS2=input("enter the name of the student2: ")
la2=input("enter the marks of student 2: ")
laS3=input("enter the name of the student3: ")
la3=input("enter the marks of student 3: ")
laS4=input("enter the name of the student4: ")
la4=input("enter the marks of student 4: ")

li2=[laS1+f":{la1} marks",laS2+f":{la2} marks",laS3+f":{la3} marks",laS4+f":{la4} marks"]
print(li2)

#check that tuple type can not be change in python

# enter a program to calculate the sum of number in the list
li3=[23,32,4,3]
print(li3[0]+li3[1]+li3[2]+li3[3])

#count the number of 0 int the list
listA=[1,0,0,0,0,0]
print(listA.count(0))