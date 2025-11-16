num=int(input("enter the number: "))
p='00'
l=[]
l2=[]
i=1
while(i*i<=num):
  l.append(i*i)
  l2.append(i)
  i+=1
sq=l[len(l)-1]
a=l2[len(l)-1]
a2=0
ab=int()
num2=int(str(num-sq)+p)

l3=[]
while (ab*a2)<num2:
  ab=int(str(2*a)+str(a2))
  l3.append((ab*a2)%(num2))
  a2+=1

ab2=ab+a2-1
print(ab2)
print(l3)
# print(f"your root is= {a+(a2-1)/10}")

num3=int(str(num2-l3[len(l3)-1]) + p)
a3=0
ab3=int()
l4=[]
while ab3*a3<num3:
  ab3=int(str(ab2)+str(a3))
  l4.append((ab3*a3)%num3)
  a3+=1
print(l4)
print(ab3,ab3*a3)
print(num3)
print(a3)
print(f"root of number: {num} is: {a+(a2-1)/10 + (a3-1)/100}")
  


    