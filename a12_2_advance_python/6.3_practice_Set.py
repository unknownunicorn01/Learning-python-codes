'''crate a list of tabel of 7 and make string of the same number vertically'''

# l=[7,14,21,28,35,42,49,56,63,70]
# l2=[str(a) for a in l]

#above code can be write as also :
l3=[str(7*i) for i in range(11)]  #we write it because join fucntion only take string as an input
joint="\n".join(l3)
print(joint)