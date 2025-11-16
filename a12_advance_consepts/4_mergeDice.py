'''in this we are going to learn how to merge dictnary in advanve python'''

dict1={
  "shikhar":19,
  "rank": 1
}
dict2={
  "everyone": 13,
  "rank": 2  # because i wrote rank two time so the second one will be priouritize
}
marge = dict1 | dict2
print(marge)

# dict1.update({dict2})
# print(dict1)
'''we comment it out because it will not work if you want to marge two dictnary you have to
use following: 
marge = dict2 | dict2
now it marge dict 1 and dict 2 in marge 
'''