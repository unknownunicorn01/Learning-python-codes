with open("log.html","r") as f:
  data=f.read()
word = input("ehter the work you want to search: ")
if(word in data):
  print(f"{word} is in that file")
elif(word not in data):
  print(f"{word} is not in that file")