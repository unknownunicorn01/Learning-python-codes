def fun(n):
  with open(f"practice/table{n}.txt","w") as f:
    for i in range(1,11):
      print(f"{i} X {n} = {i*n}\n".strip())
      f.write(f"{i} X {n} = {i*n}\n")

for n in range(2,21):
  fun(n)