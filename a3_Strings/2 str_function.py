# #first importent function we have is len
# name="shikhar"
# len1=len(name)
# print(len1)

string=input("enter the string you want to enter: ")
strName=string[:]
print("Your string",strName)
findStr=input("enter the string you want to find: ")
findStr1=string.find(findStr)
print("you word is: ",findStr1)
rep=input("incase you misstype any word do you want to replace it: yes or no: ")

if(rep=="yes"):
  rep1=input("enter a word you want to replace: ")
  rep2=input("enter the word you want to replace with: ")
  print(strName.replace(rep1,rep2))
elif(rep=="no"):
  print("your word is",strName)
