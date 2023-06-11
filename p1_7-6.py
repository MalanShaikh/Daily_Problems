'''Input 2 arrays with varying no of integer elements
Arr1 =[2,4,5,6]
Arr2=[5,6,7,8,9]
Write a program to output elements which are there in arr1 but not in arr2 and vice-versa. 
Expected Output:[2,4,7,8,9]'''


Arr1 =[2,4,5,6]
Arr2= [5,6,7,8,9]
Arr3= list(set(Arr1)-set(Arr2))
Arr4=list(set(Arr2)-set(Arr1))
Arr5=Arr3+Arr4
print(Arr5)

# Another approach
'''Arr1 =[2,4,5,6]
Arr2= [5,6,7,8,9]

Arr3=[]
for i in Arr1:
	if i not in Arr2:
		Arr3.append(i)
for j in Arr2:
	if j not in Arr1:
		Arr3.append(j)

print(Arr3)'''



