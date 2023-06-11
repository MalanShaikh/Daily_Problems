string="hello my name is Malan"

# solution-1
length1=len(string)
print(length1)

#solution-2
length2=0
for char in string:
	length2+=1
print(length2)

#solution-3
length3= string.__len__()
print(length3)

#solution-4
from functools import reduce

length4 = reduce(lambda acc, _: acc + 1, string, 0)
print(length4)