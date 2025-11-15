'''write a program to tell the gread of the student based on there marks mentioned bellow
    90-100 => exc
    80-90 => A
    70-80 => B
    60-70 => C
    50-60 => D
    50> => F'''

marks=int(input("enter you marks: "))
if(marks>=90 and marks<=100):
  print("Your result is \"excelent\"")
elif(marks>=80 and marks<90):
  print("You get the grade \"A\"")
elif(marks>=70 and marks<80):
  print("You get the grade \"B\"")
elif(marks>=60 and marks<70):
  print("You get the grade \"C\"")
elif(marks>=50 and marks<60):
  print("You get the grade \"D\"")
elif(marks<50 and marks>=0):
  print("You get the grade \"F\"")
else:
  print("You entered invalid marks!!!")

print("end of program!")

