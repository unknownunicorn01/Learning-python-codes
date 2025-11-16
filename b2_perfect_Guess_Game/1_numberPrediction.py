import random
import os

computerNumber=random.randint(1,100)
print(computerNumber)
yourGuess=int(input("enter your guess: "))

i=1
while yourGuess!=computerNumber:
  if(yourGuess>computerNumber):
    print("Your guess is greater then computer guess!!")
  elif(yourGuess<computerNumber):
    print("Your guess is smaller then computer guess!!")
  yourGuess=int(input("enter your guess: "))
  i+=1

print(f"Congratulations you find correct number in {i} attempts!!")
print("\n Now your friend's chance to guess the number!!")

computerNumber2=random.randint(1,100)
print(computerNumber2)
friendGuess=int(input("Guess the number: "))

j=1
while friendGuess!=computerNumber2:
  if(friendGuess>computerNumber2):
    print("Your guess is greater then computer guess!!")
  elif(friendGuess<computerNumber2):
    print("Your guess is smaller then computer guess!!")
  friendGuess=int(input("enter your guess: "))
  j+=1

print(f"Congratulations you find correct number in {j} attempts!!\n")
result=""
if(i>j):
  result="Your friend win!!!"
  print(f"\n{result}\nYour friend's attempts: {j}\nYour attempts: {i}\n")
elif(j>i):
  result="You win!!!"
  print(f"\n{result}\nYour attempts: {i}\nYour friend's attempts: {j}\n")
elif(i==j):
  result="Draw!!"
  print(f"\n{result}\nYour attempts: {i}\nYour friend's attempts: {j}\n")

print("\nThanks for playing!\nHope you enjoyed.")

save=input("Do you want to save this in saperate file? : (Yes/No) ").lower()

if save!="yes" and save!="no":
  k=1
  while save!="yes" and save!="no":
    print("Please answer in Yes or No only!")
    save=input("Do you want to save this file? : (Yes/No) ").lower()
    k+=1
if save=="yes":
  name=input("What would you like to name you file? : ")
  fileName=f"{name}.txt"
  if name=="Result":
    print("You can't name file Result because it is a default file to save all data.\nTry another name")
  else:
    if os.path.exists(f"result/{fileName}"):
      save2=input("File name already exist, do you want to replace this file? : (Yes/No)").lower()
      if(save2=="no"):
        choice=input("Do you want to append in file? : (Yes/No): ").lower()
        if(choice=="yes"):
          with open(f"result/{fileName}","a") as f:
            f.write(f"\n{result}\nYour attempts: {i}\nYour friend's attempts: {j}")
          with open(f"result/Result.txt","a") as f:
            f.write(f"\n{result}\nYour attempts: {i}\nYour friend's attempts: {j}")
        elif(choice=="no"):
          new_name=input("What would you like to name you file? : ")
          with open(f"result/{new_name}.txt","a") as f2:
            f2.write(f"\n{result}\nYour attempts: {i}\nYour friend's attempts: {j}")
          with open(f"result/Result.txt","a") as f:
            f.write(f"\n{result}\nYour attempts: {i}\nYour friend's attempts: {j}")
    else:
      with open(f"result/{fileName}","a") as f:
        f.write(f"\n{result}\nYour attempts: {i}\nYour friend's attempts: {j}")
elif(save=="no"):
  with open(f"result/Result.txt","a") as f:
    f.write(f"\n{result}\nYour attempts: {i}\nYour friend's attempts: {j}")