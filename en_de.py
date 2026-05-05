message = input("Please enter your message here:")
option = input("Enter de for decrypting or en for encrypting:")
output=""
if option == "de":
	for i in message:
		output=output+chr((ord(i)-1))
	print(output)
elif option ==  "en":
	for i in message:
		output=output+chr(ord(i)+1)
	print(output)
else:
	print("Error:No correct option provided.")
