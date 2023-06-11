# Check given string is pallindrome or not

string= input("Enter string: ")

#rev=string[::-1]

rev=""

for i in string:
	rev= i+ rev

if(string==rev):
	print("Its a pallindrome")
else:
	print("Its not pallindrome")

