'''check wether the given post is talking about shikhar ot not'''
str1="hi wether today is beautyfull"
str2="have you seen shikhar today!"
str3="do you know what shikhar is doing now a days"
str4="shikhar is a python developer"
str5="somone is learning python today"
str6="hey shikhar let study together"

resStr=input("enter your name if you want to know if any post talking about you or not: ").lower()
#we use lower() function because someone can write it in uppercase and we have everything in lower case 
#for that to work too we used lower() function
if((resStr in str1)):
  print("string 1 is talking about you")
  print(str1,"\n")
else:
  print("string 1 is not talking about you\n")

if((resStr in str2)==True):
  print("string 2 is talking about you")
  print(str2,"\n")
else:
  print("string 2 is not talking about you\n")

if((resStr in str3)==True):
  print("string 3 is talking about you")
  print(str3,"\n")
else:
  print("string 3 is not talking about you\n")

if((resStr in str4)==True):
  print("string 4 is talking about you")
  print(str4,"\n")
else:
  print("string 4 is not talking about you\n")

if((resStr in str5)==True):
  print("string 5 is talking about you")
  print(str5,"\n")
else:
  print("string 5 is not talking about you\n")

if((resStr in str6)==True):
  print("string 6 is talking about you")
  print(str6,"\n")
else:
  print("string 6 is not talking about you\n")
