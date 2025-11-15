'''wrtie multiplication table from 2 to 20 and 
store them in deffrent files and store them in a folder name 13 year old'''

def genrate_table(n):
  table=""
  with open(f"5.3.1file/table{n}.txt","w") as f:
    for i in range(1,11):
      table=f"{n} X {i} = {n*i}\n"
    
      f.write(table)
for n in range(2,21):
  genrate_table(n)





    
