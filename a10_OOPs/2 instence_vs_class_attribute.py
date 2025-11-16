class employ():
  language="python"  #this is a class attribute
  salery=1200000

shikhar=employ()
shikhar.language="javascript"  #this is a instence attribute
print(shikhar.language,shikhar.salery)  #here language javascript will be printed 
  #because instence class have more prefrence then onject class
  #at first it will check that is the attribut present in onject if not it will check in class

#but if you want to print class attribute insted of instence attribute
print(employ.language)  #now it will print class attribute