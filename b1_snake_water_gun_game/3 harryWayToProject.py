'''
computer_move - your_move = 1 = win or -2 = win 
computer_mvoe - your_move = -1 = lose or 2 = lose
0 = draw


'''

import random
comp_rand=random.choice([-1,0,1])
you=input("enter your choice: ")
your_dict={"snake":-1,"water":0,"gun":1}
rev_dict={-1:"snake",0:"water",1:"gun"}
your_move=your_dict[you]
print(f"your move: {rev_dict[your_move]}\nComputer move: {rev_dict[comp_rand]}")
if((comp_rand-your_move)==1 or (comp_rand-your_move)==-2):
  print("You win")
elif((comp_rand-your_move)==-1 or (comp_rand-your_move)==2):
  print("You lose")