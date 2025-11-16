'''we also use typing for importing defrent methods'''
from typing import List, Tuple, Dict, Union

num:List[int]= [1,23,"h",3,4]
tup:Tuple[str,int] = (1,2,3,"a","b")


'''we will tell the code the return type, mostly used in functions'''
def fun(a:int , b: int) -> list[int]:
  return [a,b]
print(fun(1,2))