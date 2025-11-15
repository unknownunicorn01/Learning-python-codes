import random  #it is a module  inside the standerd liberary of python
random_float = random.random()
print(f"random number is: {random_float}")  #will print a random numbe rbetween 0 to 1 also exclude 0 and 1

num=random.uniform(10,20)  #store the value of floating point number of betwern 10 to 20
print(num)
num2=random.randint(1,100)  #store the number in integer form between 1 to 100
print(num2)