'''write a content to wipe out the content of the file py python'''

# with open("wipeout.txt","r") as f:
#   line=f.readlines()

# for i in range(0,len(line)-1):
#   with open("wipeout.txt","w") as f:
#     line.pop(i)


#or you can just leave the space blank it will replace the content in it compleatly
with open("wipeout.txt","w") as f:
  f.write("")

print("code has been exicuted,\nContent in the file has been erased!")


  