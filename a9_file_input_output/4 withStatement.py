'''many time people forget to write close() statement or writing it may seems like burder for some people
for that we use with statement which allowes use to write acciss file
and close it by itself without out help but we have to write code after the indentation
for ex: (code given bellow)'''
with open("myfile.txt","r") as f:  #r is not nessery for the read files because it is default in python
  data=f.readline()
  print(data)