def sta(status):
  match status:
    case 201:
      return "greater then 200"
    case 199:
      return "smaller than 200"
    case _:
      return f"number is undefine"

#it mostly work as switchcase

print(sta(39))