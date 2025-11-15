with open ("5.4.1 page.txt","r") as f:
  content = f.read()

words=["donkey","bad","sad"]

for word in words:
  content = content.replace(word,"#"*len(word))

with open("5.4.1 page.txt","w") as f:
  f.write(content)
