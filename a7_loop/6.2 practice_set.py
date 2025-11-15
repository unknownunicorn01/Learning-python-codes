#write a python program to greet every person in the list whose name starts with S
num_of_name=int(input("enter the number of name you want to enter: "))
l=[]

for i in range(num_of_name):
  name=input("enter the name you want: ").upper()
  l.append(name)

print(l)


for i in range(0,len(l)):
  flet=l[i][0]
  if(flet != "S"):    #or we can also use name.startswith(S)
    continue
  print(f"{l[i]} : Namestay")