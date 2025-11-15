import random
your_move=input("Which one do you chose (Snake, Water or Gun): ").lower()
while your_move!="snake" and your_move!="water" and your_move!="gun":
  print("invalid input!!")
  your_move=input("Which one do you chose (Snake, Water or Gun): ").lower()
computer_num=random.random()
computer_move=""
for i in range(1,6):
  if computer_num>0 and computer_num<(1/3):
    computer_move="snake"
    print(computer_num)
  elif computer_num>1/3 and computer_num<(2/3):
    computer_move="water"
    print(computer_num)
  elif computer_num>2/3 and computer_num<1:
    computer_move="gun"
    print(computer_num)

  result=""
  print(f"computer move: {computer_move}")
  if your_move==computer_move:
    print(f"your move:{your_move} ,and computer move:{computer_move}")
    print("it is a draw")
    result="draw"
  elif your_move=="snake" and computer_move=="water":
    print(f"your move:{your_move} ,and computer move:{computer_move}")
    print("Your win,congrates!!")
    result="win"
  elif your_move=="snake" and computer_move=="gun":
    print(f"your move:{your_move} ,and computer move:{computer_move}")
    print("Your lose!")
    result="lose"
  elif your_move=="gun" and computer_move=="water":
    print(f"your move:{your_move} ,and computer move:{computer_move}")
    print("Your lose!")
    result="lose"
  elif your_move=="gun" and computer_move=="snake":
    print(f"your move:{your_move} ,and computer move:{computer_move}")
    print("Your win,comgrates!!")
    result="win"
  elif your_move=="water" and computer_move=="gun":
    print(f"your move:{your_move} ,and computer move:{computer_move}")
    print("Your win, Congrates!!")
    result="win"
  elif your_move=="gun" and computer_move=="snake":
    print(f"your move:{your_move} ,and computer move:{computer_move}")
    print("Your lose!")
    result="lose"
