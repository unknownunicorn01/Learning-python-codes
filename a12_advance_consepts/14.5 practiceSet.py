'''store the tabel in practice set 3 in a txt file'''
import os
item=int(input("enter the number: "))
l2=[item*i for i in range (1,11)]
print(l2)
if os.path.exists("tables/") == False:
  os.mkdir("tables")
with open("tables/table.txt","a") as f:
  f.write(str(l2)+"\n")
