''' input Array: [1,2,3,4,5,5,3,5,4,4,4,1,5,5,5,5]
Print elements having frequency more or equal to 4'''

array= [1,2,3,4,5,5,3,5,4,4,4,1,5,5,5,5]
freq={}

for i in  range(len(array)):
	if array[i] in freq.keys():
		freq[array[i]]+=1
	else:
		freq[array[i]]=1
	
	
answer=[x for x in freq if freq[x]>=4]

print(answer)


