n=int(input("Enter an integer:"))
accumulator=1
counter=1
while counter <= n:
    accumulator = accumulator*counter
    counter+=1
print(f"The factorial of the number entered is:{accumulator}")
