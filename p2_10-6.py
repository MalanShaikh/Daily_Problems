# There is a list : [1,3,5,2,6,8,0] find second Max and second min element in the list

nums=[1,3,5,2,6,8,0]

min1=99
min2=99
max1=0
max2=0
for i in range(len(nums)):
	if(nums[i]>max1):
		max2=max1
		max1=nums[i]
	if(nums[i]<min1):
		min2=min1
		min1=nums[i]

print("Second Max in list: ", max2)
print("Second Min in list: ", min2)
		

	

# Another approch: sort list and then find second max and min
'''nums=sorted(nums)

print("second max: ", nums[-2])
print("Second min: ", nums[1])

'''