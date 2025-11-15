'''remove a number from the list and strip it at the same time using function in python'''
def fun():
  l=[]
  n=int(input("how many elements you want in your list: "))

  for i in range(0,n):
    l1=(input("input the element you want:")).strip()
    l.append(l1)
  print(f"Your current list: {l}")
  ask=input("Do you want to remove any item from the list (yes or no): ").lower()
  while(ask !="yes" and ask != "no"):  #remember to write and because if you write or it will check if both yes and no present at the same time
    print("please enter Yes or No only!!!")
    ask=input("Do you want to remove any item from the list (yes or no): ").lower()
  if ask=="no":
    print(f"you current list: {l}")
  elif ask=="yes":
    rem=input("which index you want to remove:") 
    while(rem in l)==False:
      print(f"element {rem} is not presnt in the list!")
      rem=input("which index you want to remove:")

  # del l[rem-1]  #we use del function for deleting an elemetn from the list in that index
  l.remove(rem)  #if thr values comes mulitple times, it will only remove first value
  print(f"you current list: {l}")
  print(f"element {rem} has been removed")

fun()