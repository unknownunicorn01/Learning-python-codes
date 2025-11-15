set1={1,32,43,12,234,"shikhar"}
set1.add(330)
print(set1,type(set1))

'''
  propertiese of set
    1. sets are unordered
    2. set is unindexed
    3. you cant change items in set
    4. set can not contain duplicate values
'''

print(len(set1))

#we can remove the element from the set
set2=set1
set2.remove(330)  # we revmore th
print(set2)

#we have another method called "union"

set3={1,2,3,4}
set4={"shikhar","lol","aditiya","ayush"}
print(set3.union(set4))  #both set will be printed in one set

#intersection
#it allow you to write common value from the sets
print(set1.intersection(set3))  # common element in both will be printed

#for subtracting 
print(set3-set1)

#to check if the value is in the set of not
print({1,2}.issubset(set3))  #output True
print(set3.issubset({1,2}))  #will return False because set3 is not a subset of {1,2}

set5=set3.copy()  # we created a coly of the set 3 and store in set5
print((set5).issubset(set3))  #return True because set 5 is a copy fot set 3 which mean it will have all the element of set3 
#so set 5 is a subset of set3

#pop element
set3.pop()  #first element is been removed
print(set3)  #will pop first value from the set and return rest of the set 
#push element
set3.add(1) #will add the elemtn in the first inside the set
print(set3)  #return the new set

#to check is a set is a superset or not

set6={1,2,3,4,5,6}
set7={1,2,3,4,5}
print((set6).issuperset(set7))  #will return True because set7 is subset of set6 and set6 is superset of set7

