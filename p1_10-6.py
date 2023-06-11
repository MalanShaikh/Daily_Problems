'''There is a sentence : The fox jumped over the wall. Find frequency of each word n print it in dictionary'''
sentence="The fox jumped over the wall"

tokenize_sent= sentence.split(" ")

freq={}

for word in tokenize_sent:
	word=word.lower()
	if word in freq.keys():
		freq[word]+=1
	else:
		freq[word]=1

print(freq)
