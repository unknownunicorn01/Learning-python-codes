file_name=input("enter the name of file you want to copy from: ")
file_name2=input("enter the name of file you want to past to: ")
with open(file_name,"r") as f:
  data=f.read()

with open(file_name2,"w") as f:
  f.write(data)

# import time
# n=int(input("after how much time do you want you code to run:"))
# if n%2==0:
#   time.sleep(n)
#   print("done exicution, lol!!!")
# else:
#   print("code run for odd number!!")