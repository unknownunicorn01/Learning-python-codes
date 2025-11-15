'''change the name of the file'''

with open("name.txt","r") as f:
  data=f.read()

with open("rename.txt","w") as f:
  f.write(data)  #content of the old file has been copyed in another file and now you can delete the old file
               # for deleting file on program you need to install some modules but for now do it manully
               