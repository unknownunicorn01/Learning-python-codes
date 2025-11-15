'''search the word and the line in which tha word comes'''
# word=input("enter the work you want to search: ")
# with open("log.html","r") as f:
#   data=f.readlines()

# for i in range(0,len(data)):
#   if(f" {word} " in data[i] or f" {word}" in data[i]):
#     print(f"\"{word}\" word is in the line\n\"{data[i]}\"")
#     print(f"In line number: {data.index(data[i+1])}")
#   else:
#     print(f"{word} is not present in paragraph")

with open("log.html","r") as f:
  data=f.readlines()

lineno=1
for line in data:  #here it will run every line in the file
  if "python" in line:  #here it will check every work in th line
    print(f"python is present in {lineno}")
    break
  lineno+=1  #the numbers of line increase

else:
  print("word python not found in the file")