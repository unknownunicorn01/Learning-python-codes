import os
with(
  open("file1.txt","r") as f,
  open("file2.txt","r") as f2  #like this we can open multiple file in one with statement
):
  data=f.read()
  print(data)
  data2=f2.read()
  print(data2)
  if os.path.exists("file3.txt"):
    print("yes this file exist")
    