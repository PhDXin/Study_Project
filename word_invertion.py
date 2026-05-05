message=input("Enter your text:")
remessage=''
l=len(message)
counter=1
for i in message:
	remessage=remessage+message[l-counter]
	counter+=1
if remessage==message:
	print("Yes")
else:
	print("No")
	
