'''chect if the file exist or not if file exit then print yes it exist
but if file not exist use exception handeling for showing error 
and so the code also not cresh'''

import os

print("following program checks that the files exist or not: ")

# check=input("enter the file name:")
# if(os.path.exists(f"{check}.txt")):
#   print("yes this file exist")
# else:
#   print("This file dose not exist")

try:
  with open("file1.txt","r") as f:
    print(f.read())
except Exception as e:
  print(e)
try:
  with open("file2.txt","r") as f:
    print(f.read())
except Exception as e:
  print(e)
try:
  with open("file3.txt","r") as f:
    print(f.read())
except Exception as e:
  print(e)


print("\nThank you, for showing that our code did not cresh but still runing")