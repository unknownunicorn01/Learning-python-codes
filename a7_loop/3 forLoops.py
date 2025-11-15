''' we declear for loop in following way:
for i in range(start_value, ending_value, stap_size):
  in this i will the starting value you declear
  ending will be the value it will check condition till
  and step_size is the step it will jump in he code'''

for i in range(0,50,4): #it will print every 4th number from the first one
  print(i)  # it already assume that i=+1 so you dont have to write it

#pritn a list using for loop
l1=[1,2,2,3,4,5,6]
for i2 in range(0,len(l1)):  #last value is not included
  print(l1[i2])  

#print a tuple in the for loop
t1=("shikhar","aditiya","shrey",1,2,3)
print(len(t1))
for i3 in range(0,len(t1)):
  print(t1[i3])

#you can also write string in foe loops
str="shikhar"
for i4 in range(0,len(str)):
  print(str[i4])