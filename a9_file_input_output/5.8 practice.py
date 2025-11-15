'''write a python program to find out that content of a file matches the content of
another file or not'''

with open("file.txt","r") as f:
  data=f.read()

with open("log.html","r") as f:
  data2=f.read()

if(data==data2):
  print("yes the conten of the file matches")
else:
  print("no the content of the file do not matches")