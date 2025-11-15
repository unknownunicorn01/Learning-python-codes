'''the game() function in a program lets a user play a game and return tehbscore as an integer.
You need to read the file "5.2.1 game.txt" which is either blank or contain the previous 
hi-score. You need to write a program to update the high-score whenever the game() function
break the high score'''


import random
def game():
  
  with open("5.2.1 game.txt", "a") as f:
    rounds=int(input("enter teh rounds you want to play: "))
    for i in range(0,rounds):
      comp_choice=random.randint(0,1)
      your_choice=int(input("\nenter your choice 0 or 1 : "))
      you=""
      if(your_choice!=1 and your_choice!=0):
        print("wront input,\nplease enter only \"1\" or \"0\"!!!\n")
        i-=1
      else:
        print(f"your choice: {your_choice} , Computer choice: {comp_choice}")
        data=f.write(f"your choice: {your_choice} , Computer choice: {comp_choice}\n")
        if(your_choice==comp_choice):
          you="you win"
          print(you)
          data=f.write(f"{you}\n")
        elif(your_choice!=comp_choice):
          you="you lose"
          print(you)
          date=f.write(f"{you}\n")
    

game()

with open("5.2.1 game.txt","r") as f1:
  score=f1.read()
  print(f"Your win score: {score.count("you win")}")




