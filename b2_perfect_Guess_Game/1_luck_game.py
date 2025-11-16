'''GTA-7: LUCKY DRAW!!!'''
import random


# yourChoice=input("Enter you choice out of ('A' / 'B' / 'C') : ").upper()

# while yourChoice!="A" and yourChoice!="B" and yourChoice!="C":
#   yourChoice=input("Sorry!, But you can only chose out of ('A' / 'B' / 'C') : ").upper()

# print(yourChoice)
r11=random.randint(1,3)
r12=random.randint(1,3)
r13=random.randint(1,3)
r21=random.randint(1,3)
r22=random.randint(1,3)
r23=random.randint(1,3)
r31=random.randint(1,3)
r32=random.randint(1,3)
r33=random.randint(1,3)

v11=""
v12=""
v13=""
v21=""
v22=""
v23=""
v31=""
v32=""
v33=""


if r11==1:
  v11="A"
elif r11==2:
  v11="B"
elif r11==3:
  v11="C"

if r12==1:
  v12="A"
elif r12==2:
  v12="B"
elif r12==3:
  v12="C"

if r13==1:
  v13="A"
elif r13==2:
  v13="B"
elif r13==3:
  v13="C"

if r21==1:
  v21="A"
elif r21==2:
  v21="B"
elif r21==3:
  v21="C"

if r22==1:
  v22="A"
elif r22==2:
  v22="B"
elif r22==3:
  v22="C"

if r23==1:
  v23="A"
elif r23==2:
  v23="B"
elif r23==3:
  v23="C"

if r31==1:
  v31="A"
elif r31==2:
  v31="B"
elif r31==3:
  v31="C"

if r32==1:
  v32="A"
elif r32==2:
  v32="B"
elif r32==3:
  v32="C"

if r33==1:
  v33="A"
elif r33==2:
  v33="B"
elif r33==3:
  v33="C"

print(f"{v11} | {v12} | {v13}\n{v21} | {v22} | {v23}\n{v31} | {v32} | {v33}")
# print(f"{r11} | {r12} | {r23}\n{r21} | {r22} | {r13}\n{r31} | {r32} | {r33}")
if v21==v22 and v22==v23:
  print(f"v21: {v21}\nv22: {v22}\nv23: {v23}\nyou win")
else:
  print(f"v21: {v21}\nv22: {v22}\nv23: {v23}\nyou lose")