'''there are more functions in python in files I/O 
like 
1 readline() and readlines()  #these both are functions 
for ex:(given bellow code)'''
#for readline()
# f=open("myfile.txt")  #dont need to wright "r" because it is already in read mode by defalt
# line1=f.readline()  #it will read only one lines
# print(line1, type(line1))
# line2=f.readline()
# print(line2, type(line2))
# line3=f.readline()
# print(line3, type(line3))
# line4=f.readline()
# print(line4, type(line4))
# line5=f.readline()
# print(line5=="", type(line5)) #if we tell to print line 5 it will not print anythin but will return type string
#     #but if we equat to empty string then it will print ture because it will see that line5 is a empty string
                
# f.close()

# '''same code above can be write by using while loop'''
# f=open("myfile.txt")
# line=f.readline()
# while(line!=""):
#   print(line,type(line))
#   line=f.readline()
# f.close()



# #for readlines()
# f=open("myfile.txt")  #dont need to wright "r" because it is already in read mode by defalt
# data=f.readlines()  #it will read all lines
# print(data, type(data))  #it will print it in list form and class will be printed as list
# f.close()

#for appending a line in file
apstr=input("enter the string you want to append: ")
f1=open("myfile.txt","a")
data1=f1.write(apstr)   #at the end it will print the line we want to enter in that file
print(data1)
f1.close()