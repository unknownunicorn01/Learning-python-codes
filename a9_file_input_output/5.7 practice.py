'''write a python program to copy a file and save it in another file name file.txt'''
with open("log.html","r") as f:
  data = f.read()

with open("file.txt","w") as f:
  content=f.write(data)
  