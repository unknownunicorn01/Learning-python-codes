#tkae name input from the user and print good afternoon user
name=input("enter you name:")
print(f"Good Afternoon {name}")

#print the follow in the correct sequence and replace name with user real name and date with today date
str="""Dear <|Name|>
      You are selected!
      <|Date|>"""
print(str.replace("<|Name|>","Shikhar Dutta").replace("<|Date|>","15/June/2025"))  # this is known as chaining of function

#write a python program to detect double space in the string
space="hi  hellow"
print(space)
print("double space is in the index:",space.find("  "))
with
#replace double space from single space in the string
print("here we replace double space with single space:",space.replace("  "," "))

print("""Dear Shikhar
this Python code is nice
Thanks!""")