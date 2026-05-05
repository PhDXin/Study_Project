n=int(input("Give me an integer number:"))
counter=0
inp=n
target=int(input("State the number you want to find in the digits of the integer:"))
while n != 0:
    if target==n%10:
        counter+=1
    n=n//10
print(f"{target} appears {counter} times in {inp}")

    
