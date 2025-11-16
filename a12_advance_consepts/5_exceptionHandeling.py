try:
  a=int(input("enter the numbner: "))
  print(a)
except ValueError as b:
  print(b)  #here you  can rase an error if you want is a is not an integer 
  # we need this because we dont want out code to crase and even if it crase it still works
  #like is the value enter is not an int value thank you will still be printed

print("thank you")