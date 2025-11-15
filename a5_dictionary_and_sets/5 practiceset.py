#take input from the user in hindi and give english translation
dict={
  "hindi": "english",
  "kya haal hai" : "how are you",
  "kya kar raha ho": "what are you doing",
  "kaha ho": "where are you"
}

lang=input(f'''options to translate are:
  "hindi": "english",
  "kya haal hai" : "how are you",
  "kya kar raha ho": "what are you doing",
  "kaha ho": "where are you"
enter the word you want in hindi or english: ''')
print(dict[lang] or dict.key([lang]))

#take 8 number from the user and display all the unique number at once
''' s=set()
print(type(s))
n=int(input("enter the number of element you want to enter: "))
for i in range(1,n+1):
  num=int(input(f"enter the number {i} you want: "))
  s.add(num)
print("Your unique numbers are: ",s)  '''

#since we havemt learn loops yet we will do without loops
#take 8 number from the user and display all the unique number at once
s=set()
print(type(s))

s1=int(input("enter the number you want to add in the set: "))
s2=int(input("enter the number you want to add in the set: "))
s3=int(input("enter the number you want to add in the set: "))
s4=int(input("enter the number you want to add in the set: "))
s5=int(input("enter the number you want to add in the set: "))
s6=int(input("enter the number you want to add in the set: "))
s7=int(input("enter the number you want to add in the set: "))
s8=int(input("enter the number you want to add in the set: "))
s.add(s1)
s.add(s2)
s.add(s3)
s.add(s4)
s.add(s5)
s.add(s6)
s.add(s7)
s.add(s8)

print(s)

#chech wether 18 can be put as an int and str or not
st1=input("enter the string \"18\": ")
in1=int(input("enter the number 18: "))
set1={st1,in1}
print(set1)  

'''and the concluson it that we can write it as an string and integer
   and both will be writen because int and str are deffrent datatypes
   but is you try to give to 18 as a string or integer will only print onetime'''


#calculate the lengthe of the following string
'''
s9=set()
s9.add(20)
s9.add(20.0)
s9.add("20")  # output will be 2
'''
s9=set()
s9.add(20)
s9.add(20.00)
s9.add("20")
print("s9 set is: ",s9)  # it will consider int value and float valut same because float have .00 after it so both are equal
print("lengthe of the set is: ",len(s9))  # output will be 2

#tell teh type of s10
'''s10={}'''

s10={}
print(type(s10))  # it will be a dictnary type because we declear empty dictnary like this


#declear an empty dictnary and allow 4 friend to enter the language and key as there name
#assuming there mane are unique
dic={}
language1=input("enter the language you like: ")
name1=input("enter you name 1: ")
language2=input("enter the language you like: ")
name2=input("enter you name 1: ")
language3=input("enter the language you like: ")
name3=input("enter you name 1: ")
language4=input("enter the language you like: ")
name4=input("enter you name 1: ")
dic.update({language1:name1})
dic.update({language2:name2})
dic.update({language3:name3})
dic.update({language4:name4})
print(dic.items())

key1=input("enter language as input to get the name: ")
print(f"enter the name and get the language: {dic[key1]}")

'''if the name of two friend are same the code will have no effect
because they are the keys but is the language are same then
the second language decleared with first name will replacs the first'''

'''CODE WITH HARRY APPROACH TO SOLVE THIS PROBLEM
  dictnary1={}   #we create an empty dictnary
  name=input("enter the name of friend: ")
  lang=input("enter the language they like: ")
  dictnary1.update(name:lang)      #we update the dictnary and add the value in it
  name=input("enter the name of friend: ")
  lang=input("enter the language they like: ")
  dictnary1.update(name:lang)
  name=input("enter the name of friend: ")
  lang=input("enter the language they like: ")
  dictnary1.update(name:lang)
  name=input("enter the name of friend: ")
  lang=input("enter the language they like: ")
  dictnary1.update(name:lang)
                                #just like this we add all the value in it by just two variable to take input
  print(dictnary1)
  '''



#check wether the list in the set is mutable or not?
"""s11={8,7,12,"harry",[1,2]}"""

s11={8,7,12,"harry",[1,2]}
print(s11)  #show error because list are not hashable(CWH said)
        #insted you can use tupples which are immutable

'''will show error because it only allow immputable elements like int, float, str
   you can use tuples insted of list because tuples are immutable,
   you can not use list, dictenary, or another set inside a set'''