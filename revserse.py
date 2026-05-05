n=int(input("int:"))
accumulator = 0
n1 = n
while n1 >0:
	accumulator=accumulator*10
	accumulator+=n1%10
	n1=n1//10
if accumulator==n:
	print("Palindrome")

else:
	print("False")
