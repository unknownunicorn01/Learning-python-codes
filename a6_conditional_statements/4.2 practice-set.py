'''write a prograam which check wether the stdents has failed or pass the test
   take 3 subject as an input calculate aveage marks, percentage, and tell in whcih 
   subjects they have failed, take input from the user of the 3 subject marks'''

s1=int(input("enter you marks out of 25 in subject 1: "))
s2=int(input("enter you marks out of 25 in subject 2: "))
s3=int(input("enter you marks out of 25 in subject 3: "))
if(s1<=25 and s2<=25 and s3<=25 and s1>=0 and s2>=0 and s3>=0):
   if(s1>=33*25/100 and s2>=33*25/100 and s3>=33*25/100):
      print("you passed in all subjects")
      print("congratulations")
   elif(s1<33*25/100 and s2>=33*25/100 and s3>=33*25/100):
      print("you passed in subjects 2 and 3")
      print("you failed in subject 1")
   elif(s1>=33*25/100 and s2<33*25/100 and s3>=33*25/100):
      print("you passed in subjects 1 and 3")
      print("you failed in subject 2")
   elif(s1>=33*25/100 and s2>=33*25/100 and s3<33*25/100):
      print("you passed in subjects 1 and 2")
      print("you failed in subject 3")
   elif(s1<33*25/100 and s2<33*25/100 and s3>=33*25/100):
      print("you passed in subjects 3")
      print("you failed in subject 1 and 2")
   elif(s1>=33*25/100 and s2<33*25/100 and s3<33*25/100):
      print("you failed in subjects 2 and 3")
      print("you passed in subject 1")
   elif(s1<33*25/100 and s2>=33*25/100 and s3<33*25/100):
      print("you failed in subjects 1 and 3")
      print("you passed in subject 2")
   elif(s1<33*25/100 and s2<33*25/100 and s3<33*25/100):
      print("you failed in subjects 1, 2 and 3")
      print("you failed in all subjects")

   avg=(s1+s2+s3)/3
   print(f"Your avrage marks: {avg}")
   per=(s1+s2+s3)*100/75
   print(f"your percentage is: {per}%")
else:
   print("invalid marks")

print("end of the program")

