age1=19
dict={
  "name":"shikhar",
  "age": str(age1)+" years",
  "room":3.14,
  "male":True,
  "marks":[100,98,99,94,99]
}
print(dict.items())

#1 dict.clear  
dict.clear() #clear the existing dictenary
print(dict.items())  #items in the dictnary are cleared

dict2={
  "a":1,
  "b":2,
  "c":3,
  "d":4,
  "e":5
}

print(dict2.items())

#copy of the list
dict3=dict2.copy()
print(dict3.items())

#you can get the value of the key you want by entering the value of that
print(dict2.fromkeys("c",0))
print(len(dict2))