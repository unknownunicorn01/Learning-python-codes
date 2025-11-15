'''every file you write will sotre itself in RAM which is a volitile memory
which mean it will not there permanently, after restarting you computer it all will be gone

for ex:
  a = [a very long string with emails]
  
  email=[]
  3 seconds(take to open)
  and gone #but you dont want it to end and to store
  like we store everything in a file like hdd hard drive, ssd which are non-volitile mempry
  which mean that it will be there even if you restart you computer
  
  
  RAM is volitile and hard drive is non-volitile, so why we use RAM?
  we use RAM because it is face compaired to hard drive
  
  a python program can talk to a file which allow use to reade or write in a file
  python is also a text file which can be read or do the reading from the another file
  for example: (bellow code)'''

f=open("2 exampleFile.py" , "r")  #open is a inbuilt function which allow you to open another file in this and read
data = f.read()  #here we read the content of the file
print(data)  #here we print the date inside the file
f.close()  #and after the work is done we close the file

'''it can also have the text file or another programing file it will return 
the text writen inside it

There are two types of file 
1 Text files (like .txt , .c , .p etc)
2 Binary files (like .jpg , .dat etc)

in open() function we have to pass 2 values 1 is name of that file and mode "r" for read
but in open fuction this "r" mode is already decleared so even if we dont write it, it will work

there is another mode where we write "w" we can use it for writin an string in another file 
or we can also create another file and write any text in it
for example: (code given bellow)
'''
str=input("enter the string you want to enter in the file: ")

f1=open("myfile.txt","w")  #we open a file with open() function if file dont exist it will create one
data2=f1.write(str)  #it will write the text we give input in that file
f1.close()  #we close the file, if we dont it will run anyway but we should close it onece the code is exicuted

