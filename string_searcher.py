s=input("Please give me the string you want to analyse:")
search=input("Please give me the exact string you want me to search:")
length1=len(s)
length2=len(search)
counter=0
for i in range(length1):
	if s[i:i+length2] == search:
		counter+=1
print(counter)

