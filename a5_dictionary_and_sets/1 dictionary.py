marks={
  "shikhar": 100,
  "rohan": 92,
  "list": [23,3,25,34],  #we can also store list
  "hi":92,
  0:"harry",
  1:0
}
print(marks["list"])  # we just have to pass teh key name and it will return the value

print(marks["shikhar"],type(marks))  #you dont have to wriet index in as a key you have to give name
print(marks[1])
print(marks.items())  # will give all the key and value sotred in it
print(marks.values())  #we will get the value of the items stored
print(marks.update({"shikhar":101}),"\n",marks.items())  # we can update the value
#add item in the list
print(marks.update({"Renuka":100}),marks.items())
print(marks.get("shikhar"))  
print(marks.get("ranvir"))
'''we get the marks in marks["shikhar"] and marks.get("shikhar")
but if the item not exist in first condition it will give error and if in 
the second item dose not exist it will give NONE and not erroe'''

